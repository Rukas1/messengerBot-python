from serverCommunication import checkConnection, getUsersCount, sendMessage
from manageService import *

def main():
    head = createBasicHeader("5a81735c33msh0209801770a5b68p13ff98jsn606854c5eda6", outFile="file.json")
    print(getUsersCount(head))
    query = createBasicQuerystring("lucas", "c'est pas facile la programmation", "lucas", "Ichinose loves lucas")
    print(sendMessage(head, query))


if __name__ == "__main__":
    main()
