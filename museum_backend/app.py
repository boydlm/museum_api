from flask import Flask, request
from flask_cors import CORS
from service.exhibits_service import getExhibitsByCity
import json

api = Flask(__name__)
CORS(api)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Leah",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@api.route('/exhibits')
def get_exhibits():
    args = request.args
    city = args.get("city")
    output = getExhibitsByCity(city)
    return json.dumps([json.dumps([item.__dict__ for item in output])])


if __name__ == "__main__":
    api.run(port=8000, debug=True)