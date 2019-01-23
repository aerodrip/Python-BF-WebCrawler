from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json,os.path

url = "https://tel.search.ch/api/?was=Coiffeurgeschäft&wo=Kreis+6+%28Zürich%29&maxnum=200"
url1 = "https://tel.local.ch/de/q?what=Coiffeurgeschäft&where=Kreis+6+%28Zürich%29&maxnum=200"
url2 = 'https://tel.local.ch/de/q/Kreis%206%20(Zürich)/Coiffeurgeschäft.html?page=2'
url4 = 'https://tel.local.ch/de/q?what=Coiffeurgeschaeft'

#define vars
data = []
#ucount = 0


#define functions
#------- small functions --------
def striplogostring(string):
    return string.replace(' logo', '')


def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


def getnewurl(url):
    your_counter = get_var_value()
    print("This script has been run {} times.".format(your_counter))
    url = url + "?page=" + str(your_counter)
    return url


def countpages(url):
    print(url)
    url = getnewurl(url)
    print(url)


#------- doc functions ----------
def readjson(filename):
    with open(filename, 'r') as jsonFile:
        for object in jsonFile:
            print(object)


def writejson(data, filename):
    with open(filename, 'w') as jsonFile:
        json.dump(data, jsonFile)


def writeTXT(data, filename):
    with open(filename, "w") as file:
        for line in data:
            file.write(str(line))


def readTXT(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)


def writecsv(data, filename):
    headers = "title_name;imgSrc\n"

    with open(filename, "w") as file:
        file_exists = os.path.isfile(filename)
        if file_exists != True:
            file.write(headers)

        for line in data:
            title = line[0]["title"]
            imgSrc = line[1]["imgSrc"]
            file.write(title+";"+imgSrc + "\n")


def readcsv(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line)


#------- crawler functions ------
def crawlStudio(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "listing-container"})


    # iterate through all container Objects
    for container in containers:
        obj = []
        # get the title & imgSrc
        try:
            title = striplogostring(container.a.img["alt"])
            imgSrc = "https:" + container.a.img["src"]
        except:
            print('has no img')
        obj.append({"title":title})
        obj.append({"imgSrc":imgSrc})
        data.append(obj)
    # This function returns the following
    return data


# MAIN SOFTWARE

data = crawlStudio(url4)
writecsv(data, "dataFile.csv")

#writecsv(crawlStudio(str(countpages(url4))), "dataFile.csv")

countpages(url4)
