import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7619364034:AAHsuBrDWONcUzCPv8iMBehfh7GeojenSWk")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 25194442))
    API_HASH = os.environ.get("API_HASH", "9e93d41112872cc3bd58f4e29fd82c0a")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7651377821").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Update channel for force subscription
    UPDATE_CHANNEL = "vkprojects"
    
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://suproboiragi2:t4GwmmrWCkUcX3Ui@cluster0.nn4hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
