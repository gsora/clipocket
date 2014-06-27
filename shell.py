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

import parser
import os
import datetime
import pyPocket

def cpShell(pocketDict, entries, consumerKey, aTok):
    for i in range(0, entries):
    
        favFlag = "no"
        typeFlag = "article"
        addDate = datetime.datetime.fromtimestamp(int(pocketDict[i]["time_added"])).strftime('%a, %d %b %Y %H:%M:%S')

        if pocketDict[i]["favorite"] == '1':
            favFlag = "yes"

        if pocketDict[i]["has_video"] == "2":
            typeFlag == "video"
        elif pocketDict[i]["has_image"] == "2":
            typeFlag == "image"

        print("{}) {}\n\tFavorite: {}\n\tType: {}\n\tAdded: {}\n".format(i, pocketDict[i]["resolved_title"], favFlag, typeFlag, addDate))
    
    prompt = input("clipocket> ")
    prompt = prompt.split(" ")
    if len(prompt) > 2 or len(prompt) < 2 and prompt[0] is not "clear":
        if prompt[0] == "exit":
            exit()
        elif prompt[0] == "clear":
            os.system("clear")
            return
        else:
            cpHelp()
            return

    command = prompt[0]
    argument = prompt[1]

    if command == "help":
        cpHelp()
        return

    elif command == "read":
        cpRead(argument, pocketDict, consumerKey, aTok)
        return

    elif command == "done":
        cpDone(argument, pocketDict, consumerKey, aTok)
        return

    elif command == "rm":
        cpRm()
        return 

    elif command == "star":
        cpStar()
        return

def cpHelp():
    print("\nCLIPocket command reference:\n\tread: read a post\n\tdone: mark as read\n\trm: delete an entry\n\tstar: star an entry\n\tclear: clear the screen\n\texit: quit clipocket\n")

def cpDone(index, pocketDict, consumerKey, aTok):
    if index == 0:
        print("Syntax:\n\tdone [entry-number]")
        return "error"
    else:
        entryID = pocketDict[int(index)]["resolved_id"]
        pyPocket.archive(entryID, consumerKey, aTok)
        return "ok"

def cpRm():
    print("Not implemented yet :(")

def cpStar():
    print("Not implemented yet :(")

def cpRead(index, pocketDict, consumerKey, aTok):
    if index == 0:
        print("Syntax:\n\tread [entry-number]")
        return "error"
    else:
        title = pocketDict[int(index)]["resolved_title"]
        url = pocketDict[int(index)]["resolved_url"]
        entryID = pocketDict[int(index)]["resolved_id"]
        parser.createManPage(title, url)
        choice = input("Would you want to archive this item? (a/n): ")
        if choice == "a":
            cpDone(index, pocketDict, consumerKey, aTok)
           

