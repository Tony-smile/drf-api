
import requests
import json

#endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

data_result = requests.get(endpoint, json=={"product_id": 123})


#print(data.json())
print(data_result)

print(data_result.status_code)