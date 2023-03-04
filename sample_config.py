from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", "5948498614:AAGldqJ9CgnMzfbEX5Tp2WSXYUkXG5qJSE4")
API_ID = int(environ.get("API_ID", "28420275"))
API_HASH = environ.get("API_HASH", "ee41d63cbcf69ab63a3514642785a349")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "1471469091").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", "-1001849137304"))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", "-1001849137304"))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", "-1001849137304"))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", "3"))
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://Tamilbots:tamilbots@cluster0.aa2e1nd.mongodb.net/?retryWrites=true&w=majority")
ARQ_API_URL = environ.get("ARQ_API_URL", "https://thearq.tech")
ARQ_API_KEY = environ.get("ARQ_API_KEY", "GNNJTA-QHWNIV-YLMCTS-YPBLST-ARQ")
RSS_DELAY = int(environ.get("RSS_DELAY", 300))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/rozari0/NezukoBot.git"
)
