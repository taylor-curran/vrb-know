# AIRDNA EndPoints
import os
from dotenv import load_dotenv
import requests
import numpy
import json
import pandas as pd

# Load API Key
load_dotenv()
AIRDNA_TOKEN = os.getenv("AIRDNA_TOKEN")

# Same for All API Calls
HEADERS = {"access_token": AIRDNA_TOKEN}
HOST = "https://api.airdna.co/client/v1/"

# MARKET SEARCH
# {{HOST}}/client/{{VERSION_CLIENT}}/market/search?
# access_token={{CLIENT_TOKEN}}&term='https://www.airbnb.com/rooms/15807599'
# Country
# City
# Neighbourhood
# State (US Only)
# Metropolitan Statistical Area (US Only)
# Zip Code (US Only)

def market_search_call(city_name: str) -> int:
    
    endpoint = "market/search"
    url = HOST + endpoint

    params = {
        "access_token": AIRDNA_TOKEN,
        "term": str(city_name)
    }


    response = requests.request("GET", url,  
                                params=params).json()

    # city_id
    city_id = response['items'][0]['city']['id']
    
    return city_id
    



# MARKET SUMMARY
# {{HOST}}/client/{{VERSION}}/market/summary?
# access_token={{CLIENT_TOKEN}}&city_id=59380&region_id=12341&currency=usd

# PARAMS
# city_id
# region_id
# currency


def market_summary_call():
    # TODO
    pass
