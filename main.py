from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import os
import lxml

url = 'https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich&=maxnum2000'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#containers = page_soup.findAll("div", {"class": "listing-container"})

soup_level1 = soup(page_html, 'lxml')
#container = soup_level1.find("div", {"class": "sl-loadmore-section"})
#containers = soup_level1.findall("table", {"class": "tel-resultentry"})

containers = page_soup.find_all('table')

datalist = [] #empty list
x = 0 #counter

for container in containers:
    ##code to execute in for loop goes here
    print(container.a.img['alt'])
