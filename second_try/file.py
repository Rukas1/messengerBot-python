import requests
import json
import sys
import random
import string

authAPI = "5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6"
urlCheckServer = "https://waifu.p.rapidapi.com/v1/server/status"
urlSendMessage = "https://waifu.p.rapidapi.com/v1/waifu"


def main():
    if checkServer():
        print("The server is OK\n")
    else:
        print("The server is not OK, try again")
        sys.exit()

    alnum = string.ascii_letters + string.digits

    user_id = ''.join(random.choice(alnum) for i in range(64)) 
    name = input("Your name ? ").lower()
    situation = input("What is the situation ? ")

    while True:
        
        message = input(f"\n{name.title()}: ")
        if message.lower() == "x":
            break
        
        print(sendMessage(message=message,
                    user_id=user_id,
                    name=name,
                    situation=situation)
)        

def cleanString(msg):

    occ = msg.count("&#39;")

    for _ in range(occ):
        out = msg.replace("&#39;", "'")

    if occ > 0:
        return out
    else:
        return msg


def sendMessage(message: str, user_id: str, name: str, situation: str):

    payload = {
        "user_id": user_id,
        "message": message,
        "from_name": name,
        "to_name": "Ichinose",
        "situation": situation,
        "translate_from": "fr",
        "translate_to": "fr"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "waifu.p.rapidapi.com",
        "X-RapidAPI-Key": authAPI
    }

    response = requests.request("POST", urlSendMessage, json=payload, headers=headers)
    text = json.loads(response.text)

    msg = cleanString(text["response"])

    return "\n" + payload["to_name"] + ": " + msg


def checkServer():

    headers = {
        "X-RapidAPI-Host": "waifu.p.rapidapi.com",
        "X-RapidAPI-Key": authAPI
    }

    response = requests.request("GET", urlCheckServer, headers=headers)
    text = json.loads(response.text)
    if text.get("status") == "ok":
        return True
    else:
        return False


if __name__ == "__main__":
    main()