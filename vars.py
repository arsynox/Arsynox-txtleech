#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27404976"))
API_HASH = environ.get("API_HASH", "b9a6f7abf66013a54ec73319806adbe7")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6822491887"))
CREDIT = "࿏𝔸𝕣𝕤𝕪𝕟𝕠𝕩ッ"
AUTH_USER = os.environ.get('AUTH_USERS', '6822491887').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
