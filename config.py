# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# -------------------- KOYEB HEALTH SERVER --------------------

def run_server():
    class HealthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is alive")

    port = int(os.environ.get("PORT", 8000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# -------------------- BOT CONFIG --------------------

# Login system
LOGIN_SYSTEM = True

if not LOGIN_SYSTEM:
    STRING_SESSION = ""
else:
    STRING_SESSION = None

# Bot token (YOU MUST FILL THIS)
BOT_TOKEN = "PASTE_YOUR_REAL_BOT_TOKEN_HERE"

# API credentials (FILLED)
API_ID = 30720387
API_HASH = "2eeb9d06eb049619e747488846496bfa"

# Admin ID (FILLED AS LIST)
ADMINS = [6690830189]

# Channel ID (FILLED)
CHANNEL_ID = -1003659159660

# MongoDB URI (FILLED)
DB_URI = (
    "mongodb+srv://rishupadhyay369_db_user:"
    "Kt4Q2zYLs3UrAXUh@cluster0.dftynvv.mongodb.net/"
    "?appName=Cluster0"
)

# Flood wait time
WAITING_TIME = 10

# Error message toggle
ERROR_MESSAGE = True
