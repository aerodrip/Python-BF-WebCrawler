from functions import *
from classes import *


#crawlPBody(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'))


#writeToTXT(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'), 'newFile.txt', 'w')

header = ['id','title','address','telNr','linkUrl','imgUrl']
quelle = 'newfile.txt'
csv = 'dataset.csv'
x = 1


if(x==0):
    # create new csv
    useCSV(header, csv, 'create')
elif(x==1):
    crawlPBody(useTXT(str,quelle,'r'))
