import requests
import asyncio


async def getall():
    res = requests.get("http://127.0.0.1:8000/items")
    print(res.json())

items = [
    {"title": "title 1"},
    {"title": "title 2"},
    {"title": "title 3"},
    {"title": "title 14"},
]

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYXJhaEBkb2UuY29tIiwiZXhwIjoxNzAzMTkyNDU2fQ.AikR5b-HrrVmuLLcGeA2MseBn7uBUnjPqjCzUlH2vBI"
}


async def create_many():
    res= requests.post("http://127.0.0.1:8000/items", json=items, headers=headers)
    print(res.json())
# res = requests.post("http://127.0.0.1:8000/items", json={"title": "hello wolrd"})

asyncio.run(create_many())