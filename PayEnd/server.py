import requests
import threading
import time

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from config import (
    HOST_URL,
    HOST_PORT,
    SLEEP_TIME,
    BULK_SAVE,
    YOUTUBE_SERVICE_NAME,
    YOUTUBE_API_VERSION,
)
from utils import generate_new_API_key

from FamService.youtube import YoutubePoller

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

poller = YoutubePoller(YOUTUBE_SERVICE_NAME, YOUTUBE_API_VERSION)
# initial pageToken
page_token = None


@app.before_first_request
def activate_job():
    def poll_youtube_service():
        while True:
            print("[FamServer] Fetching new videos!")
            global page_token
            results, next_token = poller.fetch_latest_videos(
                page_token, save_each=not BULK_SAVE
            )
            if BULK_SAVE:
                poller.save_videos(results)

            # next_token is None when API limit exceeds
            page_token = next_token if next_token else page_token
            time.sleep(SLEEP_TIME)

    thread = threading.Thread(target=poll_youtube_service)
    thread.start()


@app.route("/", methods=["GET"])
@cross_origin()
def root():
    message = "New key: {}".format(generate_new_API_key())
    print(message, flush=True)
    return jsonify({"message": message})


def start_runner():
    def start_loop():
        # poll backend to trigger event loop
        SHORT_SLEEP = 2
        not_started = True
        while not_started:
            print("In start loop", flush=True)
            try:
                r = requests.get("http://" + HOST_URL + ":" + HOST_PORT)
                if r.status_code == 200:
                    print("Server started, quiting start_loop", flush=True)
                    not_started = False
                print(r.status_code, flush=True)
            except Exception:
                print("Server not yet started", flush=True)
            time.sleep(SHORT_SLEEP)

    print("Started runner", flush=True)
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == "__main__":
    start_runner()
    app.run(host=HOST_URL, port=HOST_PORT, debug=True)
