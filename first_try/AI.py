from fbchat import Client
from fbchat.models import *

client = Client('ichinoseai731@gmail.com', 'here_my_password')

if not client.isLoggedIn():
    client.login('ichinoseai731@gmail.com', 'here_my_password')

client.reactToMessage

client.logout()