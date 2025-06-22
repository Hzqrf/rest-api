""" Module Name:
    swiftoAPI : API for swifto application

   Created By: Ikhwan ikhwan@schinkelsgroups.com.my
   Created: 02/02/2025
   Framework: Python 3.10 on Flask, MySQL

   Last Edited: 02/02/2025
    Reason Edited: create API to insert data

"""

# source : library
# usage : setup path
import os
import sys
import os.path
from os import path

# source : library
# usage : read json file
import json

# source : library
# usage : log message to log file
import logging

# source : library
# usage : web application framework
from flask import Flask, jsonify, request, make_response

# source : library
# usage : web application framework
from flask_cors import CORS, cross_origin

# source : library
# usage : to get load env
from dotenv import load_dotenv

# source : self
# usage : to get database connection and redis connection
# from funcFile import funcDict2StrInsert, funcDict2StrUpdate, funcDecrypt

# source : self
# usage : to get database connection and redis connection
from funcConn import funcConMySQL

# source : self
# usage : to get custom error message
# from customErrorMessage import funcErrMessage

# source : library
# usage : to generate uuid
import uuid

# source : library
# usage : S3 connection module
import boto3

# source : library
# usage : to send a request 
import requests

# source : library
# usage : get counter
from collections import Counter, defaultdict

# source : library
# usage : to get current datetime
from datetime import datetime

# # source : library
# # usage : database connecion
# from setup import app, db

# from models import TblItem

# Load environment variables from the .env file
load_dotenv(override=True)

# get current path 
path = os.getcwd()
parPath = os.path.dirname(path)
sys.path.insert(0, path)

# create and configure logger
logFormat = "%(asctime)s:%(levelname)s:%(filename)s - %(message)s"
logging.basicConfig(filename="{}/log/restAPI.log".format(parPath),
                    level=logging.INFO,
                    format=logFormat,
                    )
logger = logging.getLogger

# get value from env
strDbHost = os.getenv('DB_HOST')
strDbUser = os.getenv('DB_USER')
strDbPassword = os.getenv('DB_PASSWORD')
# strDbPassword = funcDecrypt(strDbPassword)
strDbDatabase = os.getenv('DB_DATABASE')
strUserApi = os.getenv('API_USERNAME')
strUserApiPassword = os.getenv('API_PASSWORD')
# strBucketImage = os.getenv('BUCKET_NAME')
strOmdbKey = os.getenv('OMDB_KEY')
strOmdbUrl = os.getenv('OMDB_URL')

# set up flask config
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": {"origin": "*"}})

# api to check health check for port 5001
@app.route('/healthCheck')
@cross_origin()
def funcHealthCheck():

    dictReturn = {
        "message": "Test health check for port 5001"
    }
    return jsonify(dictReturn)

# api to get movie details
@app.route('/getMovieDetails')
@cross_origin()
def funcGetMovieDetails():
    strTitle = request.args.get('t', None)

    # APIDocument = requests.get(strOmdbUrl, auth = (strAuth['username'], strAuth['password']))
    strUrlApi = strOmdbUrl+"/?apikey="+strOmdbKey+"&t="+strTitle
    APIDocument = requests.get(strUrlApi)
    result = APIDocument.json()
    return jsonify(result)

# api to get movie details
@app.route('/getDatabase',  methods=['POST'])
@cross_origin()
def funcGetDatabase():
    # strTitle = request.args.get('t', None)
    # connect to DB
    connection = funcConMySQL()
    print(connection)
    cursor = connection.cursor(buffered=True)
    sqlStatement = "SELECT * FROM haziq_test.meja"
    cursor.execute(sqlStatement)
    tplResult = cursor.fetchall()
    print(tplResult)

    # APIDocument = requests.get(strOmdbUrl, auth = (strAuth['username'], strAuth['password']))
    # strUrlApi = strOmdbUrl+"/?apikey="+strOmdbKey+"&t="+strTitle
    # APIDocument = requests.get(strUrlApi)
    # result = APIDocument.json()
    return jsonify(tplResult)

if __name__ == '__main__':
    # 0.0.0.0 indicate global value for server.  This allow for startup at Windows and Ubuntu servers
    logging.info('env test pass. codeVelvetAPI.py system START.')
    app.run(host="0.0.0.0")