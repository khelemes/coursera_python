import requests

def get_location_info(): # объявление функции
    return requests.get("http://freegeoip.net/json/").json()

#if __name__ == "__main__":
# чтобы программа работала только тогда,
# когда мы запускаем её интерпретатором Python
print(get_location_info())
