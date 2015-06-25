#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import twitter
import post
import time

usr = 'server'

api = post.SetTwitterApi(usr)

follower = api.GetFollowers()
follow = api.GetFriends()

for ff in follower:
   flag = 0
   for f in follow:
      if f.name == ff.name:
         flag = 1
   
   if flag == 0:
      api.CreateFriendship(user_id=ff.id)
      time.sleep(1)



