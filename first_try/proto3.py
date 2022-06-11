import requests
import json

class Api:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.api = "https://waifu.p.rapidapi.com/v1/waifu"
        self.host = "waifu.p.rapidapi.com"
        self.appData = "application/json"
        self.create_header()

    def __str__(self):
        return f"Api: {self.api} | apiKey: {self.apiKey} | Host: {self.host} | AppData: {self.appData}"

    def create_header(self):
        self.headers = {
	        "X-RapidAPI-Host": self.host,
	        "X-RapidAPI-Key": self.apiKey
        }


class Conversation(Api):
    def __init__(self, apiKey):
        super().__init__(apiKey=apiKey)
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
                "from_name": "Ruka",
                "to_name": "Ichinose", 
                "situation": "je t'aime bien toi",
                "translate_from": "auto",
                "translate_to": "fr"
                }

            self.send_message()

    def send_message(self):

        header_msg = self.headers
        header_msg["content-type"] = self.appData

        response = requests.request(method="POST", url=self.api,
        json=self.payload, headers=header_msg)

        string = json.loads(response.content) 
        brut = string.get('response')

        chat = self.clean_string(brut)
        print(f"\nAI: {chat}\n")

class User(Api):

    def __init__(self, apiKey):
        super().__init__(apiKey)

    def create_user(self):
        user = input("The new ID : ")
        if user == "":
            self.create_user()
        
        payload = {}
        header_user = self.headers
        header_user['user_id'] = user

        url = "https://waifu.p.rapidapi.com/v1/user/id/" + header_user['user_id']

        response = requests.request("PUT", url, json=payload, headers=header_user)
        return response.text

    def get_all_user(self):
        url = "https://waifu.p.rapidapi.com/v1/user/all/id/0"
        response = requests.request("GET", url, headers=self.headers)
        return response.text

class Luncher:

    menu = """\nOptions:
1) Create user
2) Send chat message
3) See all users
x) Leave
>> """

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.options()

    def options(self):

        while True:
            option = input(self.menu)

            match option.lower():
                case "1":
                    print(User(self.apiKey).create_user())
                case "2":
                    Conversation(self.apiKey)
                case "3":
                    print(User(self.apiKey).get_all_user())
                case "x":
                    break
                case _ :
                    self.options()
    
if __name__ == "__main__":
    lunch = Luncher("5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6")

