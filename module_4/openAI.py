#==================================================
#This file imports openai to connect to openAI API in order to send an API prompt
#It has a function that grabs 25 comments from comments.txt and puts each groups of 25 into an ai call
#to determine the sentiment of them individually.
#==================================================
import time
from openai import OpenAI

client = OpenAI(
    api_key="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",
)

def runAI(resultFilesPath, joinCommentPath):
    commentsWithinEach = 25
    commentLimit = 50
    
    with open(joinCommentPath, 'r', encoding='utf-8') as context, open(resultFilesPath, 'w') as resultsFile:
        comments = context.read().split('\n\n')#get each comment block
        totalComments = min(len(comments), commentLimit)#up to 50 comments
            
        for i in range(0, totalComments, commentsWithinEach):#for loop that goes to 50 comments in 25 increments
            endComment = min(i + commentsWithinEach, totalComments)#find end of comment
            currentComments = comments[i:endComment]#grab comment
            batchComment = '\n\n'.join(currentComments)#join to comment string
                
            user_prompt = (
                "What are the sentiments of these 25 comment blocks? "
                "You must answer each block of comments one by one with positive or negative only. Only anwser with neutral as a last resort. "
                "The number of your answers should match 25, the same as the comments given. The output is NOT numbered and sentiment of each comment should be listed on a newline."
                "Comments:\n" + batchComment
            )
                
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
            result = chat_completion.choices[0].message.content
            resultsFile.write(result + "\n")
            time.sleep(15)#avoid 3 calls per min