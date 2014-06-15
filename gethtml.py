import bs4
import urllib.request

mobilizer = "http://www.readability.com/m?url="
postURL = "http://www.theverge.com/2014/6/13/5801022/cue-hopes-to-be-your-portable-personal-health-testing-lab"
url = mobilizer + postURL

response = urllib.request.urlopen(url)
html = response.read()
soup = bs4.BeautifulSoup(html)

pageTitle = soup.title.string
pageTitle = pageTitle[:-14]

pageURL = soup.find_all('a', attrs={"title": "View original article"})
for i in pageURL:
	pageURL = (i.get('href'))

print("Title -> {}".format(pageTitle))
print("Original URL -> {}".format(pageURL))

postContent = soup.find_all('section', attrs={"id": "rdb-article-content"})[0]

print(postContent.get_text())

