import os
import pandas
import matplotlib.pyplot as plt

def pandaAndPlot(sentimentFile, title, lineCount):
    #panda opens, reads, and parses so we dont have to open file
    dataFrame = pandas.read_csv(sentimentFile, header= None, names=['Sentiments']) #set header
    
    dataFrame['Sentiments'] = dataFrame['Sentiments'].str.lower() #make all sentiments consietent
    dataFrame['Sentiments'] = dataFrame['Sentiments'].str.strip() #gets rid of white spaces
    numOfSentiments = dataFrame['Sentiments'].value_counts() #counts num of comments per sentiment
    
    plt.figure(figsize=(10,6)) #size of graph
    colors = {'positive': 'green', 'negative': 'red', 'neutral':'purple'}
    
    plt.bar(numOfSentiments.index, numOfSentiments.values, color=[colors.get(x)for x in numOfSentiments.index])
    
    plt.xlabel('Sentiments')
    plt.ylabel('Count')
    plt.title(title)
    
    legendForGraph = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in colors]
    plt.legend(legendForGraph, colors.keys()) #add legend
    
    combine = os.path.join('Data/Plots', f'word_count_plot{lineCount}.png')
    plt.savefig(combine)