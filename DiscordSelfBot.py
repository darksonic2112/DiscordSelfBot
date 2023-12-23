import requests
import os
from threading import Thread
from dotenv import load_dotenv

load_dotenv()

DISCORD_AUTHORIZATION_TOKEN = os.getenv('DISCORD_AUTHORIZATION_TOKEN')
SERVER_IP = os.getenv('SERVER_IP')

working = {
    'content': "Hallo"
}

header = {
    'authorization': DISCORD_AUTHORIZATION_TOKEN
}


def work():
    try:
        response = requests.post(SERVER_IP, data=working, headers=header)
        if response.status_code == 200:
            print("Message sent!")
        else:
            print("Error sending Message:", response.status_code)
    except Exception as error:
        print("Error trying to execute Code:", str(error))


thread_1 = Thread(target=work)

try:
    thread_1.start()
except Exception as e:
    print("Error starting Threads:", str(e))
