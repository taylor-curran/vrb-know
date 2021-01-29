# AIRDNA EndPoints
import os
from dotenv import load_dotenv
import requests
import numpy
import json
import pandas as pd
import sys
import psycopg2
import os
from dotenv import load_dotenv
import os

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

def market_search_call(city: str, state: str = '') -> [int, str]:
    
    endpoint = "market/search"
    url = HOST + endpoint

    params = {
        "access_token": AIRDNA_TOKEN,
        "term": str(city) + ', ' + str(state) + 'USA'
    }

    try:
        response = requests.request("GET", url,  
                                    params=params).response()
    except:
        return "Error Processing Request"

    # city_id
    try:
        city_id = response['items'][0]['city']['id']
        name = response['items'][0]['name']
        return city_id, name
    except:
        return f"Error Finding {city}, {state}."
    

    



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


def market_summary_call(market_id):
    
    endpoint = "market/summary"
    url = HOST + endpoint

    params = {
    "access_token": AIRDNA_TOKEN,
    "city_id": market_id
    }

    try:
        response = requests.request("GET", url,  
                                    params=params).json()
    except:
        return "Error Processing Request"

    # city_id
    
    dfd = {} 
    # Market - Summary - Request_Info
    # COLS: city_id
    city_id = response['request_info']['city_id']
    dfd.update({'city_id': city_id})
    # Market - Summary - Data - Calendar Months
    # adr -> Average Daily Rate
    # COLS: occ, adr, revenue
    ent_stats = response['data']['calendar_months']['room_type']['entire_place']
    ent_stats
    ent_stats_dict = {
        'occ': ent_stats['occ']['50th_percentile'],
        'adr': ent_stats['adr']['50th_percentile'],
        'revenue': ent_stats['revenue']['50th_percentile']
                    }
    dfd.update(ent_stats_dict)
    # Market - Summary - Data - Host_Info - Hosts
    # COLS: total_hosts, superhosts, multi_unit_hosts, single_unit_hosts
    host_counts = response['data']['host_info']['hosts']
    dfd.update(host_counts)
    # Market - Summary - Data - Host_Info - Hosts
    # COLS: total_hosts, superhosts, multi_unit_hosts, single_unit_hosts
    host_counts = response['data']['host_info']['hosts']
    dfd.update(host_counts)
    # Market - Summary - Data - Rental_Activity - Available
    # COLS:
    # TODO: ?- What is '10-12', '1-3', and such? -?
    # They are either length-of-stay or they are n-people
    available = response['data']['rental_activity']['available']
    available_dict = {
        'available_10_12': available['10-12'],
        'available_1_3': available['1-3'],
        'available_7_9': available['7-9'],
        'available_4_6': available['4-6']
                    }

    dfd.update(available_dict)
    # Market - Summary - Data - Rental_Activity - Booked
    # COLS:
    # TODO: ?- What is '10-12', '1-3', and such? -?
    # They are either length-of-stay or they are n-people
    booked = response['data']['rental_activity']['booked']
    booked_dict = {
        'booked_10_12': booked['10-12'],
        'booked_1_3': booked['1-3'],
        'booked_7_9': booked['7-9'],
        'booked_4_6': booked['4-6']
                    }
    dfd.update(booked_dict)
    # Market - Summary - Data - Rental Counts - Counts - Private_Room
    # COLS: n_private_rooms
    n_private_rooms = response['data']['rental_counts']['counts']['private_room']['all']
    dfd.update({'n_private_rooms': n_private_rooms})
    # Market - Summary - Data - Rental Counts - Counts - Entire Place by n_rooms
    # COLS: rms0_rntl_cnt, rms1_rntl_cnt, rms3_rntl_cnt
    #       rms4_rntl_cnt, rms5plus_rntl_cnt, n_entire_place
    count_by_n_rooms = response['data']['rental_counts']['counts']['entire_place']
    count_by_n_rooms_dict = {
        'n_rooms_0': count_by_n_rooms['0'],
        'n_rooms_1': count_by_n_rooms['1'],
        'n_rooms_2': count_by_n_rooms['2'],
        'n_rooms_3': count_by_n_rooms['3'],
        'n_rooms_4': count_by_n_rooms['4'],
        'n_rooms_5plus': count_by_n_rooms['5'],
        'tot_count_entire_place': count_by_n_rooms['all'],
                            }
    dfd.update(count_by_n_rooms_dict)
    # Market - Summary - Data - Rental Counts - Counts - Entire Place by n_rooms
    # COLS: rms0_rntl_cnt, rms1_rntl_cnt, rms3_rntl_cnt
    #       rms4_rntl_cnt, rms5plus_rntl_cnt, n_entire_place
    count_by_n_rooms = response['data']['rental_counts']['counts']['entire_place']
    count_by_n_rooms_dict = {
        'n_rooms_0': count_by_n_rooms['0'],
        'n_rooms_1': count_by_n_rooms['1'],
        'n_rooms_2': count_by_n_rooms['2'],
        'n_rooms_3': count_by_n_rooms['3'],
        'n_rooms_4': count_by_n_rooms['4'],
        'n_rooms_5plus': count_by_n_rooms['5'],
        'tot_count_entire_place': count_by_n_rooms['all'],
                            }

    dfd.update(count_by_n_rooms_dict)
    row = pd.Series(dfd)
    
    # Load DB Credentials
    load_dotenv()
    RDS_HOSTNAME = os.getenv("RDS_HOSTNAME")
    RDS_PORT = os.getenv("RDS_PORT")
    RDS_DB_NAME = os.getenv("RDS_DB_NAME")
    RDS_USERNAME = os.getenv("RDS_USERNAME")
    RDS_PASSWORD = os.getenv("RDS_PASSWORD")

    conn = psycopg2.connect(
        dbname=RDS_DB_NAME,
        user=RDS_USERNAME,
        password=RDS_PASSWORD,
        host=RDS_HOSTNAME,
        port=RDS_PORT
        )

    curs = conn.cursor()

    VALUES = str(tuple(row.values))
    Q_INSERT_COL_NAMES = """
    INSERT INTO market_summary (
    city_id, occ, adr, revenue,
    total_hosts, superhosts, 
    multi_unit_hosts, single_unit_hosts,
    multi_host_properties, total_properties,
    single_host_properties, available_10_12,
    available_1_3, available_7_9, available_4_6,
    booked_10_12, booked_1_3, booked_7_9, 
    booked_4_6, n_private_rooms, n_rooms_0,
    n_rooms_1, n_rooms_2, n_rooms_3, n_rooms_4,
    n_rooms_5plus, tot_count_entire_place,
    avg_n_rooms, avg_accommodates
    )
    VALUES """
    Q_INSERT_FINAL = Q_INSERT_COL_NAMES + VALUES + ";"

    curs.execute(Q_INSERT_FINAL)
    conn.commit()
    
    curs.close()
    conn.close()
    
    print('DB Populated with Row!')

    
