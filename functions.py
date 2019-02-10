from classes import *
import csv
from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time


def useTXT(str, filename, argument):
    if argument == 'w':
        file_object = open(filename, 'w')
        file_object.write(str)
        file_object.close()
    elif argument == 'r':
        file_object = open(filename, 'r')
        return file_object
        file_object.close()


def useCSV(str, filename, argument):
    if argument == 'w':
        file_object = open(filename, 'w')
        file_object.write(str)
        file_object.close()
    elif argument == 'r':
        file_object = open(filename, 'r')
        return file_object
        file_object.close()
    elif argument == 'a':
        #file_object = open(filename, 'a', newline='')
        #file_object.writelines(str)
        #file_object.close()
        with open(filename, 'a', newline='') as file_object:
            wr = csv.writer(file_object, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(str)
    elif argument == 'create':
        #file_object = open(filename, 'w', newline='')
        #file_object.write(str)
        #file_object.close()
        with open(filename, 'w', newline='') as file_object:
            wr = csv.writer(file_object, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(str)


def crawlUrl(url):
    # @description: Opens a url and scrapes for Coiffeur Studio Information
    # @input: url as String
    # @output: none
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


def getPages(startUrl):
    # @description: AutoScroll to the Bottom of page and return innerHTML of body as String
    # @input: Url as String
    # @output: innerHTML of bodyas String
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

    # HTML Content of page as String to pBody and return it
    pBody = driver.page_source
    return pBody

    driver.close()


def crawlPBody(bodyStr):
    # @description: takes HTML as String and makes it useable in Beautifulsoup. And then scrapes for Coiffeur Studio
    #               information.
    # @input: HTML as String
    # @output: none
    id = 0
    page_soup = soup(bodyStr, 'html.parser')
    containers = page_soup.find_all('table')

    datalist = [] #empty list
    #x = 0 #counter
    #print("Startwert: " + str(x))
    for container in containers:
        #x += 1
        #print("-------- Container " + str(x) + " ----------")
        try:
            title = container.find("img")["alt"]
            address = container.find("div", {'class': 'tel-address'}).get_text()
            # plz = container.find("span", {'class': 'postal-code'})
            # locality = container.find('span', {'class': 'locality'})
            telNr = container.find('div', {'class': 'tel-number'}).span.a.get_text()
        except:
            title = ""
        try:
            hrefs = container.find_all('a')
            imgUrl = "https://tel.search.ch" + hrefs[0].img['src']
            linkUrl = ""
            for href in hrefs:
                if href.get_text().__contains__('www.'):
                    linkUrl = href.get_text()

        except:
            hrefs = ""

        # Create new Studio Object and print Object Description
        id += 1
        objList = []
        objList.append(id)
        objList.append(title)
        objList.append(address)
        objList.append(telNr)
        objList.append(linkUrl)
        objList.append(imgUrl)

        csv = 'dataset.csv'

        useCSV(objList, csv, 'a')

        obj = Studio(id, title, address, telNr, linkUrl, imgUrl)
        obj.getBeschreibung()



