from bs4 import BeautifulSoup as soup #for pulling data out of HTML
import requests #requesting the url
import json #for parsing
import re


# okay, so the wesite im trying to scrape has some securty so i changed the header
# to a browser one so that the site does not detect me as a threat
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
my_url = 'https://todayinsci.com/2/2_01.htm'
page = requests.get(my_url, headers=headers)
# page_html = page.text
# The page is put into a jason object
# so that it can more easly parsed
soup = soup(page.text,"html.parser")

#################

myList = soup.find("div", attrs={"class":"daytable"})
print(len(myList))
patern = re.compile('<span class="sprite icon-calendar"></span>(.*?)<div class="bookline">', re.DOTALL)
for fact in myList:
    data = patern.findall(str(fact))
    info = re.sub(u'<.*?>','',str(data))
    if (len(info) != 2):
        sentence = info.replace('\\xa0', ' ')
        # print(sentence[9:-4])
        print(sentence)
    # print(type(fact))
