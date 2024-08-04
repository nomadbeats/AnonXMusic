import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("22534953"))
API_HASH = getenv("8190891e894562a97d754c4984c3bc89")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7402302847:AAG780RZqPkM67bIPDQV7cNyspxClUtRW1I")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://mb1513647:mb1513647@cluster0.mlety3g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-4267428358", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6346043548))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("nomadbeeats")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-a288ae21-3ba3-4162-a5e3-46a7e63108b5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/nomadry")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nomadrysupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/dea5469a502555cda41c4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c2ac5608593e135220978.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/0c4e08e0b437e30b16dca.jpg"
STATS_IMG_URL = "https://telegra.ph/file/22fce1617bee3d5048da1.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/1e497c755e1eab7636c8b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/6c41c7c06220cff69d19c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/439a958c525e488c50d36.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/6620e5b70d438d123fc7a.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/439a958c525e488c50d36.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/6c41c7c06220cff69d19c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/57df405c866f200a1c50f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/8dfd2e945f95775280ad3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
