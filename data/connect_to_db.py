import psycopg2
import os
from dotenv import load_dotenv

import os

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

# Load DB Credentials
load_dotenv()
RDS_HOSTNAME = os.getenv("RDS_HOSTNAME")
RDS_PORT = os.getenv("RDS_PORT")
RDS_DB_NAME = os.getenv("RDS_DB_NAME") # Might Be Wrong
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