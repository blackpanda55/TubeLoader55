#! /bin/python3
import pytube
##### info
maker = "blackpanda"
github = "https://github.com/BLAck-PAnda-55"
gmail = "mazenvdgamer870@gmail.com"
telegram = "https://t.me/BLAck_PAnda_55"
bug = " for any problem [ TEXT ME ]"
##### 
video = "mp4"
music = "mp3"

video_ = "1"
music_ = "2"

so1 = "[ "
so2 = " ]"

ban1 = "___________   ___.            .__                    .___            "
ban2 = "\__    ___/_ _\_ |__   ____   |  |   _________     __| _/___________ "
ban3 = "  |    | |  |  \ __ \_/ __ \  |  |  /  _ \__  \   / __ |/ __ \_  __ \ "
ban4 ="  |    | |  |  / \_\ \  ___/  |  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/"
ban5 = "  |____| |____/|___  /\___  > |____/\____(____  /\____ |\___  >__|   "
ban6 = "                  \/     \/                  \/      \/    \/       "

def banner ():
    print(ban1) 
    print(ban2)
    print(ban3)
    print(ban4)
    print(ban5)
    print(ban6)
banner()
url = input(" \nEnter Your Link Here : ")
def would():
    print(" \nWhat You Want ? ")
    print(so1 + "1" + so2 + video)
    print(so1 + "2"+ so2 + music)
would()
would = input(" \nEnter The choose ? : ")
def WAIT():
    print(" \nYour File Will Download In Desktop")
    print("\n WAIT .........")
WAIT()
if would == video_:
    pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')
elif would == music_:
    print(" \nThe File Will DOWNLOAD by mp4 but it is mp3 ,, YOU WILL SEE IT IN REALTY [Desktop] ")
    pytube.YouTube(url).streams.get_audio_only().download('Desktop')
def finesh ():
    print(" \nDOWNLODA is DONE .......")
    print(" \nYour File in Desktop NOW!!")
finesh()

def info():
    print("\nCoded By : " + maker)
    print("Github : " + github)
    print("Gmail : " + gmail)
    print("Telegram : " + telegram)
info()