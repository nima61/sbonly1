# -*- coding: utf-8 -*-
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
from thrift.protocol import TCompactProtocol
from thrift import transport, protocol, server
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from googletrans import Translator
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient
#========================================================================
_session = requests.session()
botStart = time.time()
print("LOGIN                        INDUK")
cl = LINE("")
cl.log("Auth Token : " + str(cl.authToken))
print("\nɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2 ᴘʀᴏᴛᴇᴄᴛ \n__________________________")

"""
ɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2 ᴘʀᴏᴛᴇᴄᴛ
"""
print("login success")
oepoll = OEPoll(cl)
call = cl

creator = [""]
owner = [""]
admin = ["u541b8e613bee702f33693ea38e329bca"]
staff = ["u541b8e613bee702f33693ea38e329bca"]
#🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤
mid = cl.getProfile().mid
KAC = [cl]
ABC = [cl]
Bots = [mid]
Denjaka = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
msg_dict = {}
msg_dict1 = {}
offbot = []
welcome = []
#🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•INEX KILLERS➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤
nama1 = 'InexBots'
Headers3 = {
        'User-Agent': "CHROMEOS\t9.0.3Bot-Eater\t17.09",
        'X-Line-Application': "CHROMEOS 1.7.14 BotEater x64",
        "x-lal": "ja-US_US",
    }

#🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•INEX KILLERS FAMS➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤
settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
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
    "stickerset": {
        "STKID":"",
        "STKVER":"",
        "STKPKGID":"",
        "status": False
            },
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
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "Timeline":False,
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "denjaka":{},
    "likeOn": True,
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
    "autoJoin":True,
    "autoAdd":True,
    "autoCancel":{"on":True, "members":1},
    "autoLeave":False,
    "autoLeave1":False,
    "detectMention":False,
    "detectMention2":False,
    "arespon":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "link1": "Chrome 1",
    "link2": "Ios 1",
    "link3": "Win 1",
    "autoJoinMessage": "ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴋᴀᴋᴀ ᴀᴛᴀs ᴜɴᴅᴀɴɢᴀɴ ɢʀᴜᴘɴʏᴀ.",
    "comment1": "ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ⊶ ɪɴᴇxʙᴏᴛs ⊷ \nline.me/ti/p/Lgx8gKrUYn",
    "comment2": "╭━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║   ❀     BY BOT : INEXBOTS    ❀\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  ❀ LIKE DONE \n┃ ║  ❀ COMMENT DONE \n┃ ║  ❀ INEXBOTS_TEAM\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  http://line.me/ti/p/Lgx8gKrUYn\n┃ ╚══════════════════━━━━╯\n╰━━━━━━━━━━━━━━━━━━━━━━━━",
    "mention":"ᴋᴀʟᴏ ɴɢɪɴᴛɪᴘ ᴛᴇʀᴜs ᴅᴀᴘᴇᴛ ɢᴇʟᴀs ᴘᴇᴄᴀʜ ᴅɪ ᴋᴇᴘᴀʟᴀ...",
    "Respontag":"ᴊᴀɴɢᴀɴ ᴛᴀɢ ʙᴀᴇ ᴋᴀᴋ,,, ɴɢᴏᴍᴏɴɢ ᴀᴊᴀ ᴋᴀʟᴏ ᴄɪɴᴛᴀ ᴀᴋᴜ ᴍᴀʜ.",
    "Respontag2":"ᴊᴀɴɢᴀɴ ᴛᴀɢ ʙᴀᴇ ᴋᴀᴋ,,, ɴɢᴏᴍᴏɴɢ ᴀᴊᴀ ᴋᴀʟᴏ ᴄɪɴᴛᴀ ᴀᴋᴜ ᴍᴀʜ.",
    "Responpm":"maaf,,, Ada apa kak tag saya di grup!",
    "welcome":"⚔🅆🄴🄻🄲🄾🄼🄴⚔/n ✎﹏ᑎIᗰᗩ ᗰᗩ᙭ ᗷOT★彡★彡",
    "commentPost":"ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ⊶ ɪɴᴇxʙᴏᴛs ⊷ \nline.me/ti/p/Lgx8gKrUYn",
    "message":"тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ ⊶ ɪɴᴇxʙᴏᴛs ⊷ \nline.me/ti/p/Lgx8gKrUYn"
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "protect":[]
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

jakaProfile = cl.getProfile()
myProfile["displayName"] = jakaProfile.displayName
myProfile["statusMessage"] = jakaProfile.statusMessage
myProfile["pictureStatus"] = jakaProfile.pictureStatus

imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
plates = codecs.open("template.json","r","utf-8")
movieOp = codecs.open("movie.json","r","utf-8")
mengirim = json.load(movieOp)
plate = json.load(plates)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
cont = cl.getContact(mid)
Import_Server = plate["Server_BUG"]
for Allbots in ABC:
    for LineX in Import_Server:
        try:
            Allbots.findAndAddContactsByMid(LineX)
        except:pass
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

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
Devert = "My name is "+cont.displayName+" use your bot script Templates\n\nhttps://github.com/InexBots"
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

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
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

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
                        cl.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
Extr = cl.getContact(Import_Server).displayName
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    cl.sendMessage(to, '', contentMetadata, 7)

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

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
extras = Extr+"\n"
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict1[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict1[data]
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

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

def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots \n"
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
def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@InexBots "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@InexBots\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚🇮🇷•➤[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚🇮🇷•➤[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "🇮🇷•➤Total User🇮🇷•➤「{}」\n🇮🇷•➤Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@InexBots\n"
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
                    no = "\n╚🇮🇷•➤[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚🇮🇷•➤[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        image = 'http://dl.profile.line.naver.jp'+contact
        cl.sendImageWithURL(op.param2, image)
        cl.sendMessage(to, None, contentMetadata={"STKID":"51626528","STKPKGID":"11538","STKVER":"1"}, contentType=7)
    except Exception as error:
        cl.sendMessage(to, None, contentMetadata={"STKID":"51626528","STKPKGID":"11538","STKVER":"1"}, contentType=7)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "⚀🅽🅸MA BOT ⚀"
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@InexBots\n"
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
                    no = "\n╚🇮🇷•➤[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚🇮🇷•➤[ Success ]"
        #cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        data = {
            "type": "flex",
            "altText": "⚀🅽🅸MA BOT ⚀☪▄︻",
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
                   "text": "",
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
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
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
            mention = "@InexBots\n"
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
                    no = "\n╚🇮🇷•➤[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚🇮🇷•➤[ Success ]"
    except Exception as error:
        cl.sendMessage(to)
#TAGALL LUAR ROOM BAHAN

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━━━━━━━━━━━━━━━━━━━━╮\n├ 🇮🇷 MENTION [ {} ] MEMBER\n├━━━━━━━━━━━━━━━━━━━━\n├[1.]🇮🇷".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@InexBots\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├[%i.]🇮🇷 " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚🇮🇷•➤[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚🇮🇷•➤[ Success ]"
        cl.sendMessage(to, textx+"╰━━━━━━━━━━━━━━━━━━━━╯", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
def sendMentionV3(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots "
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

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots "
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

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@InexBots \n"
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
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n⏩ Group : "+str(len(gid))+"\n⏩ Teman : "+str(len(teman))+"\n⏩ Expired : In "+hari+"\n⏩ Version : ANTIJS2\n⏩ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n⏩ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~mdfs99"
           }                                                
 }
]
                          }
                      }
    cl.sendFlex(to, data)

