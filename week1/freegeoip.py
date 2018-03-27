import requests
import pprint

def get_location_info(): # объявление функции
    return requests.get("http://freegeoip.net/json/").json()
pprint.pprint((requests.get("http://freegeoip.net/json/").json()))
info = requests.get("http://freegeoip.net/json/").json()
pprint.pprint(info)


