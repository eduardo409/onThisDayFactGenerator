from bs4 import BeautifulSoup as soup #for pulling data out of HTML
import requests #requesting the url
import json #for parsing
import re

class webscraper():
    def __init__(self, month, day):
        self.factList = []
        self.month = month
        self.day = day
        # okay, so the wesite im trying to scrape has some securty so i changed the header
        # to a browser one so that the site does not detect me as a threat
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
        self.factList = self.genFactList(self.month, self.day)


    def genFactList(self, month, day):
        list = []
        # the followiing line is to get the proper date sytax for url usage. format = 01, 02....09
        if day < 10:
            day = '0'+str(day)
        my_url = 'https://todayinsci.com/'+str(month)+'/'+str(month)+'_'+day+'.htm'
        page = requests.get(my_url, headers=self.headers)
        mysoup = soup(page.text,"html.parser")
        myList = mysoup.find("div", attrs={"class":"daytable"})

        #  ISSUE: looking for a better srapping methon
        # this one is picking up some unwanted characters
        patern = re.compile('<span class="sprite icon-calendar"></span>(.*?)<div class="bookline">', re.DOTALL)
        for fact in myList:
            data = patern.findall(str(fact))
            info = re.sub(u'<.*?>','',str(data))
            if (len(info) != 2):
                sentence = info.replace('\\xa0', '')
                sentence = sentence.replace('\\n', '')
                sentence = sentence.replace('[\'', '')
                sentence = sentence.replace('\']', '')
                list.append(sentence)
        return list
# if __name__ == "__main__":
#     scrap = webscraper(1,1)
#     print(scrap.factList[0])