def sendBcast(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "Kickall ",  #.format(dzProfile.displayName),
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
                   "text": "⚚ΠIMΔ MΔX βΩT⚚",
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": text,
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
    cl.sendFlex(group, data)

def sendTextTemplate13(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "⚚ΠIMΔ MΔX βΩT⚚",
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
            "text": "    ⚚ΠIMΔ MΔX βΩT⚚",
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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)

def sendBradcast(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "Kickall ",  #.format(dzProfile.displayName),
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
                   "text": "⚚ΠIMΔ MΔX βΩT⚚",
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": text,
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
    cl.sendFlex(group, data)

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
          "uri": "http://line.me/ti/p/Lgx8gKrUYn"
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
        "text": "⚚ΠIMΔ MΔX βΩT⚚",
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
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
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
                "altText": "⚚ΠIMΔ MΔX βΩT⚚",
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

 
def sendTextTemplate3(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠",
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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
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
                                      "uri": "http://line.me/ti/p/Lgx8gKrUYn"
           }                                                
 }
]
                          }
                      }
    cl.sendFlex(to, data)
def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} lagi kojom dulu".format(cl.getProfile().displayName),
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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
def sendFoto(to, images):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = msg.to
    data = {
                                                "type": "template",
                                                "altText": "{} tukang unsend".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(msg_dict[msg_id]["data"])),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                                 }                                                
                       }
                      ]
                                                }
                                            }
    cl.sendFlex(to, data)
def sendTextTemplate(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
        "type": "flex",
        "altText": "⚚ΠIMΔ MΔX βΩT⚚",
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
def sendAutolike(to,text):
    data = {
        "type": "template",
        "altText": "⚚ΠIMΔ MΔX βΩT⚚",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                    "title": "{}".format(cl.getContact(op.param2).displayName),
                    "text": text,
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                        }
                      ]
                    }
                  ]
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
                                "altText": "{} ⚚ΠIMΔ MΔX βΩT⚚".format(jakaProfile.displayName),
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
            "text": "BIO DATA\n❀ NAMA: {}".format(cl.getContact(op.param2).displayName)+"\n❀ GROUP: {}".format(str(len(grouplist)))+"\n❀ FRIEND : {}".format(str(len(contactlist)))+"\n❀ FAFORITE : {}".format(str(len(favoritelist)))+"\n❀ BLOCKED : {}".format(str(len(blockedlist)))+"\nBio: {}".format(cl.getContact(op.param2).statusMessage),
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
              }
          }]
      }]
  }
}
}
    cl.sendFlex(to, data)
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = extras + "╔━☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠━━╗\n" + \
                  "╠🇮🇷•➤" + key + "🇮🇷•➤MENU HELP•🇮🇷\n" + \
                  "╠🇮🇷•➤" + key + "Me\n" + \
                  "╠🇮🇷•➤" + key + "Tokenlist\n" + \
                  "╠🇮🇷•➤" + key + "Memberpict\n" + \
                  "╠🇮🇷•➤" + key + "Mid「@」\n" + \
                  "╠🇮🇷•➤" + key + "Getmid「@」\n" + \
                  "╠🇮🇷•➤" + key + "Info「@」\n" + \
                  "╠🇮🇷•➤" + key + "Kick「@」\n" + \
                  "╠🇮🇷•➤" + key + "Kibar\n" + \
                  "╠🇮🇷•➤" + key + "Status\n" + \
                  "╠🇮🇷•➤" + key + "About\n" + \
                  "╠🇮🇷•➤" + key + "Restart\n" + \
                  "╠🇮🇷•➤" + key + "Runtime\n" + \
                  "╠🇮🇷•➤" + key + "Creator\n" + \
                  "╠🇮🇷•➤" + key + "Speed/Sp\n" + \
                  "╠🇮🇷•➤" + key + "Sprespon\n" + \
                  "╠🇮🇷•➤" + key + "Tag/Inex\n" + \
                  "╠🇮🇷•➤" + key + "Tag room:「No grup」\n" + \
                  "╠🇮🇷•➤" + key + "Ginfo\n" + \
                  "╠🇮🇷•➤" + key + "Open\n" + \
                  "╠🇮🇷•➤" + key + "Close\n" + \
                  "╠🇮🇷•➤" + key + "Gurl\n" + \
                  "╠🇮🇷•➤" + key + "Gruplist\n" + \
                  "╠🇮🇷•➤" + key + "Infogrup「angka」\n" + \
                  "╠🇮🇷•➤" + key + "Infomem「angka」\n" + \
                  "╠🇮🇷•➤" + key + "Remove chat\n" + \
                  "╠🇮🇷•➤" + key + "Lurking「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Lurkers\n" + \
                  "╠🇮🇷•➤" + key + "Sider「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Myup\n" + \
                  "╠🇮🇷•➤" + key + "Updategrup\n" + \
                  "╠🇮🇷•➤" + key + "Bcast: / Gcast:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Pmcast:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Setkey「New Key」\n" + \
                  "╠🇮🇷•➤" + key + "Mykey\n" + \
                  "╠🇮🇷•➤" + key + "Resetkey\n" + \
                  "╠🇮🇷•➤" + key + "🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷\n" + \
                  "╠🇮🇷•➤" + key + "Movie\n" + \
                  "╠🇮🇷•➤" + key + "ID line:「Id Line nya」\n" + \
                  "╠🇮🇷•➤" + key + "Sholat:「Nama Kota」\n" + \
                  "╠🇮🇷•➤" + key + "Cuaca:「Nama Kota」\n" + \
                  "╠🇮🇷•➤" + key + "Lokasi:「Nama Kota」\n" + \
                  "╠🇮🇷•➤" + key + "Musik「Judul Lagu」\n" + \
                  "╠🇮🇷•➤" + key + "Lirik:「Judul Lagu」\n" + \
                  "╠🇮🇷•➤" + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠🇮🇷•➤" + key + "Ytmp「Judul Video」\n" + \
                  "╠🇮🇷•➤" + key + "Profileig:「Nama IG」\n" + \
                  "╠🇮🇷•➤" + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠🇮🇷•➤" + key + "Jumlah:「angka」\n" + \
                  "╠🇮🇷•➤" + key + "Spamtag「@」\n" + \
                  "╠🇮🇷•➤" + key + "Spamcall:「jumlahnya」\n" + \
                  "╠🇮🇷•➤" + key + "Spamcall\n" + \
                  "╠🇮🇷•➤" + key + "Notag「on/off」\n" + \
                  "╚━━⚀🅽🅸🅼🅰 🅼🅰🆇⚀━━╝"
    return helpMessage

