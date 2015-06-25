#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta

def get_oauth():
    consumer_key = 'JpU9Lb1PEpFtLgC7XOlkw'
    consumer_secret = 'k6TsCWbybimpcBMhi8o5simuuoX3XjoMGtG5Ij9U'
    access_key = '132108032-vQ58uSC6HE0IOOMtmZcRjjko4gbykAOmDF4Vg3tI'
    access_secret = 'Q2uMS4NvwPhAs6BthJ19ImdYCixXmxfUos1B76D4'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth

class AbstractedlyListener(StreamListener):
    """ Let's stare abstractedly at the User Streams ! """
    def on_status(self, status):
        # Ubuntuの時は気づかなかったんだけど、Windowsで動作確認してたら
        # created_atがUTC（世界標準時）で返ってきてた。
        # なので日本時間にするために9時間プラスする。
        status.created_at += timedelta(hours=9)
        # format() が使えるのは Python 2.6 以上
        print(u"{text}".format(text=status.text))
        print(u"{name}({screen}) {created} via {src}\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, src=status.source))

if __name__ == '__main__':
    auth = get_oauth()
    stream = Stream(auth, AbstractedlyListener(), secure=True)
    stream.userstream()

