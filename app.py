import os

from flask import Flask
from marinetrafficapi import MarineTrafficApi
from twilio.twiml.messaging_response import MessagingResponse

api_key = os.environ['MARINE_TRAFFIC_API_KEY']
api = MarineTrafficApi(api_key=api_key)

app = Flask(__name__)

@app.route('/sms', methods=["GET","POST"])
def boat():
    resp = MessagingResponse()

    vessel = api.single_vessel_positions(time_span=240, mmsi=353136000)
    vessel = vessel.models[0]

    latitude = vessel.latitude.value
    longitude = vessel.longitude.value
    speed = vessel.speed.value

    stuck_latitude = 30.01765
    stuck_longitude = 32.5802
    stuck_speed = 0

    if speed != stuck_speed and latitude != stuck_latitude and longitude != stuck_longitude:
        resp.message("It's moving!")
    else:
        resp.message("Still stuck 😔")

    return str(resp)