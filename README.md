# sanlabTesting

Runs on the host 0.0.0.0:8000
For change host to 127.0.0.1, use -p 127.0.0.1:8000:8000 when you run this docker container

__________________________
# GET /api/course/<currency>
Example:
GET /api/course/USD
__________________________  
# POST /api/convert
{
    "from_currency": <string>,
    "to_currency": <string>,
    "amount": <float>
}
Example:
  POST /api/convert
{
    "from_currency": "USD",
    "to_currency": "RUB",
    "amount": 134
}
