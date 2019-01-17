from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://tel.search.ch/api/?was=Coiffeurgeschäft&wo=Kreis+6+%28Zürich%29&maxnum=200"
url1 = "https://tel.local.ch/de/q?what=Coiffeurgeschäft&where=Kreis+6+%28Zürich%29&maxnum=200"
url2 = 'https://tel.local.ch/de/q/Kreis%206%20(Zürich)/Coiffeurgeschäft.html?page=2'
url3 = "https://google.ch"
url4 = 'https://tel.local.ch/de/q?what=Coiffeurgeschaeft'


uClient = uReq(url4)
page_html = uClient.read()

uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "listing-container"})

for container in containers:
    #title = container.h2.img.span.text
    #print(title)
    #print(container.h2.img.span.text)
    print(container.div.a)
