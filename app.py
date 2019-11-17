import requests
import json
from ast import  literal_eval
from flask import Flask, render_template, request

app = Flask(__name__)

SUCCESS_RESPONSE = ['00']
FAILURE_RESPONSE = ['01']

@app.route("/test")
def index():
    return "Good request"

@app.route("/payment/bank", methods=["POST"])
def hello():
    data = request.get_data()
    data = data.decode('utf-8')

    data = literal_eval(data)
    payload = data[0]
    url = 'http://localhost:8069/payment/remita/bank'

    # Send a post request to Odoo
    r = requests.post(url, data=payload)
    return_data = r.json()
    if return_data.get('tnx_state') in SUCCESS_RESPONSE:
        return "OK"
    return "not ok"
