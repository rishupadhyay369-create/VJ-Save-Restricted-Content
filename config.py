# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature
LOGIN_SYSTEM = os.environ.get("LOGIN_SYSTEM", "True").lower() == "true"

if LOGIN_SYSTEM is False:
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
else:
    STRING_SESSION = None

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# API ID
API_ID = int(os.environ.get("API_ID", "30720387"))

# API HASH
API_HASH = os.environ.get(
    "API_HASH",
    "2eeb9d06eb049619e747488846496bfa"
)

# Admin ID
ADMINS = int(os.environ.get("ADMINS", "6690830189"))

# Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003659159660"))

# MongoDB
DB_URI = os.environ.get(
    "DB_URI",
    "mongodb+srv://rishupadhyay369_db_user:Kt4Q2zYLs3UrAXUh@cluster0.dftynvv.mongodb.net/?appName=Cluster0"
)

# Flood wait
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10"))

# Error message
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
