import requests
import random
import time

URL = "http://localhost:5000/api/data"

while True:
    data = {
        "device_id": "sensor_1",
        "value": round(random.uniform(20, 30), 2)
    }
    r = requests.post(URL, json=data)
    print(f"Sent: {data}, Response: {r.json()}")
    time.sleep(5)
