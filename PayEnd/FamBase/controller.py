from pymongo import DESCENDING, errors

from config import PAGINATION_LIMIT
from database import fam_collection


def add_video(video_fam):
    try:
        fam_collection.insert_one(video_fam)
    except errors.DuplicateKeyError:
        # entry already exists
        print("[FamBase] Warning: duplicate key")
        pass


def add_videos(videos):
    try:
        fam_collection.insert_many(videos)
    except errors.BulkWriteError:
        # one or more entries already exist
        print("[FamBase] Warning: Write failed, continuing")
        pass


def search_videos(query, skip_count):
    return (
        fam_collection.find({"$text": {"$search": query}})
        .sort("published_at", DESCENDING)
        .skip(skip_count)
        .limit(PAGINATION_LIMIT)
    )
