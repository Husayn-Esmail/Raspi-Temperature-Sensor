#!/bin/bash
source venv/bin/activate
export FLASK_ENV="development"
export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT='8083'
python3 -m flask run