import requests, xmltodict


class SteamAPI():
    def __init__(self, WebKey):
        self.WebKey = WebKey
        self.Session = requests.Session()


    def GetUserInfo(self, SteamID, Type = "id"):
        return xmltodict.parse(self.Session.get(url = f"https://steamcommunity.com/{Type}/{SteamID}/?xml=1").text)


    def GetGameList(self, SteamID64):
        return self.Session.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.WebKey}&steamid={SteamID64}&format=json&include_appinfo=1").json()


    def NormalizeURL(slef, URL):
        URL = URL.replace("http://steamcommunity.com/id/", "")
        URL = URL.replace("https://steamcommunity.com/id/", "")
        URL = URL.replace("http://steamcommunity.com/profiles/", "")
        URL = URL.replace("https://steamcommunity.com/profiles/", "")

        return URL.replace("/", "")
