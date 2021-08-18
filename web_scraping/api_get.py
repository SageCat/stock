import requests
from pandas import json_normalize

request = requests.get("http://localhost:3000/api/citys")
data = request.json()
print(type(data))
df = json_normalize(data, record_path='response')
print(df)
