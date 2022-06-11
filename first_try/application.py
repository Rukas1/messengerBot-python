import requests
response = requests.get("https://api.waifu.pics/sfw/waifu")
print(response.status_code)
print(response.text)
