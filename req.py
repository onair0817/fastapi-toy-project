import requests
import json


# ---
# api /items/
# ---

# request url
url = "http://localhost:8000/items/"

# data
data = {"name": "new_challenge", "description": "test1", "price": 2020, "tax": 2021}

# post request to api
res = requests.post(url, data=json.dumps(data))

# print response
print(res.text)

# ---
# api /bank_types/
# ---

bank_list = ["카카오뱅크", "케이뱅크", "토스"]

for bank in bank_list:
    url = f"http://localhost:8000/bank-types/{bank}"
    print(url)
    res = requests.get(url)
    print(res.text)
