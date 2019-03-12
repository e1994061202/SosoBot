import urllib.request
from bs4 import BeautifulSoup
import ssl

class Pageb():
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.title = self.get_pageb()
        
    def get_pageb(self):
        page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(page, 'html.parser')
        trs  = soup.findAll("td", {"style" : "padding: 3px;width:33%"})
        trs = trs[0].find("a")
        return trs