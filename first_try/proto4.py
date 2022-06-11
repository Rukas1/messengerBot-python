from fbchat import Client
import fbchat as fb
import json
import requests

class Bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type,  **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if author_id != self.uid:

            self.thread_type = thread_type
            self.thread_id = thread_id
            self.author = author_id
            self.msg = message_object.text
            self.api()

    def clean_string(self, msg):
        """clean_string method

        Args:
            self(Object): the instance
            msg (String): the message you want to purge

        Returns:
            String: the message with nothing change
            OR
            String: the message without ['#', '3', '9', ';']
                    replace (&) with (') (&#39;)
        """
        occ = msg.count("&#39;")
        if occ == 0:
            return msg
        while occ != 0:
            preout = "".join([c if c != "&" else "'" for c in msg])
            occ -= 1
        indessirables = ['#', '3', '9', ';']
        out = "".join([c for c in preout if c not in indessirables])
        return out

    def api(self):
        API = "https://waifu.p.rapidapi.com/v1/waifu"
        IDENTIFIANT = self.author

        HEADERS = {
	    "content-type": "application/json",
	    "X-RapidAPI-Host": "waifu.p.rapidapi.com",
	    "X-RapidAPI-Key": "5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6"
        }

        PAYLOAD = {
                "user_id": IDENTIFIANT,
                "message": self.msg,
                "from_name": "Boys",
                "to_name": "Ichinose", 
                "situation": "Ichinose protects Lucas (her boyfriend) from the boys.",
                "translate_from": "auto",
                "translate_to": "fr"
                }
        
        
        RESPONSE = requests.request(method="POST", url=API,
        json=PAYLOAD, headers=HEADERS)

        string = json.loads(RESPONSE.content) 
        brut = string.get('response')

        CHAT = self.clean_string(brut)


        self.send(fb.Message(text=CHAT), thread_id=self.thread_id, thread_type=self.thread_type)


client = Bot("0693027473", "reflechie")
client.listen()
