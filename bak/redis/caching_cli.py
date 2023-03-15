import requests
import random
import time


while True:
    value = random.randint(1, 50)
    response = requests.get(f"http://0.0.0.0:8000/?value={value}")
    print(f"Response: {response.json()}")
    time.sleep(2)
