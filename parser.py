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

import bs4
import urllib.request
import json
import os
import html2text

def parseURL(URL):
    parseKey = "99b97b1daefd55cf9805618152d665ae58fda6b4"
    getRequestURL = "https://www.readability.com/api/content/v1/parser?url=" + URL + "/&token=" + parseKey
    response = urllib.request.urlopen(getRequestURL).read().decode('utf-8')
    response = json.loads(response)
    postContent = bs4.BeautifulSoup(response["content"])
    return postContent

def createManPage(title, url):
    try:
        os.remove("/tmp/clipocket")
    except FileNotFoundError:
        pass

    manPage = open("/tmp/clipocket", "a+")
    manPage.write("Entry title: {}\n".format(title))
    manPage.write("URL: {}\n\n".format(url))
    manPage.writelines(html2text.html2text(parseURL(url).prettify()))
    manPage.close()
    os.system("less /tmp/clipocket")
    os.remove("/tmp/clipocket")
