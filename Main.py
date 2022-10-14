from Module.SteamAPI import *
from Module.Json import *

import datetime, os, pyperclip

Steam = SteamAPI(WebKey = Read("WebKey"))


while (True):
    PersonID = Steam.NormalizeURL(str(input("Введите ссылку на аккаунт: ")))
    Info = Steam.GetUserInfo(SteamID = PersonID)


    InfoVar = "\n> Имя: " + str(Info["profile"]["steamID"]) + "\n"
    InfoVar += "> Страна: " + str(Info["profile"]["location"]) + "\n"
    InfoVar += "> Символов в ID: " + str(len(Info["profile"]["customURL"])) + "\n"
    InfoVar += "> VAC блокировка: " + "присутствует" + "\n" if Info["profile"]["vacBanned"] else "отсутствует" + "\n"
    InfoVar += "> Тип профиля: " + str(Info["profile"]["privacyState"]) + "\n"
    InfoVar += "> Регистрация: " + str(Info["profile"]["memberSince"])


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
