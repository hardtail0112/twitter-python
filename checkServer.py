#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import os
import commands

pstest = commands.getoutput("ps -x | grep Identity.py$")
comand = "./serverIdentity.py &"

if pstest == '':
   os.system("./serverIdentity.py &")
#   print "OK"
#else:
#   print "yet"

