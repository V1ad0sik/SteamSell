from Module.SteamAPI import *
from Module.Json import *

import datetime, os, pyperclip

Steam = SteamAPI(WebKey = Read("WebKey"))


while (True):
    PersonID = Steam.NormalizeURL(URL = str(input("Введите ссылку на аккаунт: ")))

    Type = "id"
    Info = Steam.GetUserInfo(SteamID = PersonID, Type = Type)

    if ("error" in str(Info)):
        Type = "profiles"
        Info = Steam.GetUserInfo(SteamID = PersonID, Type = Type)


    InfoVar = "\n> Имя: " + str(Info["profile"]["steamID"])
    InfoVar += "\n> Страна: " + str(Info["profile"]["location"])
    InfoVar += "\n> Символов в ID: " + str(len(Info["profile"]["customURL"])) if Type == "id" else "\n> Символов в ID: 0"
    InfoVar += "\n> VAC блокировка: " + "присутствует" if Info["profile"]["vacBanned"] else "отсутствует"
    InfoVar += "\n> Тип профиля: " + str(Info["profile"]["privacyState"])
    InfoVar += "\n> Регистрация: " + str(Info["profile"]["memberSince"])


    pyperclip.copy(InfoVar)

    print(InfoVar)
    print("\n> Информация об аккаунте скопирована в буфер обмена.")
    input("> Нажмите на Enter для продолжения...\n\n")


    SteamID64 = Info["profile"]["steamID64"]
    GameList = Steam.GetGameList(SteamID64 = SteamID64)["response"]


    InfoVar = ("> Всего игр на аккаунте: " + str(GameList["game_count"]) + "\n")
    GameList = GameList["games"]


    for Game in range(len(GameList)):
        Name = GameList[Game]["name"]
        Time = datetime.timedelta(minutes = GameList[Game]["playtime_forever"])

        InfoVar += (f"[{Game + 1}] {Name} ({str(Time) if Time.seconds > 0 else 'не запускалось'})\n")


    pyperclip.copy(InfoVar)

    print(InfoVar)
    print("\n> Информация об играх скопирована в буфер обмена.")
    input("> Нажмите на Enter для продолжения...")

    os.system("cls")
