from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from gtts import gTTS
from googletrans import Translator
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient
#===================================================================================================
#==================================================================================================
#AKUN SELFBOT+ASIST
#===================================================================================================
print("\nLOGIN                        SB")
cl = LINE("EGcMR6M3v1hvaJaGUKV2.eZ9Xen0a5JxWD2LxG3bvOG.AY3Smk7rTgIvQsCVRC07vlHkmr6rRe80ki100S6w/T0=")
cl.log("Auth Token : " + str(cl.authToken)) #SELFBOT

print("\nLOGIN SUCCESS")
print("==========================================")
print("============[[TOKEN CHROME]]==================")
print("=============================================")
#==============================================================================================================
#==============================================================================================================
oepoll = OEPoll(cl)
call = cl
jaka = ["ua5b1fd053f5a6951349b912a8a7b6755"]
creator = ["ua5b1fd053f5a6951349b912a8a7b6755"]
owner = ["ua5b1fd053f5a6951349b912a8a7b6755"]
admin = ["u133f7110dd00e635f0776957837055a2","ua5b1fd053f5a6951349b912a8a7b6755"]
staff = ["ua5b1fd053f5a6951349b912a8a7b6755"]
Drop_Xv = "u58b4ebbe0cc52d5389669c0957de9e57" #ID_DROPING_BOTS
Xv_WIN = "u58b4ebbe0cc52d5389669c0957de9e57" #ID_WINDOWS_XP
Xv_LAN = "u58b4ebbe0cc52d5389669c0957de9e57" #ID_SERVER_LAN
Xv_Servic = "u58b4ebbe0cc52d5389669c0957de9e57" #ID_PROV_SERVICE
Xv_DxD = "u58b4ebbe0cc52d5389669c0957de9e57" #ID_SYSTEM_BOTS
Line_Import = [Drop_Xv,Xv_WIN,Xv_LAN,Xv_Servic,Xv_DxD] #ALL_IMPORTING
#==============================================================================
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
KAC = [cl]
ABC = [cl]
Bots = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
#===============================================================================
protectcancel = []
welcome = []
targets = []
protectname = []
userTemp = {}
userKicked = []
dict = {}
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []
offbot = []
msg_image={}
msg_video={}
msg_sticker={}
detectUnsend = []
simisimi = []
#===============================================================================
#===============================================================================
nama1 = 'InexBots'
Headers3 = {
        'User-Agent': "CHROMEOS\t9.0.3Bot-Eater\t17.09",
        'X-Line-Application': "CHROMEOS 1.7.14 BotEater x64",
        "x-lal": "ja-US_US",
    }
nama2 = 'InexBots'
Headers = {
        'User-Agent': "Line/8.3.3",
        'X-Line-Application': "DESKTOPWIN\t8.3.0RFU-BOT\t18.99",
        "x-lal": "ja-US_US",
    }
nama3 = 'InexBots'
Headers5 = {
        'User-Agent': "Line/8.0.0",
        'X-Line-Application': "IOSIPAD\t7.18.0\tiPhone OS\t11.12.1",
        "x-lal": "ja-US_US",
    }
settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "detectMention":False,
    "keyCommand": "dent ",
    "commentPost": "Dari pada di bilang sombong\ngw ikutan coment dah",
    "postEndUrl": True,
    "serviceName":[],
    "checkPost": False,
    "setKey": "",
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0',              
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (iPad; CPU OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 \'Mobile/14C92 Safari/602.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik0e Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 \'Mobile/14C92 Safari/602.1'
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "Timeline": True,
    "invite":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "detectMention2":False,
    "arespon":False,
    "MentionKick":False,
    "welcomeOn":False,
    "sticker":False,  
    "selfbot":True,
    "Responpm":"Tag aku lagi di group dong kak, kebetulan agi bojoku gak ada nih..",
    "mention":"Jangan ngintip napa.. sini ikutan chat",
    "Respontag":"Duuhh jgn suka tag kak, bahaya...",
    "welcome":"Wellcome to my Fams",
    "comment":"Auto like done",
    "comment1":"Auto like By InexBots\nBiar gak di katain sombong ikutan koment kak",
    "message":"Makasih kak udh add sya\nSalam santun.."
}

protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[],
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
plates = codecs.open("template.json","r","utf-8")
plate = json.load(plates)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
unsend = json.load(unsendOpen)
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def backupData():
	try:
		backup = read
		f = codecs.open('read.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = tagme
		f = codecs.open('tag.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = settings
		f = codecs.open('setting.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		backup = unsend
		f = codecs.open('unsend.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		logError(error)
		return False      

        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendLineMusic(to):
    contentMetadata = {
        'countryCode': 'ID',
        'i-installUrl': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'a-packageName': 'com.spotify.music',
        'linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'type': 'mt',
        'previewUrl':"http://dl.profile.line-cdn.net/{}".format(cl.profile.pictureStatus),
        'a-linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'text': cl.profile.displayName,
        'id': 'mt000000000a6b79f9',
        'subText': cl.profile.statusMessage
    }
    return cl.sendMessage(to, cl.profile.displayName, contentMetadata, 19)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                        
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + cl.profile.userid
                        cl.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+cl.getContact(mid).pictureStatus, line.getContact(mid).displayName)
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "âââââ[ {} MEMBER GROUP ]ââ\nâ â1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "â â%i.  " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        cl.sendMessage(to, textx+"âââââââââââââââââââââââ", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMentionV3(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print(error)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "{}\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "bye bye"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masukã{}ã\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n â¢ "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")      

              

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "â­âââââââââââââââ\n"
    helpMessage += "â " + "â­ââââââââââââââââââ\n"
    helpMessage += "â" + " âââââââââââââââââââ\n"
    helpMessage += "â" + " âââââââââââââââ\n"
    helpMessage += "â ââ£ %i. " % num + key + "Me\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Speed/sped/sp\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Kepo @\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Mybot\n"
    num = (num+1)   
    helpMessage += "â ââ£ %i. " % num + key + "Name\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Get mid @\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "About\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Time\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Creator\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Ginfo\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Open\n"
    num = (num+1)    
    helpMessage += "â ââ£ %i. " % num + key + "Close\n"
    num = (num+1)
    helpMessage += "â ââ£ %i ." % num + key + "Url grup\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Glist\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Stafflist\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Botlist\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Hapuschat\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "X on/off\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Upfoto\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Upgrup\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Bcast:ãTextã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Set sname\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "name: nama\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "name1/7: nama\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Reset sname\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Ssider: text\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Spesan: text\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Swelcome: text\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Srepson: text\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Upbot ãubah fotoã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Upgrupãubah fotoã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "1/7 up ãubah fotoã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "1/7 in ãjoin grupã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Gruplist 1/7\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Csider/off\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Cpesan/off\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Crespon\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Cwelcome\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Stickerãon/off\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "ãon/offã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Unsendãon/offã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Autoblockãon/offã\n"
    num = (num+1)
    helpMessage += "â ââ£ %i. " % num + key + "Welcomeãon/offã\n"
    num = (num+1)    
    helpMessage += "â " + "âââââââââââââââ\n"
    helpMessage += "â " + "â°ââââââââââââââââââ\n"
    helpMessage += "â°ââââââââââââââââ"
    helpMessage += " Creator: https://line.me/ti/p/~denjaka_inex \n"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "â­ââââââââââââââââ\n"
    helpMessage2 += "â " + "â­âââââââââââââââââââ\n"
    helpMessage2 += "â" + " âââââââââââââââââââ\n"
    helpMessage2 += "â" + " âââââââââââââââ\n"
    helpMessage2 += "â ââ£ %i. " % num + key + "Crot @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Cipok @ \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Mainkan @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Invite/stay \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Bl \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Ban all\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Unban all \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Refresh \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Gas\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Killban \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Spaminvite on \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Spaminvite off \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Banlist\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Ban all\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Clearban\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Adminexpl:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Admin:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Admin:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Adminexpl:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Owner:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Staff:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Staff:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Staffexpl:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Staffexpl:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Bot:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Bot:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Botexpl:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Botexpl:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Ban:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Ban:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Unban:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Unban:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i ." % num + key + "Talkban:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Talkban:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Untalkban:on @\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Untalkban:on\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Talkbanlist\n"
    num = (num+1)    
    helpMessage2 += "â ââ£ %i. " % num + key + "P o/f (protect)\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Skurl on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Protect on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Proall on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Skinvite on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Procancel on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "J o/f\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + ".Bye/Bye[1/4]\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "LeaveãNamagrupã\n"
    num = (num+1)    
    helpMessage2 += "â ââ£ %i. " % num + key + "Kickerãinã\n"
    num = (num+1)  
    helpMessage2 += "â ââ£ %i. " % num + key + "Kickerãlvã\n"
    num = (num+1)    
    helpMessage2 += "â ââ£ %i. " % num + key + "Infogrupãangkaã\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Infomemãangkaã\n"
    num = (num+1)     
    helpMessage2 += "â ââ£ %i. " % num + key + "Silentkiller [kickall]\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Bubar [kickall]\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Prank \n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Autojoin on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Jointicket on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "Autoadd on/off\n"
    num = (num+1)
    helpMessage2 += "â ââ£ %i. " % num + key + "leave on/off\n"
    num = (num+1)
    helpMessage2 += "â " + "âââââââââââââââ\n"
    helpMessage2 += "â " + "â°âââââââââââââââââââ\n"
    helpMessage2 += "â°ââââââââââââââââ"
    helpMessage2 += " My ID LINE : ã https://line.me/ti/p/~denjaka_inex ã\n"
    return helpMessage2
    
def helpbot1():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "â­ââââââââââââââââ\n"
    helpMessage3 += "â " + "â­âââââââââââââââââââ\n"
    helpMessage3 += "â" + " âââââââââââââââââââ\n"
    helpMessage3 += "â" + " âââââââââââââââ\n"
    helpMessage3 += "â ââ£ %i. " % num + key + "Meme@1@k1@k2 \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Getmeme \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Meme k1|k2|no \n"
    num = (num+1)  
    helpMessage3 += "â ââ£ %i. " % num + key + "Smule: link \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Profilsmule: id \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "tafsirquran no|no \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Lihat no|no\n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Sukaku @ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Get-mimpiãQueryã\n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Get-apkãQueryã\n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Ytmp4: Judul Video \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Changedual \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Changedualurl: â¢linkâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Img food: produk \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Profilesmule: id \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Profileig: id \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Addimg â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Dellimg â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Listimg â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Addvideo â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Dellvideo â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Listvideo â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Addsticker â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Dellsticker â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Liststicker â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Addaudio â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Dellaudio â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â ââ£ %i. " % num + key + "Listaudio â¢namaâ¢ \n"
    num = (num+1)
    helpMessage3 += "â " + "âââââââââââââââ\n"
    helpMessage3 += "â " + "â°âââââââââââââââââââ\n"
    helpMessage3 += "â°ââââââââââââââââ"
    helpMessage3 += " My ID LINE : ã https://line.me/ti/p/~denjaka_inex ã\n"
    return helpMessage3
    
def helpbot2():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "â­ââââââââââââââââ\n"
    helpMessage4 += "â " + "â­âââââââââââââââââââ\n"
    helpMessage4 += "â" + " âââââââââââââââââââ\n"
    helpMessage4 += "â" + " âââââââââââââââ\n"
    helpMessage4 += "â ââ£ %i. " % num + key + "Help\n"
    num = (num+1)
    helpMessage4 += "â ââ£ %i. " % num + key + "Menu\n"
    num = (num+1)
    helpMessage4 += "â ââ£ %i. " % num + key + "Media\n"
    num = (num+1)
    helpMessage4 += "â ââ£ %i. " % num + key + "Helpkick\n"
    num = (num+1)
    helpMessage4 += "â ââ£ %i. " % num + key + "Settings\n"
    num = (num+1)
    helpMessage4 += "â " + "âââââââââââââââ\n"
    helpMessage4 += "â " + "â°âââââââââââââââââââ\n"
    helpMessage4 += "â°ââââââââââââââââ"
    helpMessage4 += " My ID LINE : ã https://line.me/ti/p/~denjaka_inex ã\n"
    return helpMessage4
def sendTextTemplate7(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~denjak_inex"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "INEXBOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.sendFlex(to, data)
def sendTextTemplate44(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "{} Mencintaimu ".format(cl.getProfile().displayName),
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#0000FF",
               },
               "body": {
                 "backgroundColor": "#000000",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "Nama : {}".format(cl.getContact(op.param2).displayName),
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "{}".format(cl.getContact(op.param2).displayName)+str(text),
                               "wrap": True,
                               "color": warnanya1,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warnanya1,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
    cl.sendFlex(to, data)
 
def sendTextTemplate1(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
                "type": "template",
                "altText": "InexBots",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    cl.sendFlex(to, data)

def sendTextTemplate2(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "InexBots",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.sendFlex(to, data)
 
def sendTextTemplate13(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "CCTV",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [          
          {
            "text": "    CCTV POLANTAS",
            "size": "xs",
            "color": "#00FF33",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          },
          {
            "type": "separator",
            "color": "#000000"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
       {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "sm",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#006400",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
def sendAutolike(to,text):
    data = {
        "type": "template",
        "altText": "AUTO LIKE DONE",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                    "title": "{}".format(cl.getContact(msg._from).displayName),
                    "text": text,
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "http://line.me/ti/p/~denjaka_inex"
                        }
                      ]
                    }
                  ]
                }
               }
    cl.sendFlex(to, data)
def sendTextTemplate3(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "Denjaka",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#40ff00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#03f5f1"
    },
    "header": {
      "backgroundColor": "#03f5f1"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#ff0a3b",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#310dff",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~denjaka_inex"
           }                                                
 }
]
                          }
                      }
    cl.sendFlex(to, data)
def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menyukai anda di sini".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#006400",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
def sendTextTemplate(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
        "type": "flex",
        "altText": "flex template",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": text,
                        "color": "#3800E0",
                        "wrap": True
                    }
                ]
            }
        }
    }
    cl.sendFlex(to, data)
def sendCyduk(to, text):
    contact = cl.getContact(op.param2)
    favoritelist = cl.getFavoriteMids()
    grouplist = cl.getGroupIdsJoined()
    contactlist = cl.getAllContactIds()
    blockedlist = cl.getBlockedContactIds()
    data = {
                                "type": "flex",
                                "altText": "{} Lagi nyari janda".format(dzProfile.displayName),
                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000080"
    },
    "footer": {
      "backgroundColor": "#000080"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text": "BIO DATA\n? NAMA: {}".format(cl.getContact(op.param2).displayName)+"\n? GROUP: {}".format(str(len(grouplist)))+"\n? FRIEND : {}".format(str(len(contactlist)))+"\n? FAFORITE : {}".format(str(len(favoritelist)))+"\n? BLOCKED : {}".format(str(len(blockedlist)))+"\nBio: {}".format(cl.getContact(op.param2).statusMessage),
            "size": "sm",
            "color": "#FF3366",
            "wrap": True,
            "type": "text",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "type": "image",
            "size": "full"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [            
              {
                "size": "xxl",
                "type": "icon",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus)
              },
              {
                "text": text,
                "size": "sm",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text",
                "align": "center"            
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
def sendWelcome(to,text):
    data = {
            "type": "flex",
            "altText": "JANGAN KABUR DARI GRUP KAK",
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#000080",
               },
               "body": {
                 "backgroundColor": "#0000FF",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "WELCOME",
                   "weight": "bold",
                   "color": "#FF0000",
                   "size": "xxl"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://thumbs.gfycat.com/DearestPoshAfricanclawedfrog.webp",
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": str(textx),
                               "wrap": True,
                               "color": "#00FF00",
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": "#00FF00",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
    cl.sendFlex(to, data)
warKey = """â­ââââââââââââââââââââ
â ââââââââââââââââââââââ
â â  BY BOT : INEXBOTS
â ââââââââââââââââââââââ
ââââââââââââââââââââââ
â ââââââââââââââââââââââ
â â  LIKE DONE 
â â  COMMENT DONE 
â â  INEXBOTS  
â ââââââââââââââââââââââ
ââââââââââââââââââââââ
â ââââââââââââââââââââââ
â â  http://line.me/ti/p/~denjaka_inex
â ââââââââââââââââââââââ
â°âââââââââââââââââââââ
"""
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param2 in wait["blacklist"] == True:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                except:
                    pass
#====================================================================                                                  
#====================================================================                            
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
#====================================================================                            
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[Zmid,Dhenza])
                            wait["blacklist"][op.param2] = True
                    except:
                        pass
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return                                       
#====================================================================
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancleGroupInvitation(op.param1,[op.param2])
                    except:
                        pass
                return                                
#====================================================================                            
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return                      
#====================================================================                                            
        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True    
                    try:
                        admin.kickoutFromGroup(op.param1,[op.param2])
                        admin.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid,Dhenza,Jaka])
                        cl.acceptGroupInvitation(op.param1)
                        admin.kickoutFromGroup(op.param1,[op.param2])
                        admin.cancelGroupInvitation(op.param1,[op.param2])
                        admin.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
