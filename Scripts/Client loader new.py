import requests
import subprocess
import random
from time import sleep




cookie = ("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_902F3BA606C7C38002F295BD28D067F4F0B1F79AC39945F8F3A902E89F1E8B2AA566FB297A75F4C9A788E12E63D590AA530FD6FC8BA98906B3BB6701CC3F5D922021B73DAA5E614B53972C50C705C700F8C0509BC9568ADFFEB39B22C56B3E7DA4D41067642130C605CD114C4F95C02EADF7223D00150967E7818DB8D1501AC5283B7A72CA263FC15931B45220B954D52C3C869AD898F1932F40D718E41FD989156E13A15D6F26444738B85DC63080BCB6FE682157E5A5F8C461C27473E744467CC5C1C7DB341FAC37DC4262DF995F94BF986EA2BA5556405FD1032331318327B7A2B2FCD1D6360456CE5E1DD7582BE0F7D94A47830F33CE5FD6ED4C711C83BBA5B67A238B0918C28A9F7CE46CA500A8F55D80ABA11CDC231089C89B1EFA049E2A201AB4B0AB2FFDB716948B661CAC24F4A286036E22B15C88FD0DF1A7D8F5626A9B265E156513240A5D90783D45358535A98E9E83C55660786AB48B81C69D117604A50F4A145165C7527731B3FAF27308BDADBA; domain=.roblox.com; expires=Fri, 01-Nov-2052 19:37:31 GMT; path=/; secure; HttpOnly")

gameId = input("Enter gameid: ")


def auther(self, cookie, gameId):
    self.cookie = cookie
    self.gameId = gameId
    self.session = requests.Session()
    self.session.cookies[".ROBLOSECURITY"] = self.cookie
    self.session.headers['x-csrf-token'] = self.session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
    self.auth_ticket = self.session.post('https://auth.roblox.com/v1/authentication-ticket/', headers={'referer':f'https://www.roblox.com/games/{self.gameId}'}).headers['rbx-authentication-ticket']
    self.browserId = random.randint(1000000, 10000000)
    print(self.auth_ticket)
    print(self.browserId)
    print(self.gameId)
def join_game(self):
    game = subprocess.Popen(f"start roblox-player:1+launchmode:play+gameinfo:{self.auth_ticket}+launchtime:{self.browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{self.browserId}%26placeId%3D{self.gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{self.browserId}+robloxLocale:en_us+gameLocale:en_us+channel:", shell=True)
    sleep(10)
    print(self.auth_ticket)
    print(self.browserId)
    print(self.gameId)
    print("Joined!")
