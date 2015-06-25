#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import account
import secret2
import twitter
import sys
import codecs

def SetTwitterApi(usr):
   return twitter.Api(
      consumer_key = account.consumer_key[usr],
      consumer_secret = account.consumer_secret[usr],
      access_token_key = account.access_token_key[usr],
      access_token_secret = account.access_token_secret[usr]
   )

def help():
   print "api = post.SetTwitterApi(usr)"

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

if __name__ == "__main__":
   #user = raw_input('whitch usr>')
   api = SetTwitterApi("server")

   s = sys.argv
   test = str(s[1])
   out = api.PostUpdate(status = test)
   #print test
