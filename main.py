from functions import *
from classes import *


#crawlPBody(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'))


#writeToTXT(getPages('https://tel.search.ch/?was=coiffeur&wo=z%C3%BCrich'), 'newFile.txt', 'w')


crawlPBody(useTXT('newFile.txt', 'newFile.txt', 'r'))