def helpa():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessagea = extras + "╔☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠━╗\n" + \
                  "╠🇮🇷•➤" + key + "🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷🇮🇷\n" + \
                  "╠🇮🇷•➤" + key + "Sticker「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "R1「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "R2「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "PM「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Contact「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Autojoin「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Autoadd「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Autoblock「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Wc「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Autoleave「on/off」\n" + \
                  "╠🇮🇷•➤" + key + "Admin:on\n" + \
                  "╠🇮🇷•➤" + key + "Admin:repeat\n" + \
                  "╠🇮🇷•➤" + key + "Staff:on\n" + \
                  "╠🇮🇷•➤" + key + "Staff:repeat\n" + \
                  "╠🇮🇷•➤" + key + "Bot:on\n" + \
                  "╠🇮🇷•➤" + key + "Bot:repeat\n" + \
                  "╠🇮🇷•➤" + key + "Adminadd「@」\n" + \
                  "╠🇮🇷•➤" + key + "Admindell「@」\n" + \
                  "╠🇮🇷•➤" + key + "Staffadd「@」\n" + \
                  "╠🇮🇷•➤" + key + "Staffdell「@」\n" + \
                  "╠🇮🇷•➤" + key + "Botadd「@」\n" + \
                  "╠🇮🇷•➤" + key + "Botdell「@」\n" + \
                  "╠🇮🇷•➤" + key + "Listadmin\n" + \
                  "╚━⚀🅽🅸🅼🅰 🅼🅰🆇⚀═━━╝"
    return helpMessagea

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = extras + "╔☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠━╗\n" + \
                  "╠🇮🇷•➤" + key + "🇮🇷•HELP BOT•🇮🇷\n" + \
                  "╠🇮🇷•➤" + key + "Blc\n" + \
                  "╠🇮🇷•➤" + key + "Ban:on\n" + \
                  "╠🇮🇷•➤" + key + "Unban:on\n" + \
                  "╠🇮🇷•➤" + key + "Ban「@」\n" + \
                  "╠🇮🇷•➤" + key + "Unban「@」\n" + \
                  "╠🇮🇷•➤" + key + "Talkban「@」\n" + \
                  "╠🇮🇷•➤" + key + "Untalkban「@」\n" + \
                  "╠🇮🇷•➤" + key + "Talkban:on\n" + \
                  "╠🇮🇷•➤" + key + "Untalkban:on\n" + \
                  "╠🇮🇷•➤" + key + "Banlist\n" + \
                  "╠🇮🇷•➤" + key + "Talkbanlist\n" + \
                  "╠🇮🇷•➤" + key + "Clearban\n" + \
                  "╠🇮🇷•➤" + key + "Refresh\n" + \
                  "╠🇮🇷•➤" + key + "Cek allrespon\n" + \
                  "╠🇮🇷•➤" + key + "Cek sider\n" + \
                  "╠🇮🇷•➤" + key + "Cek spam\n" + \
                  "╠🇮🇷•➤" + key + "Cek pesan \n" + \
                  "╠🇮🇷•➤" + key + "Cek respon \n" + \
                  "╠🇮🇷•➤" + key + "Cek welcome\n" + \
                  "╠🇮🇷•➤" + key + "Set sider:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set spam:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set pesan:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set r1:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set r2:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set pm:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set Autojoin:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Set welcome:「Text」\n" + \
                  "╠🇮🇷•➤" + key + "Myname:「Nama」\n" + \
                  "╠🇮🇷•➤" + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠🇮🇷•➤" + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "╚━━━━⚀🅽🅸🅼🅰 🅼🅰🆇⚀━━━╝"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return    
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendAutolike(op.param1,"Maaf fams "+str(ginfo.name)+" saya pamit lagi ya.")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hi fams "+str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        group = cl.getGroup(op.param1)
                        warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                        warnanya1 = random.choice(warna1)
                        data = {
                                "type": "flex",
                                "altText": "☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠",
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
            "text": str(wait["autoJoinMessage"]),
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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
              }
          }]
      }]
  }
}
}
                        cl.sendFlex(op.param1, data)
# EDIT
        if op.type == 19:
            if op.param3 in admin or op.param3 in owner or op.param3 in staff:
                if op.param2 in admin or op.param2 in owner or op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        cl.log("bot limit")
                        
                        
                        
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
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
                return

        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                #welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
            "type": "flex",
            "altText": "⚀🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃⚀",
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
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
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
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "⚀🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃⚀",
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
                    except:
                        pass
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    cl.findAndAddContactsByMid(op.param1)
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