#====================================================================                            
#====================================================================                                
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                #welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
            "type": "flex",
            "altText": "JANGAN KABUR DARI GRUP KAK",
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#000080",
               },
               "body": {
                 "backgroundColor": "#0000FF",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "{} WELCOME".format(cl.getContact(op.param2).displayName),
                   "weight": "bold",
                   "color": "#FF0000",
                   "size": "xxl"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": str(wait["welcome"]),
                               "wrap": True,
                               "color": "#00FF00",
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": "#00FF00",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
                cl.sendFlex(op.param1, data)
                
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2).picturePath
                data = {
            "type": "flex",
            "altText": "kickall",
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#000080",
               },
               "body": {
                 "backgroundColor": "#0000FF",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "{} LEAVE".format(cl.getContact(op.param2).displayName),
                   "weight": "bold",
                   "color": "#FF0000",
                   "size": "xxl"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "Selamat jalan,,, semoga d luar gak kdinginan",
                               "wrap": True,
                               "color": "#00FF00",
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": "#00FF00",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
                cl.sendFlex(op.param1, data)
             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
                        
        if op.type == 5:
            if settings['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(op.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, op.param1)
                    wait["Blacklist"][op.param2] = True
                except Exception as e:
                	print (e)

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                cl.findAndAddContactsByMid(op.param1,[admin])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[admin])
                                wait["blacklist"][op.param2] = True
                        except:
                            pass

#====================================================================                            
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        cl.findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    
            if op.param1 in protect["antijs"]:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        #cl.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        cl.inviteIntoGroup(op.param1,[admin])
                        wait["blacklist"][op.param2] = True
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass
  #===================================================================================================              
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])            
                                cl.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                settings['SpamInvite'] = False
                            except:             
                                 cl.sendMessage(msg.to, 'Contact error')
                                 settings['SpamInvite'] = False
                                 break
#===================================================================================================        
        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                #if receiver in temp_flood:
                    #if temp_flood[receiver]["expire"] == True:
                        #if cmd == "open" and sender == mid:
                            #temp_flood[receiver]["expire"] = False
                            #temp_flood[receiver]["time"] = time.time()
                            #cl.sendMessage(to, "Bot kembali aktif")
                        #return
                    #elif time.time() - temp_flood[receiver]["time"] <= 1:
                        #temp_flood[receiver]["flood"] += 1
                        #if temp_flood[receiver]["flood"] >= 20:
                            #temp_flood[receiver]["flood"] = 0
                            #temp_flood[receiver]["expire"] = True
                            #ret_ = "Spam terdeteksi, Bot akan silent selama 30 detik pada ruangan ini atau ketik {}Open untuk mengaktifkan kembali.".format(setKey)
                            #cl.sendMessage(to, str(ret_))
                    #else:
                         #temp_flood[receiver]["flood"] = 0
                         #temp_flood[receiver]["time"] = time.time()
                #else:
                    #temp_flood[receiver] = {
    	                #"time": time.time(),
    	                #"flood": 0,
    	                #"expire": False
                    #}             
