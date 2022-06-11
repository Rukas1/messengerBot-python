# fbchat==1.9.7

try:
    import fbchat
    import json
    from getpass import getpass
except ModuleNotFoundError:
    print("Module introuvable, veuillez installer tout les modules demander")
    exit()


class Login(fbchat.Client):

    defaultCookieFile = "default_session.json"

    def __init__(self, email: str, password: str = None, cookieSession: str = None):

        self.email = email
        self.password = password
        self.cookieSession = cookieSession if cookieSession else self.defaultCookieFile


    def connect(self):
        try:
            print(f"Utilisateur: {self.email.split('@')[0]}")
        except:
            print(f"Utilisateur: {self.email}")

        self.cookies = self.load_cookies()
        self.load_session()
        self.save_cookies()


    def load_cookies(self):
        if self.cookieSession != self.defaultCookieFile:
            try:
                with open(self.cookieSession, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.decoder.JSONDecodeError:
                print("Erreur: fichier non conforme, reinitialisation du fichier")
                return None
            except FileNotFoundError:
                print(f"Erreur: fichier {self.cookieSession} non trouvé, creation de celui-ci")
                return None
        else:
            phrase = "Pas de fichier cookies specifier {} du fichier par defaut"
            try:
                with open(self.cookieSession, "r", encoding="utf-8") as f:
                    content = json.load(f)
                word = "utilisation"
            except FileNotFoundError:
                f = open(self.cookieSession, "x", encoding="utf-8")
                f.close()
                word = "creation"
                content = None
            except json.decoder.JSONDecodeError:
                word = "reinitialisation"
                content = None
            finally:
                print(phrase.format(word))
                return content


    def load_session(self):
        if not self.password:
            super().__init__(self.email, getpass(), session_cookies=self.cookies)
        else:
            super().__init__(self.email, self.password, session_cookies=self.cookies)

        sentence = "Connecter via les cookies" if self.cookies else "Initialisation des cookies"
        print(sentence)

        print("Votre id: {}".format(self.uid))


    def save_cookies(self):
        with open(self.cookieSession, "w", encoding='utf-8') as f:
            f.flush()
            json.dump(self.getSession(), f, indent=4)


user = Login("ichinoseai731@gmail.com", "here_my_password", "session.json")
user.connect()
