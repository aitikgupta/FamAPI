import requests
import threading
import time

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from utils import generate_new_API_key


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.before_first_request
def activate_job():
    def run_job():
        while True:
            print("Run recurring task")
            time.sleep(3)

    thread = threading.Thread(target=run_job)
    thread.start()


@app.route("/", methods=["GET"])
@cross_origin()
def root():
    message = "New key: {}".format(generate_new_API_key())
    print(message, flush=True)
    return jsonify({"message": message})


def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop', flush=True)
            try:
                r = requests.get('http://0.0.0.0:8080/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop', flush=True)
                    not_started = False
                print(r.status_code, flush=True)
            except Exception:
                print('Server not yet started', flush=True)
            time.sleep(2)

    print('Started runner', flush=True)
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == "__main__":
    start_runner()
    app.run(host="0.0.0.0", port=8080, debug=True)