#===================================================================================================        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                      if op.param2 in Bots:
                        pass
                      else:
                        Name = cl.getContact(op.param2).displayName
                        Np = cl.getContact(op.param2).pictureStatus
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n? " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    sendCyduk(op.param1, wait["mention"])
                                else:
                                    sendTextTemplate44(op.param1, "Woy " +  nick[1] + "\nBetah Banget Jadi Cicitipi. . \nChat Woy (-__-)   ")
                            else:
                                sendTextTemplate7(op.param1, "Nah.. " + "? " + Name + " ?" + "\nNgapain Cicitipi Doang???\nGa Gaul Lu ga Mau Chat\nPasti Temennya Dikit ")
                    else:
                        pass
                else:
                    pass
            except:
                pass
                                                                     
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = "ââââââââââââââââââââââ\nâ   Gambar Dihapus \nâ Pengirim : "
                                ret_ = "â Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nâ Waktu Ngirim : {}\nââââââââââââââââââââââ".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "âPesan Dihapus \n"
                                ret_ += "âPengirim : {}".format(str(ryan.displayName))
                                ret_ += "\nâNama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nâWaktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nâPesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                sendTextTemplate11(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  " Sticker Dihapus \n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sendTextTemplate(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e) 
                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\nSticker ID : {}".format(stk_id)
                   ret_ += "\nSticker Version : {}".format(stk_ver)
                   ret_ += "\nSticker Package : {}".format(pkg_id)
                   ret_ += "\nSticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\nSticker ID : {}".format(stk_id)
                   ret_ += "\nSticker Version : {}".format(stk_ver)
                   ret_ += "\nSticker Package : {}".format(pkg_id)
                   ret_ += "\nSticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["arespon"] == True: 
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           contact = cl.getContact(msg._from)
                           sendMentionV3(sender, "@! Tag lagi dong d grup", [sender])
                           warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                           warnanya1 = random.choice(warna1)
                           data = {
            "type": "flex",
            "altText": "{} Cieeeee... Kang tag".format(cl.getContact(sender).displayName),
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#0000FF",
               },
               "body": {
                 "backgroundColor": "#000000",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "{}".format(cl.getContact(sender).displayName),
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~denjaka_inex"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "{} \n".format(cl.getContact(sender).displayName)+str(wait["Responpm"]),
                               "wrap": True,
                               "color": warnanya1,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warnanya1,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
                           cl.sendFlex(sender, data)
                           #cl.sendFlex(sender, plate["pricelist"])
                           break
               if 'MENTION' in msg.contentMetadata.keys()!= None:
                   names = re.findall(r'@(\w+)', text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                       if mid in mention["M"]:
                           if wait["detectMention2"] == True:
                               contact = cl.getContact(msg._from)
                               cover = cl.getProfileCoverURL(msg._from)
                               path = "http://dl.profile.line.naver.jp/"+ contact.pictureStatus
                               try:
                                 poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                               except:
                                 poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                               data = {
        "type": "flex",
            "altText": "TOOOOLLLOOOOOOOOONGGG...",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "{} \n".format(cl.getContact(msg._from).displayName)+str(wait["Respontag"]),
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#40ff00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#03f5f1"
    },
    "header": {
      "backgroundColor": "#03f5f1"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#ff0a3b",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#310dff",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
                               cl.sendFlex(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["MentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Done Tag Me !")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "Details Post"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\nPenulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\nURL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\nStiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\nTulisan :\n{}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\nFinish"
                                    sendTextTemplate7(to, str(ret_))
                                except:
                                    sendTextTemplate11(to, "Post tidak valid")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], wait["comment1"])
                                adws = cl.createComment(purl[0], purl[1], warKey)

            except Exception as error:
                logError(error)
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = " Detail Postingan "
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\nð´ Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\nð´ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\nð´ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nð´ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\nð´ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nð´ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\nð´ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nð´ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nð´ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\nð´ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\nð´ Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            sendTextTemplate11(to, str(ret_))
                            cl.likePost(purl[25:58], purl[66:], likeType=1001)                                                        
                            cl.createComment(purl[25:58], purl[66:], wait["comment"])
                            sendTextTemplate1(to, "Like done")
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n Sticker Info "
                   ret_ += "\n Sticker ID : {}".format(stk_id)
                   ret_ += "\n Sticker Version : {}".format(stk_ver)
                   ret_ += "\n Sticker Package : {}".format(pkg_id)
                   ret_ += "\n Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if settings["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = " Sticker Info "
                            ret_ += "\nð´ STICKER ID : {}".format(stk_id)
                            ret_ += "\nð´ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\nð´ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\nð´STICKER URL : line://shop/detail/{}".format(pkg_id)
                            sendTextTemplate44(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = " Sticker Info "
                            ret_ += "\nð´ PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\nð´ AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\nð´ STICKER ID : {}".format(str(stk_id))
                            ret_ += "\nð´ STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\nð´ STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\nð´ STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\nð´ DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            sendTextTemplate2(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate11(msg.to,"  Contact Info \n Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "Dia ke bl kak... hpus bl dulu lalu invite lagi")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  " Sukses Invite \nNama "
                                  ret_ = "Ketik Invite off jika sudah done"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  sendTextTemplate(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
#ADD Bots&media
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "Succes change pict group")
                            
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help" or cmd == "Help":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["helpgrup"])
                               
                        elif cmd == "helpbot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               sendTextTemplate15(msg.to, str(helpMessage2))
                               
                        elif cmd == "media":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage3 = helpbot1()
                               sendTextTemplate11(msg.to, str(helpMessage3)) 
                              
                        elif cmd == ".help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage4 = helpbot2()
                               sendTextTemplate11(msg.to, str(helpMessage4)) 
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "Bot telah di aktifkan")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "Bot off smentara waktu")
                                
                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.pictureStatus + "/vp")                                            
                                                
                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   â£â SETTING MENU ââ£\n\n"
                                if wait["sticker"] == True: md+="ãâãSticker\n"
                                else: md+="ãâãSticker\n"
                                if wait["contact"] == True: md+="ãâãContact\n"
                                else: md+="ãâãContact\n"
                                if wait["detectMention"] == True: md+="ãâãRespon\n"
                                else: md+="ãâãRespon\n"
                                if wait["detectMention2"] == True: md+="ãâãRespon2\n"
                                else: md+="ãâãRespon2\n"
                                if wait["arespon"] == True: md+="ãâãRespon pm\n"
                                else: md+="ãâãRespon pm\n"
                                if wait["autoJoin"] == True: md+="ãâãAutojoin\n"
                                else: md+="ãâãAutojoin\n"
                                if settings["autoJoinTicket"] == True: md+="ãâãJointicket\n"
                                else: md+="ãâãJointicket\n"
                                if settings["unsendMessage"] == True: md+="ãâãUnsend\n"
                                else: md+="ãâãUnsend\n"
                                if wait["autoAdd"] == True: md+="ãâãAutoadd\n"
                                else: md+="ãâãAutoadd\n"
                                if msg.to in welcome: md+="ãâãWelcome\n"
                                else: md+="ãâãWelcome\n"
                                if wait["autoLeave"] == True: md+="ãâãAutoleave\n"
                                else: md+="ãâãAutoleave\n"
                                if msg.to in protect["pqr"]: md+="ãâãSkurl\n"
                                else: md+="ãâãSkurl\n"
                                if msg.to in protect["proall"]: md+="ãâãProall\n"
                                else: md+="ãâãProall\n"
                                if msg.to in protect["protect"]: md+="ãâãProtect\n"
                                else: md+="ãâãProtect\n"
                                if msg.to in protect["pinv"]: md+="ãâãSkinvite\n"
                                else: md+="ãâãSkinvite\n"
                                if msg.to in protect["antijs"]: md+="ãâãJs\n"
                                else: md+="ãâãJs\n"
                                if msg.to in ghost: md+="ãâãGhost\n"
                                else: md+="ãâãGhost\n"
                                if msg.to in protectcancel: md+="ãâãProcancel\n"
                                else: md+="ãâãProcancel\n"
                                sendTextTemplate13(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")                              
                                

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "ð´My Creator\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = help2()
                               sendTextTemplate3(to,helpMessage2)

                        elif cmd == "galeri" or cmd == "Galeri":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["galery"])

                        elif cmd == "Align" or cmd == "align":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["align"])

                        elif cmd == "owner" or cmd == "Owner":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["owner"])

                        elif cmd == "block" or cmd == "Block":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["block"])

                        elif cmd == "filler" or cmd == "Filler":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["filler"])

                        elif cmd == "warna" or cmd == "Warna":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["color1"])

                        elif cmd == "warna2" or cmd == "Warna2":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["color2"])

                        elif cmd == "Spaces" or cmd == "spaces":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["spaces"])

                        elif cmd == "buton" or cmd == "Buton":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, button["button"])

                        elif cmd == "Filler" or cmd == "filler":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, filler["filler"])

                        elif cmd == "Poto" or cmd == "poto":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            data = {
        "type": "template",
        "altText": "AUTO LIKE DONE",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                    "title": "Nama: {}".format(cl.getContact(msg._from).displayName),
                    "text": "Bio: {}".format(cl.getContact(msg._from).statusMessage),
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "http://line.me/ti/p/~denjaka_inex"
                         }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://1.bp.blogspot.com/-0cJUYiIj9So/Wg_statUjsI/AAAAAAAAK1k/6L1sY5xJEIUfi-8hxW6KuKBSy6jiVoChQCLcBGAs/s1600/Casey_Youtube_GIF.0.gif",
                    "title": "BAGIAN 2",
                    "text": "TEKS CORESOLE2 2",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "LINK 1",
                            "uri": "http://line.me/ti/p/~denjaka_inex"
                        }
                      ]
                    }
                  ]
                }
               }
                            cl.sendFlex(to, data)

                        elif cmd == "Texs" or cmd == "texs":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, teks["teks"])

                        elif cmd == "Booble" or cmd == "booble":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, booble["booble"])

                        elif cmd == "helpmedia":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMedia = media()
                               sendTextTemplate10(to,helpMedia)
                               
                        elif cmd == "price":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["pricelist"])
                        elif cmd == "movie":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["movie"])
                        elif cmd == "listapp":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["listapp1"])
                            cl.sendFlex(to, plate["listapp2"])
                        elif cmd == "me":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                              contact = cl.getContact(msg._from)
                              cover = cl.getProfileCoverURL(msg._from)
                              h = cl.getContact(msg._from)
                              cl.reissueUserTicket()
                              try:
                                poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                              except:
                                poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                              data = {
                             "type": "flex",
                             "altText": "{} Bagi-bagi rezeki".format(str(h.displayName)),
                             "contents": {
                              "type": "bubble",
                              "styles": {
                                "header": {
                                  "backgroundColor": "#000000",
                                },
                                "body": {
                                  "backgroundColor": "#000000",
                                  "separator": True,
                                  "separatorColor": "#ffffff"
                                },
                                "footer": {
                                  "backgroundColor": "#000080",
                                  "separator": True
                                }
                              },
                              "header": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "  INDONESIA_WARS",
                                    "weight": "bold",
                                    "color": "#00ffff",
                                    "size": "xxl"
                                  }
                                ]
                              },
                              "hero": {
                                "type": "image",
                                "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka_inex"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka_inex"
                                },
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": h.displayName,
                                    "size": "md",
                                    "color": "#00ffff"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                          {
                                            "type": "icon",
                                            "url": "https://qr-official.line.me/L/"+cl.getUserTicket().id+".png",
                                            "size": "5xl"
                                          },
                                          {
                                            "type": "text",
                                            "text": "Cover Ticket : ",
                                            "weight": "bold",
                                            "color": "#008B8B",
                                            "margin": "sm",
                                            "flex": 0
                                          },
                                          {
                                            "type": "text",
                                            "text": "InexWars",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                           }
                                         ]
                                       },
                                       {
                                         "type": "box",
                                         "layout": "baseline",
                                         "contents": [
                                           {
                                             "type": "icon",
                                             "url": cover,
                                             "size": "5xl"
                                           },
                                           {
                                             "type": "text",
                                             "text": "Cover Base:",
                                             "margin": "sm",
                                             "color": "#008B8B",
                                             "weight": "bold",
                                             "flex": 0
                                           },
                                           {
                                             "type": "text",
                                             "text": "Id_InexBots",
                                             "size": "sm",
                                             "align": "end",
                                             "color": "#aaaaaa"
                                          }
                                        ]
                                      }
                                    ]
                                  },
                                  {
                                    "type": "text",
                                    "text": "________________________________________________\nThanks to Allah SWT \nThanks to Acil PrankBost And ZE tidur[call]ajah\nAnd my team InexBots.\n________________________________________________\nBio: {}".format(cl.getContact(msg._from).statusMessage),
                                    "wrap": True,
                                    "color": "#aaaaaa",
                                    "size": "xxs"
                                  }
                                ]
                              },
                              "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "spacer",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "button",
                                    "style": "primary",
                                    "color": "#10CF08",
                                    "action": {
                                      "type": "uri",
                                      "label": "SUPORT PLATE",
                                      "uri": "line://app/1623679774-k9nBDB6b?type=sticker&stk=anim&sid=36276468&pkg=3259824"
                                    }
                                  }
                                ]
                              }
                             }
                            }
                              cl.sendFlex(to, data)
                        elif cmd == 'status.':
                          if wait["selfbot"] == True:
                           if msg._from in jaka:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2019
                                bln = 2     #isi bulannya yg sewa
                                hr = 17    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = cl.getContact(mid)
                                favoritelist = cl.getFavoriteMids()
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                #cl.sendText("ua5b1fd053f5a6951349b912a8a7b6755", '.')
                                elapsed_time = time.time() - start
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " INFORMASI SELFBOT?\nUSER : "
                                ret1_ = " GROUP : {} GROUP".format(str(len(grouplist)))
                                ret2_ = " FRIEND : {} FRIEND".format(str(len(contactlist)))
                                ret3_ = " BLOCKED : {} BLOCKED".format(str(len(blockedlist)))
                                ret4_ = " FAFORITE : {} FAFORITE".format(str(len(favoritelist)))
                                ret5_ = " VERSION : .8.14.2 "
                                ret6_ = " EXPIRED : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret7_ = " IN DAYS : {} AGAIN".format(days)
                                ret8_ = " Speed respon {} DETIK".format(str(elapsed_time))
                                ret9_ = " Selfbot respon {}".format(str(bot))
                                #ret10_ += " INEXBOTS"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret1_ + ret2_ + ret3_ + ret4_ + ret5_ + ret6_ + ret7_ + ret8_ + ret9_ + ""
                                #cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                h = cl.getContact(msg._from)
                                cl.reissueUserTicket()
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                data = {
                               "type": "flex",
                               "altText": "{} Lagi di sawah ".format(str(h.displayName)),
                               "contents": {
                                "type": "bubble",
                                "styles": {
                                  "header": {
                                    "backgroundColor": "#003DF5",
                                  },
                                  "body": {
                                    "backgroundColor": "#0000FF",
                                    "separator": True,
                                    "separatorColor": "#ffffff"
                                  },
                                  "footer": {
                                    "backgroundColor": "#0000FF",
                                    "separator": True
                                  }
                                },
                                "header": {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "MASA AKTIF BOT",
                                      "weight": "bold",
                                      "color": warnanya1,
                                      "size": "xxl"
                                    }
                                  ]
                                },
                                "hero": {
                                  "type": "image",
                                  "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                  "size": "full",
                                  "aspectRatio": "20:13",
                                  "aspectMode": "cover",
                                  "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/ti/p/~denjaka_inex"
                                  }
                                },
                                "body": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "spacing": "md",
                                  "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/ti/p/~denjaka_inex"
                                  },
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "INEXBOTS",
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": "User Name: {}" .format(str(dzProfile.displayName)),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret1_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret2_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret3_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret4_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret5_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret6_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret7_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret8_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": str(ret9_),
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": "Open Order Bot",
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": "1",
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": "2",
                                      "size": "md",
                                      "color": warnanya1,
                                    },
                                    {
                                      "type": "text",
                                      "text": "3",
                                      "size": "md",
                                      "color": warnanya1,
                                    }
                                  ]
                                },
                                "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "spacer",
                                      "size": "sm"
                                    },
                                    {
                                      "type": "button",
                                      "style": "primary",
                                      "color": "#10CF08",
                                      "action": {
                                        "type": "uri",
                                        "label": "MY CONATCT",
                                        "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                                      }
                                    }
                                  ]
                                }
                               }
                              }
                                cl.sendFlex(to, data)
                                #cl.sendContact(to, "")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))
                              
                                                                       
                        elif text.lower() == "midku":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd  == "my":
                          if msg._from in admin:
                              try:
                                  sendLineMusic(msg.to)
                              except:sendLineMusic(msg.to)
                               
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)                              
                               
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "sá´á´á´á´ É¢Êá´á´ sá´á´á´Ê á´ÉªÊá´á´á´Êá´á´É´")

                        elif text.lower() == "hapuschat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif cmd.startswith("pictlab "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               separate = text.split(" ")
                               teks = text.replace(separate[0] + " ","")
                               url1 = "https://memegen.link/buzz/"+teks+".jpg"
                               url2 = "https://memegen.link/joker/"+teks+".jpg"
                               url3 = "https://memegen.link/cbg/"+teks+".jpg"
                               url4 = "https://memegen.link/fry/"+teks+".jpg"
                               url5 = "https://memegen.link/yuno/"+teks+".jpg"
                               url6 = "https://memegen.link/fa/"+teks+".jpg"
                               url7 = "https://memegen.link/iw/"+teks+".jpg"
                               url8 = "https://memegen.link/blb/"+teks+".jpg"
                               url9 = "https://memegen.link/doge/"+teks+".jpg"
                               url10 = "https://memegen.link/firsttry/"+teks+".jpg"
                               data = {
                "type": "template",
                "altText": "SendgifPicture",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": url1,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url2,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url3,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url4,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url5,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url6,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url7,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url8,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url9,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url10,
                      "action": {
                        "type": "uri",
                        "uri": "http://line.me/ti/p/~denjaka_inex",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                               cl.sendFlex(to, data)

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   #cl.sendMessage(group,"ð´Broadcast \n\n" + str(pesan))
                                   data = {
        "type": "template",
        "altText": "!kickall",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                    "title": "ð´Broadcastð´ ",
                    "text": str(pesan),
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "http://line.me/ti/p/~denjaka_inex"
                         }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                    "title": "Nama: {}".format(cl.getContact(msg._from).displayName),
                    "text": "Bio: {}".format(cl.getContact(msg._from).statusMessage),
                    "actions": [
                        {
                            "type": "uri",
                            "label": "ORDER",
                            "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"
                        }
                      ]
                    }
                  ]
                }
               }
                                   cl.sendFlex(group, data)

                        elif cmd.startswith("broadcast: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " [BC] \nBroadcast by "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "ð´ Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, " Status Setkey \nSetkey saat ini " + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, " Change Setkey \nSetkey diganti jadi{}".format(str(key).lower()))
                                   
                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, " Resetkey \nSetkey mu telah direset")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate(msg.to, "ð´Sname change \n\nSname succes change to {}".format(str(key).lower()))
                        #elif text.lower() == "yasin" or text.lower() == "yasinan":
                            #sendTextTemplate(msg. to, yasin1)
                            #sendTextTemplate(msg. to, yasin2)
                            #sendTextTemplate(msg. to, yasin3)
                            #sendTextTemplate(msg. to, yasin4)
                            #sendTextTemplate(msg. to, yasin5)

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "Succes Reset Sname ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "Done...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               sendTextTemplate(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            group = cl.getGroup(msg.to)
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "SUDAH PUSKUN ORANGNYA"
                            if group.invitee is None:
                                gPending = "0"
                            else:
                                gPending = str(len(group.invitee))
                            if group.preventedJoinByTicket == True:
                                gQr = "Closed"
                                gTicket = "Qr tidak tersedia karna di tutup"
                            else:
                                gQr = "Open"
                                gTicket = "https://me.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                            timeCreated = []
                            timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(group.createdTime) / 1000)))
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ret_ = "[ Group Info ]"
                            ret_ += "\n Nama Group : {}".format(str(group.name))
                            ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                            ret_ += "\nID Group : {}".format(group.id)
                            ret_ += "\n Pembuat : {}".format(str(gCreator))
                            ret_ += "\n Jumlah Member : {}".format(str(len(group.members)))
                            ret_ += "\n Jumlah Pending : {}".format(gPending)
                            ret_ += "\nKode Qr/Link"
                            ret_ += "\n Group Ticket : {}".format(gTicket)
                            ret_ += "\n Group Qr : {}".format(gQr)
                            ret_ += "\n[ INEXBOT]"
                            #sendTextTemplate11(to, ret_)
                            warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            data = {
                                "type": "flex",
                                "altText": "Info grup",
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": str(ret_),
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": warnanya1,
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(group.pictureStatus),
    "size": "full",
    "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#006400",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
                            cl.sendFlex(to, data)
                        elif "sepi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/hHG5Mwb/AW316819-05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/12555"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "jones" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-f1Ac9hha1NA/WE_QkvJGBEI/AAAAAAAFMuA/xNeS9_M2O0M3t2cv6YFjHSLlD8TcAW6GwCLcB/s1600/AW293929_02.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/1300406"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "joget" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://2.bp.blogspot.com/-kZkuLDoIBIE/WuEwLxrL4xI/AAAAAAALXOo/TNCmzjzaCgM34zbg8SiwB188fdYfJ_jcgCLcBGAs/s1600/AS0003898_05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/11959"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-vOOo0PmF-RM/Wfnb01EIpgI/AAAAAAAMKE4/kReJM5yOdMIa6fFJ3wUHs1mk7EaaApH0ACLcBGAs/s1600/AW601285_05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/1759910"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "hbd" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-oSvbZPD_f44/WD-9iCgZAtI/AAAAAAAEAWA/upoLkbvxwmQqSZ2Ch2Lk3kl3X_HpkyMFQCLcB/s1600/AW284627_03.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/1291200"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "assalam" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://gifimage.net/wp-content/uploads/2018/05/salam-gif-2.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/3157914"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif "gimana" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/LikelyValidAmericancrocodile-size_restricted.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "https://line.me/S/sticker/3157914"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.sendFlex(to, data)
                        elif msg.text.lower().startswith("chrome"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers3.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers3)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=nama1)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Segera klik LOGIN untuk Login\nDan klik LINk untuk menampilkan LINK",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=b6faa883755d778161424e0b22ac5dbf&oe=5CDAA4F5",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "LOGIN",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": str(link)
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "LINK",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text="+str(link)
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "WIN10",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
                                 cl.sendFlex(to, data)
                                 #cl.sendMessage(msg.to,"Starting white true")
                                 #cl.sendMessage(msg.to,"Except")
                                 #cl.sendMessage(msg.to,str(link))
                                 Headers3.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers3).text)
                                 Headers3.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers3)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 cl.sendMessage(msg.to,str(res.authToken))
                                 cl.sendMessage(msg.to, "Jika ini bukan Anda, silakan ketuk tautan di bawah ini \n\nline://nv/connectedDevices/")
                                 
                        elif msg.text.lower().startswith("win"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=nama2)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Segera klik LOGIN untuk Login\nDan klik LINk untuk menampilkan LINK",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=b6faa883755d778161424e0b22ac5dbf&oe=5CDAA4F5",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "LOGIN",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": str(link)
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "LINK",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text="+str(link)
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "WIN10",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
                                 cl.sendFlex(to, data)
                                 #cl.sendMessage(msg.to,"Starting white true")
                                 #cl.sendMessage(msg.to,"Except")
                                 #cl.sendMessage(msg.to,str(link))
                                 Headers.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers).text)
                                 Headers.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 cl.sendMessage(msg.to,str(res.authToken))
                                 cl.sendMessage(msg.to, "Jika ini bukan Anda, silakan ketuk tautan di bawah ini \n\nline://nv/connectedDevices/")
                                 
                        elif msg.text.lower().startswith("ios"):
                             separate = msg.text.split(" ")
                             jmlh = int(separate[1])
                             for x in range(jmlh):
                                 Headers5.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                 transport.setCustomHeaders(Headers5)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 qr = client.getAuthQrcode(keepLoggedIn=1, systemName=nama3)
                                 link = "line://au/q/" + qr.verifier
                                 print(link)
                                 data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Segera klik LOGIN untuk Login\nDan klik LINk untuk menampilkan LINK",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=b6faa883755d778161424e0b22ac5dbf&oe=5CDAA4F5",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "LOGIN",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": str(link)
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "LINK",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text="+str(link)
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "WIN10",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
                                 cl.sendFlex(to, data)
                                 #cl.sendMessage(msg.to,"Starting white true")
                                 #cl.sendMessage(msg.to,"Except")
                                 #cl.sendMessage(msg.to,str(link))
                                 Headers5.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                 json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers5).text)
                                 Headers5.update({'x-lpqs' : '/api/v4p/rs'})
                                 transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                 transport.setCustomHeaders(Headers5)
                                 protocol = TCompactProtocol.TCompactProtocol(transport)
                                 client = LineService.Client(protocol)
                                 req = LoginRequest()
                                 req.type = 1
                                 req.verifier = qr.verifier
                                 req.e2eeVersion = 1
                                 res = client.loginZ(req)
                                 print('\n')
                                 print(res.authToken)
                             else:
                                 cl.sendMessage(msg.to,str(res.authToken))
                                 cl.sendMessage(msg.to, "Jika ini bukan Anda, silakan ketuk tautan di bawah ini \n\nline://nv/connectedDevices/")
                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                sendTextTemplate4(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leavegrup "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    ginfo = cl.getGroup(group)
                                    gCreator = ginfo.creator.mid
                                    recky = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = 'Sorry mudik dullu\n\nsilahkan invite owner kami '
                                    reck = str(recky.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':recky.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan+zxc + "Next Mapir Lagi" 
                                    ki.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    ki.sendImageWithURL(group,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=u48c350911cde6604da051d9da06c5db7&oid=faadb1b4f3991376bdccbd5700545da6")
                                    ki.leaveGroup(group)
                                    kk.leaveGroup(group)
                                    kc.leaveGroup(group)
                                    km.leaveGroup(group)
                                    kb.leaveGroup(group)
                                    jk.leaveGroup(group)
                                    sw.leaveGroup(group)
                                    dz.leaveGroup(group)
                                except:
                                    cl.sendMessage(msg.to, "")
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ginfo = cl.getGroup(group)
                                gCreator = ginfo.creator.mid
                                reck = cl.getContact(gCreator)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = ' Sukses Leave Group \n Creator :  '
                                recky = str(reck.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':reck.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                ret_ += xpesan +zxc
                                ret_ += " Nama grup : {}".format(G.name)
                                ret_ += "\n Pendingan : {}".format(gPending)
                                ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                sendTextTemplate(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))								

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate(msg.to,"ð´FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                               warnanya1 = random.choice(warna1)
                               data = {
                                   "type": "flex",
                                   "altText": "{} MEMBAGIKAN SEMPAK BOLONG ".format(dzProfile.displayName),
                                   "contents": {
                                       "type": "bubble",
                                       "body": {
                                           "type": "box",
                                           "layout": "horizontal",
                                           "contents": [
                                             {
                                                 "type": "text",
                                                 "text": str("GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups"),
                                                 "wrap": True,
                                                 "color": "#0108E5",
                                                 "align": "center"
                                             }
                                         ]
                                     },
                                     "footer": {
                                         "type": "box",
                                         "layout": "vertical",
                                         "spacing": "sm",
                                         "contents": [{
                                             "type": "button",
                                             "style": "primary",
                                             "height": "sm",
                                             "color": warnanya1,
                                             "action": {
                                                 "type": "uri",
                                                 "label": "ADD MY LINE",
                                                 "uri": "Http://line.me/ti/p/~denjaka_inex"
                                                 }													
                                             },
                                         {
                                             "type": "spacer",
                                             "size": "sm",
                                         }],
                                         "flex": 0
                                       }
                                   }
                               }
                               cl.sendFlex(to, data)

                        elif text.startswith("Smule "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("-")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "DAFTAR OC\n"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n\nSelanjutnya ketik: smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                                sendTextTemplate(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "Judul Oc: "+str(b["title"])
                                    c += "\nPembuat: "+str(b["owner"]["handle"])
                                    c += "\nTotal like: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\nTotal comment: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\nStatus VIP: "+str(b["owner"]["is_vip"])
                                    c += "\nStatus Oc: "+str(b["message"])
                                    c += "\nCreated Oc: {}".format(b["created_at"][:10])
                                    c += "\nDidengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                    hasil = "Detail Record\n\n"+str(c)
                                    dl = str(b["cover_url"])
                                    cl.sendImageWithURL(msg.to,dl)
                                    sendTextTemplate(msg.to, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            sendTextTemplate(msg.to,"Type: Audio\n\nPlease wait for audio...")
                                            cl.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            sendTextTemplate(msg.to,"Type: Video\n\nPlease wait for video...")
                                            cl.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    sendTextTemplate(msg.to,"DONE BOSS Q")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE FROFILE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"Send Picture") 
                       
                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"Send your images...")          
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["SKfoto"][mid] = True
                                sendTextTemplate(msg.to,"Send picture")                                
#================BOT UPDATE NAME============#
                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE============#                                                          
                        elif cmd == "inex" or text.lower() == 'tag':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"ð´Botlistð´\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"ð´Adminlistð´\n\nð´Owner\n"+ma+"\nð´Admin\n"+mb+"\nð´Staff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                mg = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = ghost
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate(msg.to,"ð´SETTING PROTECT ð´\n\nðProqr :\n"+ma+"\nðProinvit:\n"+mb+"\nðProAntikicker:\n"+mc+"\nðProtect Cancel:\n"+md+"\nðProtect:\n"+me+"\nðProAll:\n"+mf+"\nðGhost:\n"+mg+"\n\nð´Protectlist %s Grup protectð´" %(str(len(protect["pqr"])+len(protect["pinv"])+len(protect["antijs"])+len(protectcancel)+len(protect["protect"])+len(protect["proall"])+len(ghost))))
#====================================================================                            
                        elif cmd == "skill":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "â full 99%"
                               else:sil = "â Low 0,20%"
                               if has1 == "OK":sil1 = "â full 90%"
                               else:sil1 = "â Low 0,3%"
                               sendTextTemplate(to, "Status:\n\nâKick : {} \nâInvite : {}".format(sil1,sil))

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, " Silahkan invite Ownernya ")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"Succes leave group " +h)
#====================================================================                            
                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate(msg.to, "âTime Responâ\n\n âGet Profile\n   %.10f\n âGet Contact\n   %.10f\n âGet Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "Prosess....")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "Time:\n{}".format(str(elapsed_time)))
                               
                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "x on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "x off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"+cctv['sidermem'][msg.to])
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========add img============# 
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"Send your images.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"Send your images.....")
                                              
                        elif cmd == "changedual":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                sendTextTemplate(msg.to,"Send Videonya...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                cl.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                sendTextTemplate(msg.to, "Send Gambarnya.....")
                                
                        elif cmd.startswith("addimg"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Silahkan kirim fotonya...")
                                else:
                                    cl.sendMessage(to, "Foto itu sudah dalam list")
                        elif cmd.startswith("dellimg "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   cl.sendMessage(to, "Foto itu tidak ada dalam list")

                        elif cmd == "listimage":
                                no = 0
                                ret_ = "Daftar Image\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} Images".format(str(len(images)))
                                sendTextTemplate(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Silahkan kirim video nya...")
                                else:
                                    cl.sendMessage(to, "video itu sudah dalam list")
                        elif cmd.startswith("dellvideo "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   cl.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   cl.sendMessage(to, "video itu tidak ada dalam list")

                        elif cmd == "listvideo":
                                no = 0
                                ret_ = "Daftar video\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} video".format(str(len(images)))
                                cl.sendMessage(to, ret_)
#=========== [ Add Audio] ============#
                        elif cmd.startswith("addmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim mp3 nya...") 
                                else:
                                    cl.sendMessage(to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Mp3 itu tidak ada dalam list") 
                        elif "login" in msg.text.lower():
                                lists = {"result": [{"name": "Chrome 1\n(CHROMEOS)",},{"name": "Ios 1\n(ISOPAD)",},{"name": "Win 1\n(DESKTOPWIN)",}]}
                                if lists["result"] != []:
                                        ret_ = []
                                        for fn in lists["result"]:
                                                if len(ret_) >= 20:
                                                    pass
                                                else:
                                                    ret_.append({
                                                            "title": "{}".format(fn["name"]),
                                                            "text": "ketik Sesuai ketikan di atas",
                                                            "actions": [
                                                                {
                                                                    "type": "uri",
                                                                    "label": "CREATOR",
                                                                    "uri": "http://line.me/ti/p/~denjaka_inex",
                                                                }
                                                            ]
                                                        }
                                                    )
                                        k = len(ret_)//10
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Tokenlist",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            cl.sendFlex(to, data)
                        elif cmd.startswith("musik"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                f = cl.sendAudioWithURL(to,e)
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#bfff00"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "INEX TEAM\n\nMP3\nSONG ALBUM",
            "size": "xs",
            "color": "#00FF33",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "sm",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://steemitimages.com/0x0/https://i.imgur.com/q7MivIi.gif",
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#660000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "URL",
                  "uri": e
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ORDER",
                  "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"
              }
          }]
      }]
  }
}
}
                                cl.sendFlex(to, data)
                                cl.sendAudioWithURL(to,e)
                            except Exception as error:
                                sendTextTemplate(to, "error\n" + str(error))
                                logError(error)

                        elif cmd.startswith("ytmp "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "header": {
                                                    "backgroundColor": "#0000FF"
                                                },
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#FF7F50",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=u67ae64c90c91af8d20d8edbef8281dd5"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "JUDUL",
                                                        "color": "#00BFFF",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#1E90FF",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#7B68EE",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Ytdl%20{}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                }, {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#191970",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp4",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        cl.sendFlex(to, data)

                        elif cmd.startswith("dj"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#bfff00"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text": hasil,
            "size": "sm",
            "margin": "none",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "regular",
            "type": "text"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": g,
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#660000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "JOOX",
                  "uri": e
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "PLAY DI BAWAH",
                  "uri": "http://line.me/ti/p/~denjaka_inex"
              }
          }]
      }]
  }
}
}
                                cl.sendFlex(to, data)
                                cl.sendAudioWithURL(to,e)
                            except Exception as error:
                                sendTextTemplate(to, "error\n" + str(error))
                                logError(error)

                        elif "youtube" in msg.text.lower():
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    data = {
                                        "type": "flex",
                                        "altText": "YOUTUBE",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#FFFFFF"
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgekIeIdfny8Bgr-WBIhhZgecUBZKyE89-u_SdB6Z2P-XNPdaVXhrSL1o",
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#C0C0C0"
          },
          {
            "text": "YOUTUBE\nVIDEOS\nLOADING.\nPLAY",
            "size": "sm",
            "color": "#000000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "text": "JUDUL\n " + vid.title + " ?",
            "size": "xs",
            "align": "center",
            "color": "#000000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Author : " + str(vid.author),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Duration : " + str(vid.duration),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Likes : " + str(vid.likes),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Rating : " + str(vid.rating),
                "size": "sm",
                "margin": "none",
                "color": "#6F00FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#800000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "YOUTUBE",
                  "uri": search_url
              }
          }]
      }]
  }
}
}
                                cl.sendFlex(to, data)
                                cl.sendVideoWithURL(msg.to, me)
                            except Exception as e:
                                sendTextTemplate(msg.to,str(e))
                        elif cmd == "listmp3":
                                no = 0
                                ret_ = "Daftar Lagu ?\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\nTotal {} Lagu".format(str(len(audios)))
                                cl.sendMessage(to, ret_)
 #=========== [ Add sticker] ============#                   
                        elif cmd.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim stickernya...") 
                                else:
                                    cl.sendMessage(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Sticker itu tidak ada dalam list") 
                                                   
                        elif cmd == "liststicker":
                                no = 0
                                ret_ = " Daftar Sticker \n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                sendTextTemplate(to, ret_)
#====================================================================   
                        elif 'sukaku ' in text.lower():
                           if msg._from in admin:
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(msg.to), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(msg.to), str(result), wait["comment"])
                                    sendTextTemplate(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    sendTextTemplate(msg.to, str(e))
                                 
                        elif cmd.startswith("tafsirquran "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        sendTextTemplate(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n"+data.findAll('p')[1].text
                                                    cl.sendMessage(to, str(ret))
                                                except:
                                                    cl.sendMessage(to, "Gagal mengambil data.")                                                       
                                                                                               
                        elif text.lower().startswith("!music "):
                            try:
                                search = text.lower().replace("!musik","")
                                r = requests.get("https://rest.farzain.com/api/joox.php?apikey=rambu&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "ã Hasil Musik ã\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                sendTextTemplate(msg.to, "Searching mp3 done..")
                            except Exception as error:
                            	sendTextTemplate(msg.to, "ã Result Error ã\n" + str(error))
                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                          
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("https://citldesign.herokuapp.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                cl.sendImageWithURL(msg.to, image)
                                cl.sendAudioWithURL(msg.to, url)
                                cl.sendVideoWithURL(msg.to, url)
                                
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)                            
                                                                
                        elif cmd.startswith("getmeme"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "Meme image list\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    cl.sendMessage(msg.to,hasil)
                                    sendMention(msg.to,"@!\nSilahkan pilih keinginan:\n\n[Cek meme]\ngetmeme | urutan\n\n[Create meme]\nmeme teks1|teks2|urutan",[sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        sendMention(msg.to, sender,"","\nfoto sedang diproses...")
                                        cl.sendMessage(msg.to,hasil)
                                        cl.sendImageWithURL(msg.to,gambar["url"])
                                    except Exception as e:
                                        cl.sendMessage(msg.to," "+str(e))
                        elif "meme" in text.lower():
          #                 if msg._from admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                    result = api.caption_image(meme, atas,bawah)
                                    sendMention(msg.to, msg._from,"","\nfoto sedang diproses...")
                                    cl.sendImageWithURL(msg.to,result["url"])
                                except Exception as e:
                                    cl.sendMessage(msg.to," "+str(e)) 
                                        
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                sendTextTemplate7(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                cl.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("lihat "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "ã Informasi CCTV ã\nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Untuk melihat wilayah lainnya, Ketik kode wilayah"
                                    sendTextTemplate(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                    sendTextTemplate(to, ret)
                                except:
                                    sendTextTemplate(to, "Data cctv tidak ditemukan!")
                                    
                        elif cmd.startswith("get-apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "ã Pencarian Aplikasi ã\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))
                                                
                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)
                                    
                        elif text.lower() == 'top kaskus':
                           if msg._from in admin:
                               r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                               data=r.text
                               data=json.loads(data)                                                                                                      
                               if data["hot_threads"] != []:
                                   no = 0
                                   hasil = "ã Kaskus Search ã\n"
                                   for news in data["hot_threads"]:
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n â¢ Deskripsi : " + str(news["detail"]) + "\nâ¢ Link: " + str(news["link"]) + "\n"
                                        hasil += "\n"
                                   cl.sendMessage(msg.to, str(hasil))
                                                           
                                                                                    
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                sendTextTemplate(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                                
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))
                        
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"Informasiâ¢\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)
                            
                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    dhenza = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "ã Clone Profile ã\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(dhenza.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dhenza.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    sendTextTemplate(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    sendTextTemplate(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "ã Restore Profile ã\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")
                                  
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")
                                    
                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = ki.findContactsByUserid(userid)
                                    ki.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                ki.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = ki.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    ki.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    ki.leaveGroup(grup.id)
                                                	    ki.sendText(to,"@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Wc ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wc ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "?Diaktifkan?\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate(msg.to, "?Dinonaktifkan?\n" + msgs)
                        elif 'Prourl ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Prourl ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "SKurl has been active"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Skurl telah active\n\ndi group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Skurl deactive\n\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Skurl has been deactive"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "Protect has been active"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect Active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "Proall has been active"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect all active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect all deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect all has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel has been active "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "skinvite has been active"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "skurl active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "skinvite deactive\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "skinvite has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'J ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'o':
                                  if msg.to in protect["antijs"]:
                                       msgs = "Protectjs has been active"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti kicker \n\naktif di group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "active\n\n" + msgs)
                              elif spl == 'f':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti kicker off\n\ndi group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti kicker off "
                                    cl.sendMessage(msg.to, "nonactive\n" + msgs)
                                    
                        elif 'G ' in msg.text:
                          if msg._from in admin:
                             spl = msg.text.replace('Ghost ','')
                             if spl == 'o':
                                 if msg.to in ghost:
                                      msgs = "Ghost sudah aktif"
                                 else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                 cl.sendMessage(msg.to, "Status:\n" + msgs)
                             elif spl == 'f':
                                   if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                   else:
                                        msgs = "Ghost Sudah Tidak Aktif"
                                   cl.sendMessage(msg.to, "Status:\n" + msgs)

                        elif 'P ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('P ','')
                              if spl == 'o':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect on \n\ndi group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "."
                                  cl.sendMessage(msg.to, "Assalamualaikum" + msgs)
                              elif spl == 'f':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Succes Nonactive Allpro\n\nIn group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ".."
                                    sendTextTemplate(msg.to, "Assalamualaikum\n" + msgs)

#===========KICKOUT============#       
                        elif ("Sory " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Kebo" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Kebo","")                                 
                                 gs = cl.getGroup(msg.to)
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"...")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   denjaka= [cl]
                                                   kicker=random.choice(denjaka)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "Limit bos")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                      
                           elif "Invite. " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
#===========ADMIN ADD============
                        elif ("Staff:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Bot:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif ("Adminexpl:on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel admin")
                                       except:
                                           pass

                        elif ("Staffexpl:on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel staff")
                                       except:
                                           pass

                        elif ("Botexpl:on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel Bots")
                                       except:
                                           pass
  #====================================#                                         
                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                settings["autoJoin"] = True
                                sendTextTemplate(to, "Berhasil mengaktifkan auto join")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                settings["autoJoin"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan auto join")
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                sendTextTemplate(to, "Berhasil mengaktifkan auto Block")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan auto Block")
                        elif cmd == "autoleave on":
                            if msg._from in owner:	
                                settings["autoLeave"] = True
                                sendTextTemplate(to, "Berhasil mengaktifkan auto leave")
                        elif cmd == "autoleave off":
                            if msg._from in owner:
                                settings["autoLeave"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan auto leave")
                        elif cmd == "autojointicket on":
                        	if msg._from in owner:
                                 settings["autoJoinTicket"] = True
                                 sendTextTemplate(to, "Berhasil mengaktifkan auto join by ticket")
                        elif cmd == "autojointicket off":
                           if msg._from in owner:
                                 settings["autoJoinTicket"] = False
                                 sendTextTemplate(to, "Berhasil menonaktifkan auto join by ticket")                        
                        elif cmd == "tl on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 sendTextTemplate(msg.to, "Berhasil mengaktifkan check details post")
                        elif cmd == "tl off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                sendTextTemplate(msg.to, "Berhasil menonaktifkan check details post")                                   
#==================================#
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                sendTextTemplate(msg.to,"Send Contact")

                        elif cmd == "adminexpl:on" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "staffexpl:on" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "botexpl:on" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"Prosess...")
                                sendTextTemplate(msg.to,"Refresh done ð¯")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                     
                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                sendTextTemplate(msg.to, "Send Contact to spam grup..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                sendTextTemplate(msg.to, "Send Contact to send grup Off..")
                                
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "r1 on" or text.lower() == 'respon1 on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"Auto respon diaktifkan")

                        elif cmd == "pm on" or text.lower() == 'respon1 on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["arespon"] = True
                                sendTextTemplate(msg.to,"Auto respon pm diaktifkan")

                        elif cmd == "pm off" or text.lower() == 'respon1 off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["arespon"] = False
                                sendTextTemplate(msg.to,"Auto respon pm dinonaktifkan")

                        elif cmd == "r1 off" or text.lower() == 'respon1 off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "r2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention2"] = True
                                sendTextTemplate(msg.to,"Auto respon 2 diaktifkan")

                        elif cmd == "r2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention2"] = False
                                sendTextTemplate(msg.to,"Auto respon 2 dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"Notag dinonaktifkan")
                                
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = True
                                sendTextTemplate(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = False
                                sendTextTemplate(msg.to,"detect unsend dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, "ã Status Invite ã\nUser ", "\nSend a contact to invite,\nIf done -> Invite off")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, "ã Status Invite ã\nUser ", " \nInvited has been disabled")
                                
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "ã Status Timeline ã\nUser ", "\nSend a post,\nIf done -> Timeline off")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "ã Status Timeline ã\nUser ", " \nDeteksi timeline dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif cmd == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))
                                

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotalã%sãTalkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == 'clearban':
                            if msg._from in owner or msg._from in admin:
                                wait["blacklist"] = {}
                                ragets = cl.getContacts(wait["blacklist"])
                                mc = "Ûâ¢ã%iãPenjahat" % len(ragets)
                                sendTextTemplate(msg.to,"Succes Clearban " +mc)
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              random.choice(ABC).sendMessage(msg.to, "like done")
                              
                        elif "Pmcast: " in msg.text:
                            bctxt = msg.text.replace("Pmcast: ", "")
                            a = cl.getAllContactIds()
                            line.sendMessage(to, "Sukses broadcast ke "+str(len(a))+" teman")
                            for manusia in a:
                                C = cl.getContact(mid)
                                mids = [C.mid]
                                text = "BROADCAST FRIEND:\n\n{}\n\nBROADCASTED BY: @!".format(str(bctxt))
                                sendMentionV2(manusia, text, mids)
                                cl.sendMessage(to, (bctxt))
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "?Pesan Msg?\nPesan Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "?Welcome Msg?\nWelcome Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set r1: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r1: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "?Respon Msg?\nRespon Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set r2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate(msg.to, "?Respon Msg?\nRespon Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set pm: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pm: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon ke pm")
                              else:
                                  wait["Responpm"] = spl
                                  sendTextTemplate(msg.to, "?Respon pm?\nRespon pm diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "?Spam Msg?\nSpam Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "?Sider Msg?\nSider Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Pesan Msg?\nPesan Msg mu :\n\n? " + str(wait["message"]) + " ?")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Welcome Msg?\nWelcome Msg mu :\n\n? " + str(wait["welcome"]) + " ?")

                        elif text.lower() == "cek r1":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Respon Msg?\nRespon Msg mu :\n\n? " + str(wait["Respontag"]) + " ?")

                        elif text.lower() == "cek r2":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Respon Msg?\nRespon Msg mu :\n\n? " + str(wait["Respontag2"]) + " ?")

                        elif text.lower() == "cek pm":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Respon pm?\nRespon pm mu :\n\n? " + str(wait["Responpm"]) + " ?")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Spam Msg?\nSpam Msg mu :\n\n? " + str(Setmain["RAmessage1"]) + " ?")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "?Sider Msg?\nSider Msg mu :\n\n? " + str(wait["mention"]) + " ?")
#=================================[ STAMINA BOT ]================================================                               
                        #=============================[ JOIN TICKET ]============+=============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Pá´sá´á´á´É´ SÉªÊá´É´á´á´·á¶¦Ë¡Ë¡áµÊ³ É¢á´ : %s" % str(group.name))
                                     group1 = cl.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
