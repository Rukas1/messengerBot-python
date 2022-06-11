import json

def createBasicHeader(authAPI: str, hostAPI: str=None, outFile: str=None):
    
    headers = {
        "X-RapidAPI-Host": hostAPI if hostAPI else "waifu.p.rapidapi.com",
        "X-RapidAPI-Key": authAPI
    }

    if outFile:
        try:
            with open(outFile, "w", encoding="utf-8") as f:
                json.dump(headers, f, indent=4)
        except:
            print("An occured error apear with the file system")
    
    return headers


def loadBasicHeaderFromFile(headersFile: str):
    
    try:
        with open(headersFile, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("An occured error apear with the file system, the file cannot be load")


def createQuerystring(user_id: str,
                    message: str,
                    from_name: str,
                    to_name: str,
                    situation: str,
                    translate_from: str,
                    translate_to: str):

    return {"user_id": user_id,
            "message": message,
            "from_name": from_name,
            "to_name": to_name,
            "situation": situation,
            "translate_from": translate_from,
            "translate_to": translate_to}

def createBasicQuerystring(user_id: str, message: str, from_name: str, situation: str):
    return {"user_id": user_id,
            "message": message,
            "from_name": from_name,
            "to_name": "Ichinose",
            "situation": situation,
            "translate_from":"auto",
            "translate_to":"auto"}

