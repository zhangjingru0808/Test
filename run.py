from module_1 import getURL
#from module_2 import openFileRead
#from module_3 import extractComments
#from module_4 import openAI
from module_5 import graph
import os

commentTXTDir = 'Data/processed/'
directoryfolder = 'Data/Sentiments/'

def main():
    lines = 0
    inputpath = getURL.sys.argv[1]#input URL file txt
    with open(inputpath, 'r') as file:
        for line in file: 
            lines += 1 #set a value to record file number to name the resultFiles
            #getURL.retrieveURL(line)
            #joinCommentPath = os.path.join(commentTXTDir,f'comments{lines}.txt')
            #extractComments.goComment(joinCommentPath)
            resultFiles = os.path.join(directoryfolder, f'resultsFile{lines}.txt') #connects 'CS325_p4/Data/Sentiments/' with 'resultFiles1' to make the path
            #openAI.runAI(resultFiles, joinCommentPath)
            graph.pandaAndPlot(resultFiles, getURL.titleURL(line), lines)
main() 