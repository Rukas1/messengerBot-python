import requests
import json

class Api:

    def __init__(self, keyID):
        self.api = "https://waifu.p.rapidapi.com/v1/waifu"
        self.keyID = keyID
        self.host = "waifu.p.rapidapi.com"
        self.appData = "application/json"
        self.create_header()
    
    def __repr__(self):
        return f"Api(api='{self.api}', keyID='{self.keyID}')"

    def __str__(self):
        return f"Api: {self.api} | KeyID: {self.keyID} | Host: {self.host} | AppData: {self.appData}"

    def create_header(self):
        self.headers = {
            "content-type": self.appData,
	        "X-RapidAPI-Host": self.host,
	        "X-RapidAPI-Key": self.keyID
        }

class Service(Api):

    def __init__(self, keyID):
        super().__init__(keyID)
        self.options()

    def options(self):
        
        menu = """Options:
1) Create user
2) Send chat message
>> """

        option = ""
        while option not in ['1', '2']:
            option = input(menu)

        match option:
            case '1':
                self.CreateID()
            case '2':
                self.charge_user()
                self.main()

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

    def charge_user(self):
        self.identifiant = input("Your identifiant ? ")
        if self.identifiant == "":
            self.charge_user()

    def send_message(self):
        response = requests.request(method="POST", url=self.api,
        json=self.payload, headers=self.headers)

        string = json.loads(response.content) 
        brut = string.get('response')

        chat = self.clean_string(brut)
        print(f"\nAI: {chat}\n")

    def main(self):
        print("\npress x key to exit\n".upper())
        while True:
            msg = input("ME: ")
            if msg == "":
                continue
            if msg.lower() == "x":
                break

            self.payload = {
                "user_id": self.identifiant,
                "message": msg,
                "from_name": "Boy",
                "to_name": "Girl",
                "situation": "Girl loves Boy.",
                "translate_from": "fr",
                "translate_to": "fr"
                }

            self.send_message()    

conv = Service("5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6")
