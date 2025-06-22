#!/bin/bash
cd src/
export FLASK_APP=restApi.py
# export FLASK_DEBUG=1
flask run -h 127.0.0.1 -p 5001