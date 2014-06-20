'''
    The MIT License (MIT)
    Copyright (c) 2014 PeppeLaKappa
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
    OR OTHER DEALINGS IN THE SOFTWARE.
'''

import pyPocket
import os
import json
import time
import argparse
import shell
import subprocess

null = open(os.devnull, "w")

try:
    subprocess.call("w3m", stderr=null, stdout=null)
except OSError:
    print("w3m is required to use clipocket.")
    exit(1)

# initialize the argparse
parser = argparse.ArgumentParser()
parser.add_argument("--reader", help="read your Pocket articles directly from your Shell", action="store_true")
parser.add_argument("--add", help="add a link to the authorized account")
args = parser.parse_args()

consumerKey = "23692-39e93da62c7cbec9e5e4c468"
redirectUri = "http://gsora.me"

if(not os.path.isfile("myLoginData")):
    # get the request token and authorize it

    rTok = pyPocket.requestToken(consumerKey, redirectUri)
    url = "Go to https://getpocket.com/auth/authorize?request_token={}&redirect_uri={} then press enter".format(rTok, redirectUri)
    print(url)
    a = input("")

    # then get the access token and save into a file

    aTok = pyPocket.accessToken(consumerKey, rTok)
    file = open("myLoginData", "a")
    file.write(aTok)
    file.close()

file = open("myLoginData", "r")
aTok = file.readline()

if args.reader:
    # now let's parse some data
    gData = pyPocket.getData(consumerKey, aTok)

    # load the json
    pocketJson = json.loads(gData)

    # counts how many links you saved
    entryCounter = 0

    # a dict containing your actual links data (eg: URL, name, word count etc)
    pocketEntries = {}
    for i in sorted(pocketJson["list"]):
        pocketEntries[entryCounter] = pocketJson["list"][i]
        entryCounter+=1

    # a pretty CLI-like interface!
    while(1):
        shell.cpShell(pocketEntries, entryCounter)

if args.add:
    print("Working...")
    try:
    	pyPocket.addData(consumerKey, aTok, args.add)
    	print("Added!")
    except AttributeError:
    	print("Failed!")

file.close()
