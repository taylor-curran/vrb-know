import psycopg2
import os
from dotenv import load_dotenv
import os


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


conn.close()


# Queries!
# CREATE TABLE IF NOT EXISTS 
# market_summary (
# 	city_id INT PRIMARY KEY, 
# 	occ REAL,
# 	adr NUMERIC(13, 2),
# 	revenue NUMERIC(13, 2),
# 	total_hosts INT,
# 	superhosts INT,
# 	multi_unit_hosts INT,
# 	single_unit_hosts INT,
# 	multi_host_properties INT,
# 	total_properties INT,
# 	single_host_properties INT,
# 	available_10_12 INT,
# 	available_1_3 INT,
# 	available_7_9 INT,
# 	available_4_6 INT,
# 	booked_10_12 INT,               
# 	booked_1_3 INT,
# 	booked_7_9 INT,                
# 	booked_4_6 INT,                 
# 	n_private_rooms INT,           
# 	n_rooms_0 INT,               
# 	n_rooms_1 INT,             
# 	n_rooms_2 INT,              
# 	n_rooms_3 INT,                 
# 	n_rooms_4 INT,            
# 	n_rooms_5plus INT,           
# 	tot_count_entire_place INT,     
# 	avg_n_rooms NUMERIC (5, 3),                   
# 	avg_accommodates NUMERIC (5, 3)         
# )

# Insert
# VALUES = str(tuple(gat_df_row.values))
# Q_INSERT_COL_NAMES = """
# INSERT INTO market_summary (
# city_id, occ, adr, revenue,
# total_hosts, superhosts, 
# multi_unit_hosts, single_unit_hosts,
# multi_host_properties, total_properties,
# single_host_properties, available_10_12,
# available_1_3, available_7_9, available_4_6,
# booked_10_12, booked_1_3, booked_7_9, 
# booked_4_6, n_private_rooms, n_rooms_0,
# n_rooms_1, n_rooms_2, n_rooms_3, n_rooms_4,
# n_rooms_5plus, tot_count_entire_place,
# avg_n_rooms, avg_accommodates
# )
# VALUES """
# Q_INSERT_FINAL = Q_INSERT_COL_NAMES + VALUES + ";"

# CREATE TABLE IF NOT EXISTS 
# comp_props (
# 	entry_id SERIAL PRIMARY KEY,
# 	instant_book BOOLEAN,
# 	rating_overall NUMERIC(5, 3),
# 	bathrooms NUMERIC(5, 2),
# 	revenue NUMERIC(13, 2),
# 	listing_url TEXT,
# 	longitude NUMERIC(10, 6),
# 	extra_person_charge NUMERIC(5,2),
# 	property_type VARCHAR(50),
# 	listed_dt DATE,
# 	price_monthly NUMERIC(13, 2),
# 	reviews SMALLINT,
# 	check_in TEXT,
# 	airbnb_host_id INT,
# 	business_ready BOOLEAN,
# 	price_weekly NUMERIC(13, 2),
# 	occ REAL,
# 	days_r_ltm SMALLINT,
# 	scraped_dt DATE,
# 	img_prop TEXT [],
# 	amenities TEXT [],
# 	superhost BOOLEAN,
# 	price_nightly NUMERIC(13, 2),
# 	num_res_ltm SMALLINT,
# 	img_count SMALLINT,
# 	security_deposit NUMERIC(13, 2),
# 	airbnb_property_id INT,
# 	bedrooms NUMERIC(5, 2),
# 	days_a_ltm SMALLINT,
# 	latitude NUMERIC(10, 6),
# 	minimum_stay SMALLINT,
# 	adr NUMERIC(13, 2),
# 	check_out TEXT,
# 	response_time NUMERIC(13, 2),
# 	days_b_lmt INT,
# 	last_calendar_update DATE,
# 	title TEXT,
# 	loc JSON,
# 	accommodates SMALLINT,
# 	room_type VARCHAR(100),
# 	img_cover TEXT,
# 	cleaning_fee NUMERIC(13, 2),
# 	response_rate NUMERIC(5, 2),
# 	cancellation TEXT,
# 	area_id TEXT,
# 	zip_code SMALLINT,
# 	city_state VARCHAR(100)
# );