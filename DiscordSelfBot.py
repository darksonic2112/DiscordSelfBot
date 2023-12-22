import requests
import time
import os
from threading import Thread
from dotenv import load_dotenv

load_dotenv()
DISCORD_AUTHORIZATION_TOKEN = os.getenv('DISCORD_AUTHORIZATION_TOKEN')  # Never give this away, reset password to change
SERVER_IP = os.getenv('SERVER_IP')  # Change server through channel link

working = {
    'content': "!rp work"
}

header = {
    'authorization': DISCORD_AUTHORIZATION_TOKEN
}
