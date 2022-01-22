import os, json, datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, 'resources')

@app.route("/json/rockets", methods=['GET'])
def rockets():
    with open(os.path.join(RESOURCE_DIR, "data.json")) as f:
        data = json.loads(f.read()).get('rockets')
        key = request.args.get('key')
        reply = {}
        for i in range(len(data)):
            first_key = list(data[i])[0]
            id = data[i].get(first_key)
            response = data[i].get(key)
            reply[id] = response
        return jsonify(reply)
        

@app.route("/json/cores", methods=['GET'])
def cores():
    with open(os.path.join(RESOURCE_DIR, "data.json")) as f:
        data = json.loads(f.read()).get('cores')
        key = request.args.get('key')
        reply = {}
        for i in range(len(data)):
            first_key = list(data[i])[0]
            id = data[i].get(first_key)
            response = data[i].get(key)
            reply[id] = response
        return jsonify(reply)

@app.route("/json/launches", methods=['GET'])
def launches():
    with open(os.path.join(RESOURCE_DIR, "data.json")) as f:
        data = json.loads(f.read()).get('launches')
        key = request.args.get('key')
        reply = {}
        for i in range(len(data)):
            first_key = list(data[i])[0]
            id = data[i].get(first_key)
            response = data[i].get(key)
            reply[id] = response
        return jsonify(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)