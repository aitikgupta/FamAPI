import os

# Because GenZ loves video games!
PREDEFINED_QUERY = "fortnite"

# poll interval (in seconds)
SLEEP_TIME = 10
# YouTube API keys
# https://developers.google.com/youtube/v3/getting-started
GLOBAL_API_KEYS = os.getenv("GOOGLE_API_KEYS").split(",")

# Flask-specific vars
HOST_URL = "0.0.0.0"
HOST_PORT = "8080"

# MongoDB-specific vars
MONGODB_URI = "mongodb://localhost:27017"
