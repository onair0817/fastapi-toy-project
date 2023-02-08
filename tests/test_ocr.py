import requests

url = "http://localhost:8001/image/process"

file = {"file": ("IMG_4955.jpg", open("../images/IMG_4955.jpg", "rb"), "image/jpeg")}

response = requests.post(url, files=file)

print(response.json())
