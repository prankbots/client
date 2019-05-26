from lineX import *
from multiprocessing import Pool, Process
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import LoginRequest
from akad import LineService
import json, requests
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from googletrans import Translator
_session = requests.session()
botStart = time.time()
OWNER = "u0ac948397fbc732bd3bc5ca273faa698"
try:
    with open("temp.json","r",encoding="utf_8_sig") as f:
        set = json.loads(f.read())
except:
    print("TEMP JSON ERROR")
def backupData():
    try:
        backup = set
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print (error)
        return False
def restartBot():
    print ("RESET")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
class OverPoll(object):
    def __init__(self, resp, authQR=None):
        self.resp = resp
        self.resp = self.resp+' '
        self.authQR = authQR
        self.login(authQR)
        self.fetch()
    def login(self, auth):
        if auth == None:
            self.client = LINE()
        else:
            self.client = LINE(idOrAuthToken=auth)
        self.client.log(str(self.client.authToken))
        self.mid = self.client.getProfile().mid
        sett = open('temp.json','r')
        self.set = json.load(sett)
        mbah = open('read.json','r')
        self.read = json.load(mbah)
        
    def fetch(self):
        while True:
            try:
                self.operations = self.client.poll.fetchOperations(self.client.revision, 10)
                for op in self.operations:
                    if (op.type != OpType.END_OF_OPERATION):
                        self.client.revision = max(self.client.revision, op.revision)
                        self.bot(op)
            except Exception as error:
                print(error)
    def bot(self, op):
      me = self.client
      meM = self.mid
      set = self.set
      read = self.read
      meProfile = me.getProfile()
      mid = me.getProfile().mid
      St = set["stile"]
      try:
        if op.type == 0:
            return
        if op.type == 5:
            icone = ("1","2","3","4","5","6","7")
            stgift = random.choice(icone)
            icont = ("2ec7c3ad-2257-4b6d-bf8a-9e676fa18239","eb0949bf-c2ef-4fe1-8bec-149d8a46a44d","03de6834-ffdb-4d87-bcd7-853d3e4ec2ac","29568287-d858-44e7-b254-0558cad97933","25e24851-994d-4636-9463-597387ec7b73","02d85080-6b81-448d-9ecb-b8c72cde3561","eb2f8450-e1ae-4846-940d-bac85cf31244","6c3a8150-58c7-4a87-85e8-617b4ef25daa")
            giftst = random.choice(icont)
            if set["autoAdd"] == True:
                me.findAndAddContactsByMid(op.param1)
            me.sendMention(op.param1, op.param1, "Thanks sudah add ","")
            me.sendMessage(op.param1, None, contentMetadata={'PRDID': giftst, 'PRDTYPE': 'THEME', 'MSGTPL': stgift}, contentType=9)
        if op.type == 17:
          if op.param2 in set["ban"]:
            g = me.getGroup(opp1)
            if g.preventedJoinByTicket == True:
              pass
            else:
              g.preventedJoinByTicket = True
              me.updateGroup(g)
              try:
                me.sendMessage(op.param1,"sorry...\ncontact in blacklist")
                me.kickoutFromGroup(op.param1,[op.param3])
              except:pass
        if op.type == 19 or op.type == 32:
          if op.param3 in set["bot"]:
            if op.param2 in set["bot"] or op.param2 in meM:
              pass
            else:
              set["ban"][op.param2] = True
              try:
                me.kickoutFromGroup(op.param1,[op.param2])
                me.inviteIntoGroup(op.param1,[op.param3])
              except:pass
        if op.type == 13:
          if meM in op.param3:
            if op.param2 in set["bot"] or op.param2 in OWNER:
              me.acceptGroupInvitation(op.param1)
            else:pass
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != me.profile.mid:
                        to = sender
                    else:
                        to = receiver
                if msg.toType == 1:
                    to = receiver
                if msg.toType == 2:
                    to = receiver
                if set["autoRead"] == True:
                    me.sendChatChecked(receiver, msg.id)
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        Pbot = text.lower()
                        if Pbot == "help":
                            zxz = "╔HELP PUB"
                            zxz += "\n╠Me"
                            zxz += "\n╠Myprofile"
                            zxz += "\n╠Prangkat"
                            zxz += "\n╠Mid"
                            zxz += "\n╠Creator/admin"
                            zxz += "\n╠Gift"
                            zxz += "\n╠Speed"
                            zxz += "\n╠Channel"
                            zxz += "\n╚═════════"
                            me.reMessage(msg.id, to, zxz)
                        if Pbot == "myhelp":
                          if msg._from in OWNER or msg._from in meM:
                            zxz = "╔SELF & ADMIN"
                            zxz += "\n╠Me"
                            zxz += "\n╠Myprofile"
                            zxz += "\n╠Prangkat"
                            zxz += "\n╠#Reboot"
                            zxz += "\n╠Botinfo"
                            zxz += "\n╠Mid"
                            zxz += "\n╠Creator/admin"
                            zxz += "\n╠Gift"
                            zxz += "\n╠Speed"
                            zxz += "\n╠Channel"
                            zxz += "\n╠Kick @"
                            zxz += "\n╠Addbot @"
                            zxz += "\n╠Delbot @"
                            zxz += "\n╠botlist"
                            zxz += "\n╠Banlist"
                            zxz += "\n╠Clearbot"
                            zxz += "\n╠Clearban"
                            zxz += "\n╠Bot [to invite]"
                            zxz += "\n╚═════════"
                            me.reMessage(msg.id, to, zxz)
                        if Pbot == "me":
                            contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(msg._from).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(msg._from).statusMessage if me.getContact(msg._from).statusMessage != '' else 'creator By PrankBots |ID LINE|\nadiputra.95', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(msg._from).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+msg._from,'MSG_SENDER_NAME':  me.getContact(msg._from).displayName,}
                            me.reMessage(msg.id, to, me.getContact(msg._from).displayName, contentMetadata, 19)
                        if Pbot == "myprofile":
                            contact = me.getContact(msg._from)
                            result = "╔══[___ Details Profile ___]"
                            result += "\n╠ Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status: {}".format(contact.statusMessage)
                            result += "\n╚══[_______________________]"
                            try:
                                me.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                me.reMessage(msg.id, to, result)
                            except:
                                me.reMessage(msg.id, to, result)
                                me.sendMessage(to,"anda tidak memiliki foto profile\nTERCYDUK BAPER")
                        if Pbot == "perangkat":
                            me.reMessage(msg.id, to, "CEK DAFTAR PERANGKAT KAMU\nline://nv/connectedDevices/")
                        if Pbot == "#reboot":
                          if msg._from in OWNER or msg._from in meM:
                            me.reMessage(msg.id, to, "ngges.!!")
                            set["restartPoint"] = to
                            restartBot()
                        elif Pbot == "botinfo":
                          if msg._from in OWNER or msg._from in meM:
                            start = time.time()
                            me.sendMessage(to, "wait...")
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            cmd= "╭════════Informasi════════\n"
                            cmd+= St + "ᴄʀᴇᴀᴛᴏʀ: {}\n".format(str(mastah.displayName))
                            cmd+= St + "ᴛʏᴘᴇ ʙᴏᴛ: ᴏғғɪᴄɪᴀʟ ʟɪɴᴇ\n"
                            cmd+= St + "ᴛʏᴘᴇ ᴛʜʀɪғᴛ: ᴛʜʀɪғᴛ ᴍᴏᴅ.ᴠ1\n"
                            cmd+= St + "ᴛʏᴘᴇ ʟɪʙ: ʟɪɴᴇᴘʏ ᴍᴏᴅ ᴏғғɪᴄɪᴀʟ\n"
                            cmd+= St + "sᴘᴇᴇᴅ ʙᴏᴛ: %.5f\n" % (took)
                            cmd+= St + "ʀᴇsᴘᴏɴ sᴘᴇᴇᴅ: %.5f\n" % (elapsed_time)
                            cmd+= St + "━━━━━━━━ᴅᴇᴠɪᴄᴇ━━━━━━━━\n"
                            cmd+= St + "ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ\n"
                            cmd+= St + "https://bit.ly/2xbVxlh\n"
                            cmd+= St + "ᴄʜɪᴍɪᴄʜɪᴍɪ ʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ\n"
                            cmd+= St + " https://bit.ly/2OJc46U\n"
                            cmd+= St + "ᴏғғɪᴄɪᴀʟ ᴠᴏɪᴄᴇ ᴏғ ɢᴀᴍᴇʀ sᴍᴜʟᴇ\n"
                            cmd+= St + "https://bit.ly/2T4gRCp\n"
                            cmd+= "╰════════ʙʏ:ᴘʀᴀɴᴋʙᴏᴛ═══════"
                            me.reMessage(msg.id, to, cmd)
                        elif Pbot == "mymid" or Pbot == "mid":
                            x = me.getContact(sender)
                            me.reMessage(msg.id, to,x.mid)
                        elif Pbot == "creator" or Pbot == "admin":
                            x = me.getContact(OWNER)
                            me.reMessage(msg.id, to, None, contentMetadata={'mid': x.mid}, contentType=13)
                        elif Pbot == "gift":
                            me.reMessage(msg.id, to, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                        elif Pbot == "sp" or Pbot == "speed":
                            start = time.time()
                            me.sendMessage(to, ".......")
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            me.reMessage(msg.id, to,"mencret : %.4fms\nSpeed respon: %.8f" % (took,elapsed_time))
                        elif Pbot.startswith("kick "):
                          if msg._from in OWNER or msg._from in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', text)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              lists = []
                              for mention in mentionees:
                                if mention["M"] not in lists:
                                  lists.append(mention["M"])
                              for ls in lists:
                                try:
                                  me.kickoutFromGroup(to,[ls])
                                except Exception as e:
                                  me.log(str(e))
                        elif Pbot.startswith("delbot "):
                          if msg._from in OWNER or msg._from in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', text)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              lists = []
                              for mention in mentionees:
                                if mention["M"] not in lists:
                                  lists.append(mention["M"])
                              for ls in lists:
                                try:
                                  del set["bot"][ls]
                                  me.sendMessage(to,"Berhasil menghapus daftar bot")
                                except:me.sendMessage(to,"tidak ada dalam daftar bot")
                        elif Pbot.startswith("addbot "):
                          if msg._from in OWNER or msg._from in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', text)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              lists = []
                              for mention in mentionees:
                                if mention["M"] not in lists:
                                  lists.append(mention["M"])
                              for ls in lists:
                                try:
                                  me.findAndAddContactsByMid(ls)
                                  set["bot"][ls] = True
                                  me.sendMessage(to,"Berhasil menambahkan daftar bot")
                                except:me.sendMessage(to,"Sudah ada dalam daftar bot")
                        elif Pbot == "clearbot":
                          if msg._from in OWNER or msg._from in meM:
                            me.sendMessage(to,"DAFTAR[%s] BOT\n[success deleted]" % (str(len(set["bot"]))))
                            set["bot"] = {}
                        elif Pbot == "clearban":
                          if msg._from in OWNER or msg._from in meM:
                            me.sendMessage(to,"DAFTAR[%s] BAN\n[success deleted]" % (str(len(set["ban"]))))
                            set["ban"] = {}
                        elif Pbot == "banlist":
                          if msg._from in OWNER or msg._from in meM:
                            if set["ban"] == {}:
                              me.sendMessage(to,"Tidak Ada kontak blacklist")
                            else:
                              me.sendMessage(to,"═══════blacklist═══════")
                              h = ""
                              for i in set["ban"]:
                                h = me.getContact(i)
                                me.sendContact(to,i)
                        elif Pbot == "botlist":
                          if msg._from in OWNER or msg._from in meM:
                            if set["bot"] == {}:
                              me.sendMessage(to,"Tidak Ada kontak bot")
                            else:
                              me.sendMessage(to,"═══════botlist═══════")
                              h = ""
                              for i in set["bot"]:
                                h = me.getContact(i)
                                me.sendContact(to,i)
                        elif Pbot == "bot":
                          if msg._from in OWNER or msg._from in meM:
                            if set["bot"] == {}:
                              me.sendMessage(to,"Tidak Ada kontak bot")
                            else:
                              me.inviteIntoGroup(to,set["bot"])
                        elif Pbot == "channel":
                            me.sendMessage(to, "Waiting...")
                            search = "PrankBots"
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(set["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.reMessage(msg.id, to, str(ret_))
      except Exception as e:
          print(e)
