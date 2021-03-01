import pandas as pd

states = pd.read_csv('join_tables/state_abbrevs.csv')


def name_to_code(state_name):
    try:
        return states[states['State'] == state_name]['Code'].values[0]
    except:
        print(f"Error Processing {state_name}")

def code_to_name(state_code):
    try:
        return states[states['Code'] == state_code]['State'].values[0]
    except:
        print(f"Error Processing {state_name}")
        

        
# Connecting to AirDNA

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

# Test Connection HERE <- Search Calls are Free
# API CALL - Market Search - Find Gatlinburg Market ID
endpoint = "market/search"
url = HOST + endpoint

params = {
    "access_token": AIRDNA_TOKEN,
    "term": "gatlinburg"
}


response = requests.request("GET", url,  
                            params=params)

# Turn this Into Function

# Market Search

def get_city_id(city_name: str) -> str:
    
    endpoint = "market/search"
    url = HOST + endpoint

    params = {
        "access_token": AIRDNA_TOKEN,
        "term": str(city_name)
    }


    response = requests.request("GET", url,  
                                params=params)

    # city_id
    city_id = response.json()['items'][0]['city']['id']
    
    return city_id