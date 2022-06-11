from fbchat import Client
from fbchat.models import *
import json

import logging
logging.basicConfig(level=logging.DEBUG)

client = Client("ichinoseai731@gmail.com", "here_my_password")

session = client.getSession()

with open("session.json", "w") as f:
    json.dump(session, f, indent=4)
