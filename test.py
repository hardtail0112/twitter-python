
import sys 
import tweepy 
CONSUMER_KEY = 'JpU9Lb1PEpFtLgC7XOlkw' 
CONSUMER_SECRET = 'k6TsCWbybimpcBMhi8o5simuuoX3XjoMGtG5Ij9U' 
ACCESS_KEY = '132108032-vQ58uSC6HE0IOOMtmZcRjjko4gbykAOmDF4Vg3tI' 
ACCESS_SECRET = 'Q2uMS4NvwPhAs6BthJ19ImdYCixXmxfUos1B76D4' 
mypost = sys.stdin.readline().strip() 
if 0==len(mypost):
    exit() 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 
api = tweepy.API(auth_handler=auth, api_root='/1.1', secure=True)
api.update_status(mypost)
