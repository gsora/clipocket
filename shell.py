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

def cpShell(pocketDict, entries):
    for i in range(0, entries):
        print("{}) {}".format(i,pocketDict[i]["resolved_title"]))
    
    prompt = input("\nclipocket> ")
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
    elif command == "read":
        cpRead(argument, pocketDict)
    elif command == "done":
        cpDone()
    elif command == "rm":
        cpRm()
    elif command == "star":
        cpStar()

def cpHelp():
    print("\nCLIPocket command reference:\n\tread: read a post\n\tdone: mark as read\n\trm: delete an entry\n\tstar: star an entry\n\tclear: clear the screen\n\texit: quit clipocket\n")

def cpDone():
    print("Not implemented yet :(")

def cpRm():
    print("Not implemented yet :(")

def cpStar():
    print("Not implemented yet :(")

def cpRead(index, pocketDict):
    if index == 0:
        print("Syntax:\n\tread [entry-number]")
        return "error"
    else:
        title = pocketDict[int(index)]["resolved_title"]
        url = pocketDict[int(index)]["resolved_url"]
        parser.createManPage(title, url)

