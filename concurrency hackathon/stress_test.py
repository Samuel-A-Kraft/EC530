import requests
import time
import random

countries = ["France", "Germany", "Brazil", "India", "USA", "Italy", "Spain", "Canada", "Japan", "Australia"]

def send_request(country):
    payload = {"country": country}
    try:
        r = requests.post("http://localhost:8000/covid", json=payload)
        print(f"{country}: {r.status_code}")
    except Exception as e:
        print(f"Error sending {country}: {e}")

for _ in range(100):
    send_request(random.choice(countries))
    time.sleep(0.05)