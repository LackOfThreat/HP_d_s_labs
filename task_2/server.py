import os, json, datetime
from flask import Flask
from storage import MongodbService

storage = MongodbService.get_instance()

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, 'resources')

@app.route("/")
def hello_world():
    with open(os.path.join(RESOURCE_DIR, "response.json")) as f:
        data = {
        "datetime": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        }
        storage.save_data(data)
        points = ""
        for data in storage.get_data():
            points += f"{data['datetime']}"
        return "%s - %s" % (json.loads(f.read()).get("response"), points)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8060)