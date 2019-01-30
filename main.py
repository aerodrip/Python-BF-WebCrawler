from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time, re, os, lxml
import pandas as pd


def writeToTXT(str, filename, argument):
    if argument == 'w':
        file_object = open(filename, 'w')
        file_object.write(str)
        file_object.close()
    elif argument == 'r':
        file_object = open(filename, 'r')
        return file_object
        file_object.close()



def getPages(startUrl):
    driver = webdriver.Safari()
    driver.get(startUrl)

    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    pBody = driver.page_source
    return pBody

    driver.close()


def crawlUrl(url):
    url = 'https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.find_all('table')

    datalist = [] #empty list
    x = 0 #counter
    print("Startwert: " + str(x))
    for container in containers:
        x += 1
        print("-------- Container " + str(x) + " ----------")
        try:
            title = container.find("img")["alt"]
            address = container.find("div", {'class': 'tel-address'}).get_text()
            plz = container.find("span", {'class': 'postal-code'})
            locality = container.find('span', {'class': 'locality'})
            telNr = container.find('div', {'class': 'tel-number'}).span.a.get_text()
        except:
            title = ""
        try:
            hrefs = container.find_all('a')
            imgSrc = "https://tel.search.ch" + hrefs[0].img['src']
            lnk = ""
            for href in hrefs:
                if href.get_text().__contains__('www.'):
                    lnk = href.get_text()

        except:
            hrefs = ""

        print("Title:   " + title)
        print("Address: "+ address)
        print("Tel:     " + telNr)
        print("Link:    " + lnk)
        print("Bild:    " + imgSrc)
        print("")
        print(container.prettify())

def crawlPBody(bodyStr):
    page_soup = soup(bodyStr, 'html.parser')
    containers = page_soup.find_all('table')

    datalist = [] #empty list
    x = 0 #counter
    print("Startwert: " + str(x))
    for container in containers:
        x += 1
        print("-------- Container " + str(x) + " ----------")
        try:
            title = container.find("img")["alt"]
            address = container.find("div", {'class': 'tel-address'}).get_text()
            plz = container.find("span", {'class': 'postal-code'})
            locality = container.find('span', {'class': 'locality'})
            telNr = container.find('div', {'class': 'tel-number'}).span.a.get_text()
        except:
            title = ""
        try:
            hrefs = container.find_all('a')
            imgSrc = "https://tel.search.ch" + hrefs[0].img['src']
            lnk = ""
            for href in hrefs:
                if href.get_text().__contains__('www.'):
                    lnk = href.get_text()

        except:
            hrefs = ""

        print("Title:   " + title)
        print("Address: "+ address)
        print("Tel:     " + telNr)
        print("Link:    " + lnk)
        print("Bild:    " + imgSrc)
        print("")
        #print(container.prettify())


#crawlPBody(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'))


#writeToTXT(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'), 'newFile.txt', 'w')

crawlPBody(writeToTXT('newFile.txt', 'newFile.txt', 'r'))
