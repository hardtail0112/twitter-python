#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import post
import twitter
import time
import commands
import calendar
import os

def timetotime(t):
   return t.split(' ')[3].split(':')

def today(now,rp):
   if int(now.split(' ')[3]) == int(rp.split(' ')[3]):
      return 1
   else : return 0

def invert(now,rptime):
   min = int(now[1]) - int(rptime[1])
   if (int(rptime[0])+9) < 24:
      hour = int(now[0])-(int(rptime[0])+9)
   else :
      hour = int(now[0])-(int(rptime[0])+9-24)
   if min <2 :
      if hour != 0: return 0
      return 1
   else  :return 0

def YmdHMS(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return time.strftime("%Y,%m,%d,%H,%M,%S", time_local)

def signin(name):
   mastar = u"HardTail_bike"
   if name == mastar:
      return 1
   else : return 0 


if __name__ == "__main__":
   api = post.SetTwitterApi('server')
   
   rp = api.GetMentions()
   now = time.ctime()
   
   i=0
   mastar = u"HardTail_bike"
   
   while (invert(timetotime(now),timetotime(rp[i].created_at)) and (int(now.split(" ")[2])==int(YmdHMS(rp[i].created_at).split(",")[2]))):
      flag = 0
      
      if u"時間" in rp[i].text:
         rptext = "@"+rp[i].user.screen_name +" "+now 
         flag = 1
      
      if u"よくできました" in rp[i].text:
         rptext = "@"+rp[i].user.screen_name +u" └( ＾ω＾ )」♪"
         flag = 1
      
      if u"天気" in rp[i].text:
         rptext = "@"+rp[i].user.screen_name +u" はれ（適当）"
         flag = 1
      
      if u"プロセス" in rp[i].text:
         pstest = commands.getoutput("ps -a | grep Identity.py$")
         if pstest == '': pstest = u"落ちてるよ"
         else :pstest = u"動いてるよ"
         rptext = "@"+rp[i].user.screen_name +" "+pstest+"\n"+now
         flag = 1
      
      if u"復活" in rp[i].text:
         res = os.system("/home/hardtail/twitter-python/serverIdentity.py &")
         rptext = "@"+rp[i].user.screen_name + u" 復活させました\n"
         flag = 1
      
      if u"認証" in rp[i].text:
         if signin(rp[i].user.screen_name) :text =  u" いえす　ますたー"
         else : text = u" ふぁ？"
         rptext = "@"+rp[i].user.screen_name + text+"\n"+now
         flag = 1
      
      if flag == 1 : api.PostUpdate(status=rptext,in_reply_to_status_id=rp[i].id)
      i=i+1


