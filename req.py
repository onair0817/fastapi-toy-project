import requests
import json


# ---
# 1. api /items/
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
# 2. api /bank_types/
# ---

bank_list = ["카카오뱅크", "케이뱅크", "토스"]
# get request to api
for bank in bank_list:
    url = f"http://localhost:8000/bank-types/{bank}"
    res = requests.get(url)
    print(res.text)

# ---
# 3. api /info/
# ---

# request url
url = "http://localhost:8000/info/"
# get request to api
res = requests.get(url)
# print response
print(res.text)

# ---
# 4. api /tv_show_name/
# ---

# request url
tv_show = "noltoe"
url = f"http://localhost:8000/tv-shows/{tv_show}"
# get request to api
res = requests.get(url)
# print response
print(res.text)

# ---

url = "http://127.0.0.1:8000/tv-shows/HIMYM/characters?character=Ted"
# get request to api
res = requests.get(url)
# print response
print(res.text)

# ---
# 5. api /movies/
# ---

# error case
# url = "http://127.0.0.1:8000/movies/comet"
# normal case
url = "http://127.0.0.1:8000/movies/comet?character=Kimberley"
# get request to api
res = requests.get(url)
# print response
print(res.text)

# ---
# 6. api /characters/
# ---

url = "http://127.0.0.1:8000/characters/?q=ted&q=robin&q=barney"
# get request to api
res = requests.get(url)
# print response
print(res.text)

url = "http://127.0.0.1:8000/characters/"
# get request to api
res = requests.get(url)
# print response
print(res.text)

# ---
# 7. api /numbers/
# ---

# url = "http://127.0.0.1:8000/numbers/50"
# # get request to api
# res = requests.get(url)
# # print response
# print(res.text)

url = "http://127.0.0.1:8000/numbers/200"
# get request to api
res = requests.get(url)
# print response
print(res.text)


# ---
# request body
# ---

# request url
url = "http://localhost:8000/dramas/1?q=ok"
# data
data = {
    "name": "How I Met Your Mother",
    "description": "제목대로 주인공 테드 모스비가 2030년, 자식들에게 자기 아내를 어떻게 만났는지 이야기해 주는 액자형 구성을 취하고 있다. \
        기본적으로 매 화의 내용은 보통 시청자 입장에서 어제 일어났을것 같은 이야기들이다",
    "score": 9.9,
    "channel": "CBS",
}
# put request to api
res = requests.put(url, data=json.dumps(data))
# print response
print(res.text)
