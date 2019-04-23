# Scraping a Website

# Importing Libraries
import pandas as pd
import os as os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

quote_page = "https://www.basketball-reference.com/contracts/players.html"


# Parse the html using beautiful soup and store in variable "soup"
soup = make_soup(quote_page)
print(soup.title.text)
playerdata, playerdatasaved = "",""

for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll('td'):
        playerdata = playerdata + ";" + data.text
    if len(playerdata) != 0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]
delimiter = "    
header = "Player;Tm;2018-19;2019-20;2020-2021;2021-2022;2022-2023;2023-2024;Signed Using;Guaranteed"
file = open(os.path.expanduser("Basketball_salaries.csv"),"wb")
file.write(bytes(header,encoding = "ascii",errors="ignore"))
file.write(bytes(playerdatasaved,encoding = "ascii",errors="ignore"))