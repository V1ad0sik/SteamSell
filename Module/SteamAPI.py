import requests, xmltodict



class SteamAPI():
    def __init__(self, WebKey):
        self.WebKey = WebKey
        self.Session = requests.Session()


    def GetUserInfo(self, SteamID):
        return xmltodict.parse(self.Session.get(url = f"https://steamcommunity.com/id/{SteamID}/?xml=1").text)


    def GetGameList(self, SteamID64):
        return self.Session.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.WebKey}&steamid=76561198318683779&format=json&include_appinfo=1").json()


    def NormalizeURL(slef, URL):
        return URL.replace("https://steamcommunity.com/id/", "").replace("http://steamcommunity.com/id/", "").replace("/", "")
        