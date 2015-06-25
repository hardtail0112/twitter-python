#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import twitter
import post
import time

def countdown(now):
   month = now.split(' ')[1]
   day = now.split(' ')[2]
   hour = now.split(' ')[3].split(':')[0]
   if month =="Nov":
      last = 30-int(day)+14
   else :
      last = 31-int(day)
   return last

if __name__ == "__main__":
   api = post.SetTwitterApi('server')
   
   now = time.ctime()
   val = countdown(now)
   
   text = u"コミケまで...\n\n"
   text += u"＿人人人人＿"
   text += u"\n＞ あと%2d日 ＜\n"%val
   text += u"￣Y^Y^Y^Y￣\n"
   text += u"\n3日目東P51Bで僕と握手！！！"
   
   api.PostUpdate(text)
