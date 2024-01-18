#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    longitude= resp["iss_position"]["longitude"]
    latitude= resp["iss_position"]["latitude"]
    epoch= resp["timestamp"]
    timestamp= datetime.datetime.fromtimestamp(epoch)

    locator_resp= rg.search((latitude, longitude))
    city= locator_resp[0]["name"]
    country= locator_resp[0]["cc"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp= {timestamp}
    Longitude= {longitude}
    Latitude= {latitude}
    City/Country= {city}, {country}
    """)

if __name__ == "__main__":
    main()

