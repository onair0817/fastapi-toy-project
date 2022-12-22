import requests
import json


# request url
url = "http://localhost:8000/items/"

# data
data = {"name": "new_challenge", "description": "test1", "price": 2020, "tax": 2021}

# post request to api
res = requests.post(url, data=json.dumps(data))

# print response
print(res.text)
