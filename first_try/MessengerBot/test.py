from botLogging import Logging
import fbchat

class CustomBot(Logging):
    
    thread_id = ""
    thread_type = fbchat.ThreadType.GROUP

    def __init__(self, email: str, password: str = None, cookieSession: str = None):
        super().__init__(email, password, cookieSession)
        self.connect()


    def yes(self):    
        print(self.setDefaultThread(self.thread_id, self.thread_type))
    

user = CustomBot("ichinoseai731@gmail.com", "here_my_password",cookieSession="text.txt")
user.yes()



