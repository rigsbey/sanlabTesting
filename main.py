from sanic import Sanic
from sanic.response import json, text
import requests
from sanic import response

app = Sanic("valute")

@app.route("/course/<currency>")
async def get_currency(request, currency):  
  url = 'https://www.cbr-xml-daily.ru/daily_json.js'
  resp = requests.get(url)
  data = resp.json()
  return response.json({"currency":currency, "rub_course": data['Valute'][currency]['Value']})

@app.route(methods=["POST"], uri="/api/convert")
async def test(request):  
  url = 'https://www.cbr-xml-daily.ru/daily_json.js'
  resp = requests.get(url)
  data = resp.json()

  amount = float(request.args["amount"][0])
  if(request.args["from_currency"][0] == "RUB"):
      return response.json({"currency":request.args["to_currency"][0], "Result": round(amount / data['Valute'][request.args["to_currency"][0]]['Value'], 2)})
  elif(request.args["to_currency"][0] == "RUB"):
    return response.json({"currency":request.args["to_currency"][0], "Result": round(amount * data['Valute'][request.args["from_currency"][0]]['Value'], 2)})  
  else:
    # Рублей
    rub = amount * data['Valute'][request.args["from_currency"][0]]['Value']
    # Валюты на выходе
    resultValue = round(rub / data['Valute'][request.args["to_currency"][0]]['Value'], 2) 
    return response.json({"currency":request.args["to_currency"][0], "Result": resultValue})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)