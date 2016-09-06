import urllib.request
from html.parser import HTMLParser

userText = []

class ParseText(HTMLParser):
    def handle_data(self, data):
        if data!="\n":
            userText.append(data)


thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"

handle = urllib.request.urlopen(thisurl)

html_gunk = handle.read()

#parse source code to data
lParser = ParseText()

#feed data
lParser.feed(str(html_gunk))
lParser.close()

for text in userText:
    if text.strip()!='\\n':
        if len(text)>0:
            print(text)

