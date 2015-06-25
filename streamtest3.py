#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import tweepy, urllib, urllib2, json, account,post
import sys, codecs

usr = 'main'
consumer_key    = account.consumer_key[usr]
consumer_secret = account.consumer_secret[usr]
access_key      = account.access_token_key[usr]
access_secret   = account.access_token_secret[usr]

api = post.SetTwitterApi(usr)

def main():
    
    url = "https://userstream.twitter.com/2/user.json"
    param = {"delimited":"length"}
    header = {}
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    auth.apply_auth(url,"POST",header,param)
    req = urllib2.Request(url)
    req.add_header("Authorization",header["Authorization"])
    r = urllib2.urlopen(req,urllib.urlencode(param),90)
    while True:
        len = ""
        while True:
            c = r.read(1)
            if c=="\n": break
            if c=="": raise Exception
            len += c
        len = len.strip()
        if not len.isdigit(): continue
        t = json.loads(r.read(int(len)))
        if "user" in t and "text" in t and "created_at" in t and "id" in t:
            print "%s(%s)" % (t["user"]["name"],t["user"]["screen_name"])
            print "%s" % (t["text"],)
            print "%s  id:%s" % (t["created_at"],t["id"])
            print
            
        if "event" in t:
            print "\n event " + t["event"] + "\n"


if __name__=="__main__":
    main()
