#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matsuzawa
#
# Created:     18/12/2013
# Copyright:   (c) matsuzawa 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
import json
import time

def getURL(place,date):
    url = "https://udon.upsilo.net/citlunch/api/"+place
    return url+"/"+date+"/menu.json"

def getLunch(place,date="today"):
    if date is "today":
        date=time.strftime("20%y-%m-%d")
    url = getURL(place,date)

    request = urllib2.Request(url)
    # ????????????????
    contents = urllib2.urlopen(request)
    # ??????????
    contents_str = contents.read()
    # str ???????????
    contens_dict = json.loads(contents_str)
    return contens_dict


def main():
    lunch = getLunch("shiba_dining")
    for i in lunch:
        print i["name"]
        for a in i["details"]:
            print " "+a


if __name__ == '__main__':
    main()
