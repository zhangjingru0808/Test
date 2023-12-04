#==================================================
#This file passes the URL into it and retrieves it from Reddit
#From there it determines if it successful grabbed the page from Reddit, it keeps looping till it does
#It prints the contents of the url into the URL.txt located in raw
#==================================================
import requests #imported from miniconda
import sys #included in STD library
getTxt = 'Data/raw/URL.txt'

def retrieveURL(url):
    outputFile = open(getTxt,"w",encoding="utf-8")
    while True:
        try:
            getURL=requests.get(url)
            getURL.raise_for_status()
            if "Too Many Requests" in getURL.text:
                print("Error pending")
            else:
                outputFile.writelines(getURL.text)
                print("Success")
                break
        except requests.RequestException as e:
            print("Error retrieving from Reddit")
    outputFile.close()
    
def titleURL(url):
    urlDivided = url.split("/")
    findComments = urlDivided.index("comments")
    title = urlDivided[findComments+2]
    if title:
        title = ' '.join([word.capitalize()for word in title.split('_')])
        return title
    return title