#==================================================
#This file imports BeautifulSoup to be used for extracting comments in extractComments.py
#This file's openRead() funtion opens the URL.txt, from the data path given in the getTxt string, to read the file 
#contents and store it in a html variable
#==================================================
from bs4 import BeautifulSoup #imported from miniconda
getTxt = 'Data/raw/URL.txt'
def openRead():
    with open(getTxt, "r", encoding="utf-8") as fileRead:
        html = fileRead.read()
        return html 