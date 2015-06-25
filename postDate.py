#!/usr/local/bin/python
import time
import twitter
import post

api = post.SetTwitterApi('server')
now = time.ctime()

api.PostUpdate(status = now)
