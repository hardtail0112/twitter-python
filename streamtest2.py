#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.nari64.com/?p=200
   
import sys
import tweepy
from tweepy import  Stream, TweepError
import logging
import urllib
 


CONSUMER_KEY  = 'JpU9Lb1PEpFtLgC7XOlkw'
CONSUMER_SECRET = 'k6TsCWbybimpcBMhi8o5simuuoX3XjoMGtG5Ij9U'
ACCESS_TOKEN = '132108032-vQ58uSC6HE0IOOMtmZcRjjko4gbykAOmDF4Vg3tI'
ACCESS_TOKEN_SECRET = 'Q2uMS4NvwPhAs6BthJ19ImdYCixXmxfUos1B76D4'
  
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  
class CustomStreamListener(tweepy.StreamListener):
  
    def on_status(self, status):
  
        try:
            print "---%s---\n  %s\n" % (
                                      status.author.screen_name,
                                      status.text)
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass
  
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream
  
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
  
  
class UserStream(Stream):
   
    def user_stream(self, follow=None, track=None, async=False, locations=None):
        self.parameters = {"delimited": "length", }
        self.headers['Content-type'] = "application/x-www-form-urlencoded"
  
        if self.running:
            raise TweepError('Stream object already connected!')
  
        self.scheme = "https"
        self.host = 'userstream.twitter.com'
        self.url = '/2/user.json'
  
        if follow:
           self.parameters['follow'] = ','.join(map(str, follow))
        if track:
            self.parameters['track'] = ','.join(map(str, track))
        if locations and len(locations) > 0:
            assert len(locations) % 4 == 0
            self.parameters['locations'] = ','.join(['%.2f' % l for l in locations])
  
        self.body = urllib.urlencode(self.parameters)
        logging.debug("[ User Stream URL ]: %s://%s%s" % (self.scheme, self.host, self.url))
        logging.debug("[ Request Body ] :" + self.body)
        self._start(async)
   
def main():
    stream = UserStream(auth, CustomStreamListener())
    stream.timeout = None
    stream.user_stream()
  
if __name__ == "__main__":
  main()
