from flask import Flask
from flask_cors import CORS
from flask import jsonify
from sherlock import sherlock
import os
import json

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


@app.route("/alive")
def is_alive():
    return "Is Alive"


@app.route("/search/<string:username>", methods=["GET"])
def search_user(username):
    data_file_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data.json')
    raw = open(data_file_path, "r", encoding="utf-8")
    site_data_all = json.load(raw)

    sherlock(username, site_data_all)

    return "Search done"

if __name__ == '__main__':
    app.run(host="localhost", port=8000)
    # app.run(host="0.0.0.0", port=80)