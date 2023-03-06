from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", "")
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", ""))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", ""))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", ""))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", "3"))
MONGO_URL = environ.get("MONGO_URL", "")
ARQ_API_URL = environ.get("ARQ_API_URL", "https://thearq.tech")
ARQ_API_KEY = environ.get("ARQ_API_KEY", "")
RSS_DELAY = int(environ.get("RSS_DELAY", 300))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/Suramusic/NezukoBotManagement.git"
)
