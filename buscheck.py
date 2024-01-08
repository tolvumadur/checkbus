#!/usr/bin/env python3
import requests as r
from pathlib import Path

def get_api_key():
    with open(Path.home() / ".checkbus") as f:
        api_key = f.read().strip()

api_key = "5e1196f98fd74580b45ab289d34f16c8"
api_version = "v2.2"
fmt = "json"
stop_name = "MTD6544"
method = "getdeparturesbystop"
stop_id = "WRTSTOTN:4"
url = f"https://developer.cumtd.com/api/{api_version}/{fmt}/{method}?key={api_key}&stop_id={stop_id}"

# Fetch bus data
resp = r.get(url)

if resp.status_code != 200 or resp.json()["status"]["code"] != 200:
    print(resp.json()["status"])
else:
    found=False
    for departure in resp.json()["departures"]:
        if "Yellow" in departure["route"]["route_long_name"]:
            if not "Hopper" in departure["route"]["route_long_name"]:
                found=True
                if departure["expected_mins"] > 1:
                    print(f"The next {departure['route']['route_long_name']} bus will arrive at ECEB in {departure['expected_mins']} minutes")
                else:
                    print(f"The {departure['route']['route_long_name']} bus is due now at ECEB.")
    if not found:
        print("No Yellow busses expected to arrive at ECEB")

