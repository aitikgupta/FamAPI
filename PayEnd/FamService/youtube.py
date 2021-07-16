import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import CHUNK_TIME, PREDEFINED_QUERY, LOCAL_API_LIMIT
from utils import get_API_key, generate_new_API_key
from FamBase.schema import FamVideo


class YoutubePoller:
    def __init__(self, service_name, api_version):
        self.service_name = service_name
        self.api_version = api_version

        self.api_key = get_API_key()
        # initialize poller's key hits
        self.api_key_hit = 0
        # take interval 'CHUNK_TIME' seconds before now
        self.published_after = datetime.datetime.strftime(
            datetime.datetime.now() - datetime.timedelta(seconds=CHUNK_TIME),
            "%Y-%m-%dT%H:%M:%SZ",
        )

        self._youtube_object = self.generate_youtube_object()

    def generate_youtube_object(self):
        return build(
            self.service_name, self.api_version, developerKey=self.api_key
        )

    def update_API_key(self):
        self.api_key = generate_new_API_key()
        self.api_key_hit = 0
        print("[FamService] Updating API key..", self.api_key)

    def fetch_latest_videos(self, page_token=None):
        try:
            response = (
                self._youtube_object.search()
                .list(
                    q=PREDEFINED_QUERY,
                    part="id,snippet",
                    order="date",
                    publishedAfter=self.published_after,
                    type="video",
                    pageToken=page_token,
                )
                .execute()
            )

            # increment API key hits
            self.api_key_hit += 1
            if self.api_key_hit > LOCAL_API_LIMIT:
                raise OverflowError("API Key limit exceeded.")

        except Exception as e:
            print("[FamService] Warning:", e)
            if (
                isinstance(e, HttpError) and "exceeded" in e._get_reason()
                or isinstance(e, OverflowError)
            ):
                # either YouTube API limit or local API limit exceeded
                self.update_API_key()
                # regenerate youtube object
                self._youtube_object = self.generate_youtube_object()
            else:
                print("[FamService] Uncaught exception:", e)
            return [], None

        results = []
        for item in response.get("items", []):
            # only iterate videos
            if item["id"]["kind"] == "youtube#video":
                formatted_date = datetime.datetime.strptime(
                    item["snippet"]["publishedAt"],
                    "%Y-%m-%dT%H:%M:%SZ",
                ).strftime("%Y-%m-%d %H:%M:%S")

                results.append(
                    FamVideo(
                        item["id"]["videoId"],
                        item["snippet"]["title"],
                        item["snippet"]["description"],
                        formatted_date,
                        item["snippet"]["thumbnails"]["default"]["url"],
                        item["snippet"]["thumbnails"]["high"]["url"],
                    )
                )

        next_page_token = response.get("nextPageToken", None)
        return results, next_page_token
