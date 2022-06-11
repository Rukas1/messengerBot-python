import requests
import json
import sys

def getResponse(method: str, path: str, headers: str, payload: dict=None, params: dict=None):
    try:
        if payload != None and params != None:
            response = requests.request(method, path, json=payload, headers=headers, params=params)
            return response.text
        else:
            response = requests.request(method=method, url=path, headers=headers)
            text = json.loads(response.text)
        return text

    except json.JSONDecodeError:
        print("The server has an internal error")
    except:
        print("Please, check your Internet connection and try again")
    sys.exit()


def checkConnection(basicHeaders: dict):
    """
    You can create a 'basicHeaders' with a fonction on module 
    manageService, it's called 'createBasicHeader' or by load a file 
    'loadBasicHeaderFromFile'.
    """
    path = "https://waifu.p.rapidapi.com/v1/server/status"

    response = getResponse(method="GET",
                            path=path,
                            headers=basicHeaders)

    return (True if response.get("status") == "ok" else False, response['status'] if "status" in response else response['message'])


def getUsersCount(basicHeaders: dict):
    path = "https://waifu.p.rapidapi.com/v1/user/all/count"
    
    response = getResponse(method="GET",
                            path=path,
                            headers=basicHeaders)

    return response


def sendMessage(basicHeaders: dict, querystring: dict):
    path = "https://waifu.p.rapidapi.com/path"
    payload = {}

    basicHeaders["content-type"] = "application/json"
    response = getResponse("POST", path, basicHeaders, payload, querystring) # this line can catch an error

    return response