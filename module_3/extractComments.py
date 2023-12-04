#==================================================
#This file has the function goComment which has a parameter of the comments.txt path
#that is passed into it that is retrieved from openFileRead.py but called in run.py
#This file goes through the contents of the URL.txt read file called from the openRead() function in 
#openFileRead.py and uses BeautifulSoup pulling data out of the text file by parsing
#It opens the comments.txt file that was passed into the parameter
#It goes through the whole file getting rid of <p> tags within block tags
#It also then goes through the whole file and finds the specific div class and div data-type and extracts only those
#specified comments and writes them to the comments.txt file 
#The comments.txt file is now full of only extracted comments from the URL.txt
#goComment() is a void function
#==================================================
from module_2 import openFileRead
def goComment(txtFile):
#open comment.txt and write to it
    parse = openFileRead.BeautifulSoup(openFileRead.openRead(),'html.parser')
    with open(txtFile, "w", encoding="utf-8") as file:
        #find all <blockquote> and remove <p> tags from them
        for blockTag in parse.find_all('blockquote'):
            pTagBlock = blockTag.find_all('p')
            for pTagQ in pTagBlock:
                pTagQ.extract()
    #find the <div> tags with data-type="comment"
        for divData in parse.select('div[data-type="comment"]'):
            divClass = divData.select_one('div[class="md"]') #selects one <div class="md"> 
            file.write('\n')
            if divClass: #if there
                pTags = divClass.find_all('p') #finds all pTags in that divTag
                for pTagDiv in pTags: #goes through all the <p> tags
                    file.write(pTagDiv.text + '\n') 