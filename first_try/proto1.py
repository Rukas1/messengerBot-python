import requests
import json

API = "https://waifu.p.rapidapi.com/v1/waifu"

METHODE = "POST"

identifiant = input("Your identifiant ? ")

HEADERS = {
	"content-type": "application/json",
	"X-RapidAPI-Host": "waifu.p.rapidapi.com",
	"X-RapidAPI-Key": "5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6"
}

# algorithme de nettoyage de chaine de caractère
def clean_string(msg):
    occ = msg.count("&")
    if occ == 0:
        return msg
    while occ != 0:
        preout = "".join([c if c != "&" else "'" for c in msg])
        occ -= 1
    indessirables = ['#', '3', '9', ';']
    out = "".join([c for c in preout if c not in indessirables])
    return out

print("\npress x key to exit\n".upper())
while True:
    msg = input("ME: ")
    if msg == "":
        continue
    if msg.lower() == "x":
        break

    PAYLOAD = {
	"user_id": identifiant,
	"message": msg,
	"from_name": "Boy",
	"to_name": "Girl",
	"situation": "Girl loves Boy.",
	"translate_from": "auto",
	"translate_to": "auto"
    }

    response = requests.request(method=METHODE, url=API,
    json=PAYLOAD, headers=HEADERS)

    string = json.loads(response.content) 
    brut = string.get('response')

    chat = clean_string(brut)
    print(f"\nAI: {chat}\n")
