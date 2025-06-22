""" Module Name: 
    Function for all dbs including REDIS connections ( Redis, MySQL), and use by API calls.

    Created By: Haziq
    Created: 18/06/2025
    Framework: Python 3.10

    Last Edited: 180625
     Reason Edited: create function connection
"""

import os
import sys

# source : library
# usage : setup path
import os.path
from os import path

# source : library
# usage : connect to redis
import redis

# source : library
# uasge : MySQL cennection module
import mysql.connector

# source : library
# usage : to get load env
from dotenv import load_dotenv

# source : library
# usage : S3 connection module
import boto3

# source : self
# usage : to get database connection and redis connection
from funcFile import funcDecrypt

# Load environment variables from the .env file
load_dotenv(override=True)

# adding env folder to the system path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
path = os.getcwd()
parPath = os.path.dirname(path)
sys.path.insert(0,path)

# get value from env
strDbHost = os.getenv('DB_HOST')
strDbUser = os.getenv('DB_USER')
strDbPassword = os.getenv('DB_PASSWORD')
# strDbPassword = funcDecrypt(strDbPassword)
strDbDatabase = os.getenv('DB_DATABASE')
# strRedisHost = os.getenv('REDIS_HOST')
# intRedisPort = os.getenv('REDIS_PORT')
# bLocalhostTest = os.getenv('REDIS_BLOCALHOST')
# strAwsRegionName = os.getenv('AWS_REGION_NAME')
# strAwsAccessKey = os.getenv('AWS_ACCESS_KEY')
# strAwsAccessKey = funcDecrypt(strAwsAccessKey)
# strAwsSecretKey = os.getenv('AWS_SECRET_KEY')

#connection to MySQL
def funcConMySQL ():
    connection = mysql.connector.connect(host=str(strDbHost),
                                        database=str(strDbDatabase),
                                        user=str(strDbUser),
                                        password=str(strDbPassword))
    return connection
    
# connection to Redis
# def funcConRedisDb (intDb):
#     if bLocalhostTest == 'False':
#         r = redis.Redis(host=str(strRedisHost),
#                         port=str(intRedisPort),
#                         db=intDb)
        
#         return r

#     elif bLocalhostTest == 'True':
#         r = redis.Redis(host='localhost',
#                         port='6380',
#                         db=intDb)

#         return r

# def funcConS3 ():
#     # connect to S3
#     s3_client = boto3.client('s3',
#                     region_name = str(strAwsRegionName),
#                     aws_access_key_id = str(strAwsAccessKey),
#                     aws_secret_access_key = str(strAwsSecretKey))
#     return s3_client