#🇮🇷•➤🇮🇷•➤🇮🇷•➤RKF🇮🇷•➤🇮🇷•➤🇮🇷•➤🇮🇷•➤
            if admin in op.param3:
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
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
                return
            if staff in op.param3:
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
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
                return
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
                            ret_ = "🇮🇷•➤ Detail Postingan🇮🇷•➤"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n🇮🇷•➤  Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n🇮🇷•➤  Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n🇮🇷•➤  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n🇮🇷•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n🇮🇷•➤  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n🇮🇷•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n🇮🇷•➤  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n🇮🇷•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n🇮🇷•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n🇮🇷•➤  Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n🇮🇷•➤  Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            sendTextTemplate1(to, str(ret_))
                            cl.likePost(url[25:58], url[66:], likeType=1001)
                            cl.createComment(url[25:58], url[66:], wait["comment"])
                            sendAutolike(to, "Like done")

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
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
                            cctv['sidermem'][op.param1] += "\n• " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    sendCyduk(op.param1, wait["mention"])
                                else:
                                    sendTextTemplate44(op.param1, "⚄آنــــــــلاین شـــد⚅ " +  nick[1] + "\n☠🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃☠")
                            else:
                                sendTextTemplate7(op.param1, "☸آنـــــــلاین شــد⚁ " + "☞ " + Name + " ☜" + "\n⚀🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃⚀")
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 5:
            if settings['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(op.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, op.param1)
                    wait["Blacklist"][op.param2] = True
                except Exception as e:
                	print (e)
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["arespon"] == True: 
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           contact = cl.getContact(msg._from)
                           sendMentionV3(sender, "Kak @!  "+ wait["Responpm"], [sender])
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
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
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
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                           warnanya1 = random.choice(warna1)
                           data = {
        "type": "template",
        "altText": "Mention plates",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
                    "title": "{}".format(cl.getContact(msg._from).displayName),
                    "text": str(wait["Respontag"]),
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                    "title": "ɪɴᴇxʙᴏᴛs",
                    "text": "🇮🇷•➤ ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nᴠᴇʀ.8.14.2 ᴘʀᴏᴛᴇᴄᴛ",
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
                           cl.sendFlex(to, data)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                           cl.sendMessage(msg.to,  wait["Respontag2"])
                           #cl.sendMessage(to, None, contentMetadata={"STKID":"50726910","STKPKGID":"11475","STKVER":"2"}, contentType=7)
                           data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-5wFNSCJlYWI/WRxHdiXJl0I/AAAAAAAHlIg/k9KvZJCkpfIslWlgqyxtjR5jzBEvEgA6QCLcB/s1600/AW429388_04.gif",
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
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
#===========================
        if op.type == 26 or op.type == 26:
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
                   ret_ = "╭━━━━══════════════\n"
                   ret_ = "\n┣🇮🇷•➤「 Sticker Info 」"
                   ret_ += "\n┣🇮🇷•➤ Sticker ID : {}".format(stk_id)
                   ret_ += "\n┣🇮🇷•➤ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n┣🇮🇷•➤ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n┣🇮🇷•➤ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n╰━━━━══════════════\n"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}                 
            if msg.contentType == 0:
                if text is None:
                   return
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                jaka = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = "╭━━━━══════════════\n┣🇮🇷•➤「 Gambar Dihapus 」\n┣🇮🇷•➤ Pengirim"
                                ret_ = "\n┣🇮🇷•➤ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣🇮🇷•➤ Waktu Dikirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n╰━━━━══════════════"
                                ry = str(jaka.displayName)
                                pesan = ''
                                pesan2 = pesan+"{} \n".format(str(jaka.displayName))
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':jaka.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                sendTextTemplate3(at, text)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                jaka = cl.getContact(msg_dict[msg_id]["from"])             
                                ret_ = "╭━━━━══════════════"
                                ret_ += "\n┣🇮🇷•➤ Pesan Dihapus"
                                ret_ += "\n┣🇮🇷•➤  Pengirim : {}".format(str(jaka.displayName))
                                ret_ += "\n┣🇮🇷•➤  Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣🇮🇷•➤  Waktu Dikirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n┣🇮🇷•➤  Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰━━━━══════════════"
                                sendTextTemplate3(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                jaka = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ = "╭━━━━══════════════"
                                ret_ += "\n┣🇮🇷•➤ Pengirim : {}".format(str(jaka.displayName))
                                ret_ += "\n┣🇮🇷•➤ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n┣🇮🇷•➤ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n┣🇮🇷•➤ {}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰━━━━══════════════"
                                sendTextTemplate3(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)     
#===============
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
                                    ret_ = "🇮🇷•Details Post•🇮🇷"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\n🇮🇷•➤Penulis•➤•➤ : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n🇮🇷•➤Penulis•➤•➤ : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n🇮🇷URL🇮🇷•➤ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n🇮🇷•Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n🇮🇷•Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n🇮🇷•Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n🇮🇷•Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n🇮🇷•Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n🇮🇷•Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n🇮🇷•Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n🇮🇷•Tulisan :\n{}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n🇮🇷•Finish"
                                    sendTextTemplate1(to, str(ret_))
                                except:
                                    sendTextTemplate1(to, "Post tidak valid")
            except Exception as error:
                logError(error)
#=============================[[
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(msg.to,"🇮🇷•➤Nama : " + msg.contentMetadata["displayName"] + "\n🇮🇷•➤MID : " + msg.contentMetadata["mid"] + "\n🇮🇷•➤Status Msg : " + contact.statusMessage + "\n🇮🇷•➤Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"Contact itu bukan anggota bot Dpk")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path)
                     sendTextTemplate(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help" or cmd == "Help":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendMessage(Import_Server,Devert)
                            cl.sendFlex(to, plate["helpgrup"])

                        if cmd == "helpmedia":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate3(msg.to, str(helpMessage))

                        if cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessagea = helpa()
                               sendTextTemplate3(msg.to, str(helpMessagea))
                                                                                       
                        if cmd == "on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "Selfbot dinonaktifkan")

                        if cmd == "movie":
                            cl.sendFlex(to, mengirim["movie"])

                        elif cmd == "galeri" or cmd == "Galeri":
                            cl.sendFlex(to, plate["galery"])

                        elif text.lower() == 'sepi':
                            sendTextTemplate3(to, "╔════╗╔════\n║▓▓▓█║║▓▓▓█\n║▓▓▓█║║▓▓▓█\n║▓▓▓█╚╝▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█║║▓▓▓█\n║▓▓▓█║║▓▓▓█\n╚╦═══╝╚═══\n╔╝▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█╚╝▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█║║▓▓▓█\n╠════╝╚══\n║▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓█╚╗▓▓▓█\n║▓▓▓█╔╝▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓█\n╩╦══════\n═║▓▓▓▓▓█\n═║▓▓▓▓▓█\n═╚╗▓▓▓█\n══║▓▓▓█\n══║▓▓▓█\n═╔╝▓▓▓█\n═║▓▓▓▓▓█\n═║▓▓▓▓▓█\n╔╩══════\n║▓▓▓▓▓▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓█╠═▓▓▓█\n║▓▓▓█║▓▓▓█\n║▓▓▓▓▓▓▓█\n║▓▓▓█▓▓▓█\n║▓▓▓█║▓▓▓█\n║▓▓▓█╠╗▓▓▓█\n╚════╝╚═══")

                        elif text.lower() == 'price':
                            cl.sendFlex(to, plate["pricelist"])

                        elif cmd == "listapp":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            cl.sendFlex(to, plate["listapp1"])
                            cl.sendFlex(to, plate["listapp2"])

                        elif cmd == "memberpict":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            kontak = cl.getGroup(to)
                            group = kontak.members
                            picall = []
                            for ids in group:
                              if len(picall) >= 400:
                                pass
                              else:
                                picall.append({
                                  "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                  "action": {
                                    "type": "uri",
                                    "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                                   }
                                 }
                               )
                            k = len(picall)//10
                            for aa in range(k+1):
                              data = {
                                "type": "template",
                                "altText": "{} Membagikan janda geratis".format(jakaProfile.displayName),
                                "template": {
                                  "type": "image_carousel",
                                  "columns": picall[aa*10 : (aa+1)*10]
                                }
                              }
                              cl.sendFlex(to, data)

                        elif cmd == "key":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sendTextTemplate13(msg.to, str(helpMessage1))

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  sendTextTemplate(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")

                        elif cmd == "memberlist":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                              group = cl.getGroup(to)
                              ret_ = "╭━━━══[ Member List ]"
                              no = 0 + 1
                              for mem in group.members:
                                ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                                no += 1
                              ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                              sendTextTemplate3(msg.to, ret_)
                        elif cmd == "pendinglist":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                              group = cl.getGroup(to)
                              ret_ = "╭━━━══[ Pending List ]"
                              no = 0 + 1
                              if group.invitee is None or group.invitee == []:
                                sendTextTemplate(to, "Tidak ada pendingan")
                                return
                              else:
                                for pen in group.invitee:
                                  ret_ += "\n├ 🇮🇷 {}. {}".format(str(no), str(pen.displayName))
                                  no += 1
                                ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                sendTextTemplate3(msg.to, ret_)

                        elif cmd == "me":
                              h = cl.getContact(msg._from)
                              cover = cl.getProfileCoverURL(msg._from)
                              cl.reissueUserTicket()
                              data = {
                             "type": "flex",
                             "altText": "{} Berak di celana".format(str(h.displayName)),
                             "contents": {
                              "type": "bubble",
                              "styles": {
                                "header": {
                                  "backgroundColor": "#000000",
                                },
                                "body": {
                                  "backgroundColor": "#000000",
                                  "separator": True,
                                  "separatorColor": "#000000"
                                },
                                "footer": {
                                  "backgroundColor": "#000000",
                                  "separator": True
                                }
                              },
                              "hero": {
                                "type": "image",
                                "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                                },
                               "contents": [
                               {
                                 "type": "text",
                                 "text": "⚀🅽🅸🅼🅰 🅼🅰🆇⚀",
                                 "size": "md",
                                 "color": "#0000FF"
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
                                         "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                         "size": "5xl"
                                       },
                                       {
                                         "type": "text",
                                         "text": " Name : ",
                                         "weight": "bold",
                                         "color": "#0000FF",
                                         "margin": "sm",
                                         "flex": 0
                                       },
                                       {
                                         "type": "text",
                                         "text": h.displayName,
                                         "size": "sm",
                                         "align": "end",
                                         "color": "#0000FF"
                                          }
                                        ]
                                      }
                                    ]
                                  },
                                  {
                                    "type": "text",
                                    "text": "_________________________________________________\nɬɧąŋƙʂ \nᴵᴰᴸᴵᴺᴱ ᴺᴵᴹᴬ¹⁰¹⁰ ,\n⚀🅽🅸🅼🅰 🅼🅰🆇⚀.",
                                    "wrap": True,
                                    "color": "#0000FF",
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
                                    "color": "#0000FF",
                                    "action": {
                                      "type": "uri",
                                      "label": "CONTACT",
                                      "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                                    }
                                  }
                                ]
                              }
                             }
                            }
                              cl.sendFlex(to, data)

                        elif cmd == "profil":
                                contact = cl.getContact(msg._from)
                                cover = cl.getProfileCoverURL(msg._from)
                                cl.reissueUserTicket()
                                res = "╭━━━━━━━━━━━━━━━━━━━━╮\n├ 🇮🇷 Profile info\n├━━━━━━━━━━━━━━━━━━━━\n"
                                res += "├ 🇮🇷 Display Name :{}\n".format(contact.displayName)
                                res += "├ 🇮🇷 Mid: {}\n".format(contact.mid)
                                res += "├ 🇮🇷 Status Message\n├ 🇮🇷 {}\n".format(contact.statusMessage)
                                res += "╰━━━━━━━━━━━━━━━━━━━━╯"
                                cl.sendMessage(Import_Server,Devert)
                                sendTextTemplate13(to, res)
                                try:
                                  poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                                except:
                                  poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                                dax = {
                "type": "template",
                "altText": "berak di celana",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": poto,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "PROFILE",
                        "uri": poto,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": "https://qr-official.line.me/L/"+cl.getUserTicket().id+".png",
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "CONTACT",
                        "uri": "https://line.me/ti/p/"+cl.getUserTicket().id,
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
                                cl.sendFlex(to, dax)

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "🇮🇷•PŘØŤĘČŤÎØŇ•🇮🇷\n"
                                if wait["sticker"] == True: md+="🇮🇷•➤Sticker「ON」\n"
                                else: md+="🇮🇷•➤Sticker「OFF」\n"
                                if wait["contact"] == True: md+="🇮🇷•➤Contact「ON」\n"
                                else: md+="🇮🇷•➤Contact「OFF」\n"
                                if wait["talkban"] == True: md+="🇮🇷•➤Talkban「ON」\n"
                                else: md+="🇮🇷•➤Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="🇮🇷•➤Notag「ON」\n"
                                else: md+="🇮🇷•➤Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="🇮🇷•➤Respon 1「ON」\n"
                                else: md+="🇮🇷•➤Respon 1「OFF」\n"
                                if wait["detectMention2"] == True: md+="🇮🇷•➤Respon 2「ON」\n"
                                else: md+="🇮🇷•➤Respon 2「OFF」\n"
                                if wait["arespon"] == True: md+="🇮🇷•➤Respon pm「ON」\n"
                                else: md+="🇮🇷•➤Respon pm「OFF」\n"
                                if wait["autoJoin"] == True: md+="🇮🇷•➤Autojoin「ON」\n"
                                else: md+="🇮🇷•➤Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="🇮🇷•➤Autoadd「ON」\n"
                                else: md+="🇮🇷•➤Autoadd「OFF」\n"
                                if settings["autoBlock"] == True: md+="🇮🇷•➤AutoBlock「ON」\n"
                                else: md+="🇮🇷•➤AutoBlock「OFF」\n"
                                if msg.to in welcome: md+="🇮🇷•➤Welcome「ON」\n"
                                else: md+="🇮🇷•➤Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="🇮🇷•➤Autoleave「ON」\n"
                                else: md+="🇮🇷•➤Autoleave「OFF」\n"
                                sendTextTemplate3(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'pembuat':
                            if msg._from in admin:
                                cl.sendMessage(msg.to,"Creator InexBots") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif text.lower() == "mid":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Getmid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               #cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "🇮🇷•➤Nama : "+str(mi.displayName)+"\n🇮🇷•➤Mid : " +key1+"\n🇮🇷•➤Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif "Pmcast: " in msg.text:
                            bctxt = msg.text.replace("Pmcast: ", "")
                            h = cl.getContact(msg._from)
                            a = cl.getAllContactIds()
                            cl.sendMessage(to, "Sukses broadcast ke "+str(len(a))+" teman")
                            for manusia in a:
                                C = cl.getContact(mid)
                                mids = [C.mid]
                                text = "BROADCAST FRIEND:\n\n{}\n\n⊶ ɪɴᴇxʙᴏᴛs ⊷ \nhttp://line.me/ti/p/Lgx8gKrUYn".format(str(bctxt))
                                sendMentionV2(manusia, text, mids)
                                #cl.sendMessage(manusia, (text))

                        elif cmd.startswith("gcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendBcast(grup, (bctxt))

                        elif cmd.startswith("bcast: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Broadcast 」\nBroadcast by "
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
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                data = {
            "type": "flex",
            "altText": "{} Menghapus anda dari grup ".format(jakaProfile.displayName),
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
                   "text": "ᴵᴰᴸᴵᴺᴱ ᴺᴵᴹᴬ¹⁰¹⁰",
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://i.pinimg.com/originals/fd/47/e5/fd47e55dfb49ae1d39675d6eff34a729.gif",
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/Lgx8gKrUYn"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": str(pesan),
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
                                cl.sendFlex(group, data)

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「🅽🅸🅼🅰 🅼🅰🆇 」\nSetkey bot 「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               sendTextTemplate(msg.to,bot)

                        elif cmd == "tipi":
                            contact = cl.getContact(mid)
                            cu = cl.getProfileCoverURL(mid)
                            #image = str(cu)
                            data = {
                                    "type": "flex",
                                    "altText": "Live streaming",
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
                                                "hero": {
                                                    "type": "image",
                                                    "url": "https://i.gifer.com/AJvy.gif",
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://media1.tenor.com/images/42a8d4625aeb088c45eba5a84ca36325/tenor.gif?itemid=11193323",
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": " TV STREAMING",
                                                    "size": "md",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://www.legayapi.com/theme/themeFiles/images/load.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"  SALURAN TELEVISI KELUARGA",              
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
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
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "CHANNEL",
                                                    "uri": "line://app/1560739707-0YmQLW3W",
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            cl.sendFlex(to, data) 

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
                            ret_ = "╭━━══[ Group Info ]══━━"
                            ret_ += "\n Nama Group : {}".format(str(group.name))
                            ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                            ret_ += "\nID Group : {}".format(group.id)
                            ret_ += "\n Pembuat : {}".format(str(gCreator))
                            ret_ += "\n Jumlah Member : {}".format(str(len(group.members)))
                            ret_ += "\n Jumlah Pending : {}".format(gPending)
                            ret_ += "\n═━━━Kode Qr/Link━━━═"
                            ret_ += "\n Group Ticket : {}".format(gTicket)
                            ret_ += "\n Group Qr : {}".format(gQr)
                            ret_ += "\n╰━━══[ INEXBOT]══━━"
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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                  "uri": "http://line.me/ti/p/Lgx8gKrUYn"
              }
          }]
      }]
  }
}
}
                            cl.sendFlex(to, data)

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " 🇮🇷•➤Grup Info\n"
                                ret_ += "\n🇮🇷•➤Nama Group : {}".format(G.name)
                                ret_ += "\n🇮🇷•➤ID Group : {}".format(G.id)
                                ret_ += "\n🇮🇷•➤Pembuat : {}".format(gCreator)
                                ret_ += "\n🇮🇷•➤Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n🇮🇷•➤Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n🇮🇷•➤Jumlah Pending : {}".format(gPending)
                                ret_ += "\n🇮🇷•➤Group Qr : {}".format(gQr)
                                ret_ += "\n🇮🇷•➤Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate(to, str(ret_))
                            except:
                                pass

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
            "text": "sᴇɢᴇʀᴀ ᴋʟɪᴋ ʟᴏɢɪɴ ᴜɴᴛᴜᴋ ʟᴏɢɪɴ,\nᴅᴀɴ ᴋʟɪᴋ ʟɪɴᴋ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ʟɪɴᴋ.",
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
    "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_oc=AQmPqDNEtZ1BaAsV88hv6Omtb4iAYtqLIB5eZ246K8p9zIaCWAh_LZUH4IJCIf6Izco&_nc_ht=scontent.fcgk8-1.fna&oh=1b6bbfe37e1ee80e79e251928d173319&oe=5D78D8F5",
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
        "text": "CHROMEOS",
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

                        elif text.lower() == 'tokenlist':
                               url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                               to = msg.to
                               data = {
        "type": "template",
        "altText": "Tokenlist",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_oc=AQmPqDNEtZ1BaAsV88hv6Omtb4iAYtqLIB5eZ246K8p9zIaCWAh_LZUH4IJCIf6Izco&_nc_ht=scontent.fcgk8-1.fna&oh=1b6bbfe37e1ee80e79e251928d173319&oe=5D78D8F5",
                    "title": "CHROMEOS",
                    "text": "ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nKETIK [ CHROME 1 ]",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CLICK",
                            "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=ChromeSpaces1"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-2.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/52427967_2326064874084289_579878214831177728_o.jpg?_nc_cat=107&efg=eyJpIjoiYiJ9&_nc_eui2=AeHb8CgrGa9k6YnEI4S68ZQqC_ofKGrLNvSnsbK6vezlyCteVLjGJZYC9Gwoh3fTmSPhRQs-xosP2j1ETI4AHqVhfgT-G_SK8iIfg1i_tCVZwQ&_nc_ht=scontent.fcgk8-2.fna&oh=3e47f989cae4e4f99830f7b88b609f6c&oe=5D64AB31",
                    "title": "IOSIPAD",
                    "text": "ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nKETIK [ IOS 1 ]",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CLICK",
                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=IosSpaces1"
                        }
                      ]
                   },
                  {
                    "thumbnailImageUrl": "https://scontent.fcgk8-2.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51739687_2326067977417312_5830327879942012928_n.jpg?_nc_cat=109&efg=eyJpIjoiYiJ9&_nc_eui2=AeELQzPVVYeHGkeaNu6tEg6GIqkb-hDBp8pMBsjM4_rXbuJYVVEcb77aNnsGPeT-5hjb2XqL-XnHtJZVnvijNeEDIIgYJoyoyquG9aOj2-BBhg&_nc_ht=scontent.fcgk8-2.fna&oh=4f2d6231f4b094ac6df246b28023212a&oe=5D31A0B0",
                    "title": "DESKTOPWIN",
                    "text": "ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nKETIK [ DESKTOPWIN 1 ]",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CLICK",
                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=DesktopwinSpaces1"
                        }
                      ]
                   },
                  {
                    "thumbnailImageUrl": "https://scontent.fcgk8-2.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/52427967_2326064874084289_579878214831177728_o.jpg?_nc_cat=107&efg=eyJpIjoiYiJ9&_nc_eui2=AeHb8CgrGa9k6YnEI4S68ZQqC_ofKGrLNvSnsbK6vezlyCteVLjGJZYC9Gwoh3fTmSPhRQs-xosP2j1ETI4AHqVhfgT-G_SK8iIfg1i_tCVZwQ&_nc_ht=scontent.fcgk8-2.fna&oh=3e47f989cae4e4f99830f7b88b609f6c&oe=5D64AB31",
                    "title": "DESKTOPMAC",
                    "text": "ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nKETIK [ MAC 1 ]",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CLICK",
                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=MacSpaces1"
                        }
                      ]
                   },
                  {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_oc=AQmPqDNEtZ1BaAsV88hv6Omtb4iAYtqLIB5eZ246K8p9zIaCWAh_LZUH4IJCIf6Izco&_nc_ht=scontent.fcgk8-1.fna&oh=1b6bbfe37e1ee80e79e251928d173319&oe=5D78D8F5",
                    "title": "WIN10",
                    "text": "ɪɴᴇxʙᴏᴛs.ʙᴏᴛʟɪɴᴇ \nKETIK [ WIN10 1 ]",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CLICK",
                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=win10spaces1"
                        }
                      ]
                    }
                  ]
                }
               }
                               cl.sendFlex(to, data)

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
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
                                    ret_ += "\n " "🇮🇷•➤"+ str(no) + ". " + mem.displayName
                                sendTextTemplate(to,"🇮🇷•➤Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    sendTextTemplate(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠🇮🇷•➤" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate(msg.to,"╔═🇮🇷•➤[ FRIEND LIST ]\n║\n"+ma+"║\n╚═🇮🇷•➤[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠🇮🇷•➤" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate1(msg.to,"╔═🇮🇷•➤[ GROUP LIST ]\n║\n"+ma+"║\n╚═🇮🇷•➤[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "Url Closed")

                        elif cmd == "gurl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"Kirim fotonya.....")

                        elif cmd == "myup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                sendTextTemplate(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "inex" or text.lower() == "tag":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append(i.mid)
                                mentionMembers(msg.to, b)

                        elif cmd.startswith("tag room: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//20
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*20 : (a+1)*20]:
                            			b.append(i.mid)
                            		mentionMembers(gid, b)                            
                    		        cl.sendMessage(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))

                        elif cmd == "adminlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
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
                                sendTextTemplate(msg.to,"🇮🇷•➤admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」 Rkf" %(str(len(owner)+len(admin)+len(staff))))
                        elif cmd == "prolist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate3(msg.to,"🇮🇷•➤Protection\n\n🇮🇷•➤PROTECT URL :\n"+ma+"\n🇮🇷•➤PROTECT KICK :\n"+mb+"\n🇮🇷•➤PROTECT INVITE :\n"+mb+"\n🇮🇷•➤PROTECT JOIN :\n"+md+"\n🇮🇷•➤PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectantijs)+len(ghost)+len(protectcancel))))

                        elif cmd == "pamit" or cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate(msg.to, "Mohon maaf bila da salah baik lisan maupun tulisan\nBye my fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate(msg.to, "🇮🇷•➤Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendTextTemplate(msg.to, "Speed Ngaciiirrr...")
                               elapsed_time = time.time() - start
                               sendTextTemplate(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
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
                                        cl.sendMessage(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "User kosong...")
                            else:
                                sendTextTemplate(msg.to, "Ketik lurking on dulu")

                        elif cmd == "زیرابیارو نشون بده" or cmd == "x on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃\n\niran : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  cl.sendMessage(msg.to, "1010")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "غیر فعال" or cmd == "x off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "Cek sider \n\n🅽🅸🅼🅰 : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n"+cctv['sidermem'][msg.to])
                              else:
                                  sendTextTemplate(msg.to, "♼🅽🅸🅼🅰 🅼🅰🆇 🅱🅾🆃♼")

#===========Hiburan============#
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "🇮🇷•➤Link : " + "https://www.instagram.com/" + instagram
                                text = "🇮🇷•➤Name : "+namaIG+"\n🇮🇷•➤Username : "+usernameIG+"\n🇮🇷•➤Biography : "+bioIG+"\n🇮🇷•➤Follower : "+followerIG+"\n🇮🇷•➤Following : "+followIG+"\n🇮🇷•➤Post : "+mediaIG+"\n🇮🇷•➤Verified : "+verifIG+"\n🇮🇷•➤Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

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
                            sendTextTemplate(msg.to,"🇮🇷•➤I N F O R M A S I •🇮🇷 \n\n"+"🇮🇷•➤Date Of Birth : "+lahir+"\n🇮🇷•➤Age : "+usia+"\n🇮🇷•➤Ultah : "+ultah+"\n🇮🇷•➤Zodiak : "+zodiak)


                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif "mudik" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-g9bAUWEmJVo/Wx8oA__cmPI/AAAAAAALbhg/eDKroutr6QIgDBB2wpPL2e7nLnjIEVOxQCLcBGAs/s1600/AS0004076_03.gif",
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

                        elif "lebaran" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "زیرابیارو نشون بده",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-ru5h6ZY1uR0/WSrEX_FADtI/AAAAAAAIGyA/MMCCNrPHXWsiv2qYMxeMekA2uYRQM081QCLcB/s1600/AW434676_01.gif",
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

                        elif "1010" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-ru5h6ZY1uR0/WSrEX_FADtI/AAAAAAAIGyA/MMCCNrPHXWsiv2qYMxeMekA2uYRQM081QCLcB/s1600/AW434676_01.gif",
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

                        elif "mohon maaf" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-w6uzVV3N2D0/Wx8oBbIK_rI/AAAAAAALbhk/P56hLDKJKHU9udV6T3O_E89X3QlSmC6FACLcBGAs/s1600/AS0004076_04.gif",
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

                        elif "gak puasa" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://media.tenor.com/images/13253695f2b4e34f7514848d0d118180/tenor.gif",
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

                        elif "bentar lagi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-4iM3cPRrNXY/WSrEX0LirGI/AAAAAAAIGyE/Y4bxdP2GFwIbVyZYhY8UMfNQAyv0mCexACLcB/s1600/AW434676_00.gif",
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

                        elif "takbiran" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-a4GQlMKGzjc/Wx8n_4IRObI/AAAAAAALbhU/9BRM5S93t7kTXl0fou0XsY4jxlCcb3d2wCLcBGAs/s1600/AS0004076_00.gif",
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

                        elif text.lower() == 'hahahaha':
                               url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                               to = msg.to
                               data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-W_bn2qqdYXE/Wyhbjj2wqKI/AAAAAAANIz4/KQVsbq-aXm0kZNfFOS5SN8fqCvQ18xnUACLcBGAs/s1600/AW1238502_03.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                               cl.sendFlex(to, data)

                        elif text.lower() == 'apass':
                               url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                               to = msg.to
                               data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://c-sf.smule.com/sf/s92/arr/96/be/8cf86704-a6c2-4e0c-b3c6-faaeae27ec87.jpg",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                               cl.sendFlex(to, data)
                        elif "pas band" in msg.text.lower():
                               url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                               to = msg.to
                               data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpSWAXZ0y0WKUwH_4QwoUQ8BEev3ZHxnI5jKl5pnwTTLSo_EIo",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/Lgx8gKrUYn"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                               cl.sendFlex(to, data)

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
                  "uri": "https://line.me/R/ti/p/Lgx8gKrUYn"
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
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#7FFF00"
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
            "color": "#F8F8FF"
          },
          {
            "text": "INEX TEAM\n\nMP3\nSONG ALBUM",
            "size": "xs",
            "color": "#00FF00",
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
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Proqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Prokick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Prokick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Proinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Proinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Projoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              if spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Kibar" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Kibar","")                                 
                                 gs = cl.getGroup(msg.to)
                                 sendTextTemplate(msg.to,"ASSALAMUALAIKUM \nHALLOOO!!! \nSORRY ROOM KALIAN \nKEBANYAKAN ANU\nINEXTEAM DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\nSIAP KAMI BANTAII \n\n\n\nFUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI\n⚀🅽🅸🅼🅰 🅼🅰🆇⚀\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n   SLAM KILERR\n⚀🅽🅸🅼🅰 🅼🅰🆇⚀ \n\n\nCREATOR\n\n\nhttps://line.me/R/ti/p/Lgx8gKrUYn\nhttp://line.me/ti/p/~denjaka-inex")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     sendTextTemplate(msg.to,"Limit boss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   wait["blacklist"][op.param2] = True
                                                   cl.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                        elif ("kick " in msg.text):
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
                                           cl.sendMessage(msg.to, "")
                                           wait["blacklist"][op.param2] = True
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "refresh" or text.lower() == 'fresh':
                            if msg._from in admin:
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
                                sendTextTemplate(msg.to,"Berhasil di Refresh...")

                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == '.contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == '.contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "r1 on" or text.lower() == 'respon1 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"Auto respon diaktifkan")

                        elif cmd == "r1 off" or text.lower() == 'respon1 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "r2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = True
                                sendTextTemplate(msg.to,"Auto respon 2 diaktifkan")

                        elif cmd == "r2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = False
                                sendTextTemplate(msg.to,"Auto respon 2 dinonaktifkan")

                        elif cmd == "pm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["arespon"] = True
                                sendTextTemplate(msg.to,"Auto respon pm diaktifkan")

                        elif cmd == "pm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["arespon"] = False
                                sendTextTemplate(msg.to,"Auto respon pm dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == '.autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == '.autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == '.autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == '.autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == '.autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == '.autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "autoblock on":
                           if msg._from in admin:
                                settings["autoBlock"] = True
                                cl.sendMessage(to, "Berhasil mengaktifkan auto Block")

                        elif cmd == "autoblock off":    
                            if msg._from in admin: 	
                                settings["autoBlock"] = False
                                cl.sendMessage(to, "Berhasil menonaktifkan auto Block")

                        elif cmd == "read on" or text.lower() == '.autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                sendTextTemplate(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                sendTextTemplate(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == '.sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == '.sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == '.jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == '.jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"Autojoin Tiket dinonaktifkan")

                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 sendTextTemplate(to, "Berhasil mengaktifkan check details post")

                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan check details post")                        

                        elif cmd == "unsend on":
                          if msg._from in admin:
                            if msg.toType == 2:
                                wait["unsend"] = True
                                sendTextTemplate(msg.to, "Deteksi Unsend Diaktifkan")

                        elif cmd == "unsend off":
                          if msg._from in admin:
                            if msg.toType == 2:
                                wait["unsend"] = False
                                sendTextTemplate(msg.to, "Deteksi Unsend Dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif cmd == "cek":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               try:cl.cancelGroupInvitation(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has2 = "OK"
                               except:has2 = "NOT"
                               if has == "OK":sil = "🅱🅰🅳🅰🅽 🆂🅴🅷🅰🆃"
                               else:sil = "🆃🅾🅻🅾🅽🅶 🅰🅺🆄"
                               if has1 == "OK":sil1 = "https://2.bp.blogspot.com/-4Yr8ckT8tgs/U_ZiZFWPewI/AAAAAAAACDo/GUcjJOT1lrE/s1600/senamsehat.gif"
                               else:sil1 = "https://1.bp.blogspot.com/-GhAAjmcghVc/WDQHbLNi7bI/AAAAAAAAAGg/-wIouq5Hu3EEnwdx2jr-DFN9r0Vn5f3IgCLcB/s1600/Infectieziekten%2B%25281%2529.gif"
                               if has2 == "OK":sil2 = "https://www.isostar.com/share/sport/img_anime_rub/1.gif"
                               else:sil2 = "https://www.gambaranimasi.org/data/media/511/animasi-bergerak-kubur-0025.gif"
                               #sendTextTemplate(to, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                               data = {
                                    "type": "flex",
                                    "altText": "Cek kesehatan",
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
                                                "hero": {
                                                    "type": "image",
                                                    "url": "{}".format(sil1),
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "{}".format(sil2),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#ECF0F1"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "{}".format(sil),
                                                    "size": "md",
                                                    "align": "center",
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
                                }
                            }
                               cl.sendFlex(to, data) 

                        elif (".Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait[".blacklist"][target] = True
                                           sendTextTemplate(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == '.ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == '.cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"🇮🇷•➤Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"🇮🇷•➤Blacklist User\n\n"+ma+"\nTotal🇮🇷•➤「%s」🇮🇷•➤Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == '.talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "cban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              sendTextTemplate(msg.to,"🇮🇷•➤Clearr" +mc)
#===========COMMAND SET============#
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set r1: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r1: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "「Respon Msg」\nRespon1 Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set r2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate(msg.to, "「Respon Msg」\nRespon 2 Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set pm: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pm: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Responpm"] = spl
                                  sendTextTemplate(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set autojoin: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autojoin: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Msg join")
                              else:
                                  wait["autoJoinMessage"] = spl
                                  sendTextTemplate(msg.to, "「Msg autojoin」\nMsg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  sendTextTemplate(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek allrespon":
                            if msg._from in admin:
                               sendTextTemplate3(msg.to, "➤🇮🇷•Pesan add Msg mu :\n「 " + str(wait["message"])+ "\n\n➤🇮🇷•Welcome Msg mu :\n「 " + str(wait["welcome"]) + " 」\n\n➤🇮🇷•Respon 1 Msg mu :\n「 " + str(wait["Respontag"]) + " 」\n\n➤🇮🇷•Respon 2 Msg mu :\n「 " + str(wait["Respontag2"]) + " 」\n\n➤🇮🇷•Respon Msg PM mu :\n「 " + str(wait["Responpm"]) + " 」\n\n➤🇮🇷•Sider Msg mu :\n「 " + str(wait["mention"]) + " 」\n\n➤🇮🇷•Msg Auto joinmu :\n「 " + str(wait["autoJoinMessage"]) + " 」")

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek r1":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Respon Msg」\nRespon 1 Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek r2":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Respon Msg」\nRespon 2 Msg mu :\n\n「 " + str(wait["Respontag2"]) + " 」")

                        elif text.lower() == "cek pm":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Respon MsgPm」\nRespon Msg PM mu :\n\n「 " + str(wait["Responpm"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
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
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
