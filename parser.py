import bs4
import urllib.request
import json
import os

def parseURL(URL):
    parseKey = "99b97b1daefd55cf9805618152d665ae58fda6b4"
    getRequestURL = "https://www.readability.com/api/content/v1/parser?url=" + URL + "/&token=" + parseKey
    response = urllib.request.urlopen(getRequestURL).read().decode('utf-8')
    response = json.loads(response)
    postContent = bs4.BeautifulSoup(response["content"])
    return postContent.get_text()

def createManPage(title, url):
    manPage = open("/tmp/clipocket", "a+")
    manPage.write('.TH "clipocket"\n')
    manPage.write('.SH "{}"\n'.format(title))
    manPage.write('{}\n'.format(parseURL(url)))
    manPage.write('.SH "Original link"\n')
    manPage.write('{}\n'.format(url))
    manPage.close()
    os.system("groff -Tutf8 -man /tmp/clipocket > /tmp/clipocket.1")
    os.system("man /tmp/clipocket.1")
    os.system("rm /tmp/clipocket*")
    os.system("clear")
