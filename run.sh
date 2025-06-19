#!/bin/bash
cd src/
export FLASK_APP=restApi.py
# export FLASK_DEBUG=1
flask run -h localhost -p 5001