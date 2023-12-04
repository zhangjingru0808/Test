# Project-1
## Using a reddit URL download the content into a text file

In the terminal, input the code:
```
python getURL.py your_URL
```
So the input would be: 
```
 python getURL.py "https://old.reddit.com/r/NintendoSwitch/comments/16ik507/mario_kart_8_deluxe_booster_course_pass_wave_6/"
```
This should output all the text data from the URL to the URL.txt file 

# Project-2 
## Using the URL text file you made in Project-1 extract the comments into a comment text file
In the terminal, input the code:
```
python extractComments.py URL.txt
```
This should extract all the comments and place them in the comment.txt file

# Project-4 
##  How to run our code
In the terminal, input the code:
```
python CS325_p4\\run.py
```
This should run the program and extract comments from the exisiting comments file and input them into openAI to be read and given a sentiment of negative, positive, or I don't know. 
It will return positive or negative based on the ChatGPT's analysis result and store into output file.

## Using the API to analyze the sentiment for each comment by ChatGPT stored into an output file.
Go to https://openai.com/ and login, you can login by google account, Microsoft account or Apple account, if you do not have any of these, just follow the sign up step by step.

After you login, click API it will lead you to the API main page

Click API keys in the left bar and click Create new secret key(if you already had one you can also use that), make sure you save your key somewhere because you cannot check the key again.

After that, open the openAI.py in the module_4 folder, or your with your own file paste "your key" into: client = OpenAI( api_key="your_key" ). This will allow us the user to connect to the OpenAI and call a simple API function call. 
```
chat_completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", 
                            "content": "What is the sentiment of the comment: " + commentText + " Only answer the question with positive or negative. If you are not sure, say I don't know."}
                        ]
                    )
```

Notice: Because of OpenAI limitation, for gpt-3.5, it can only process 3 comments per min, so it has to take PLENTY of time to finish if you have a big comments file. And each account can only do 1000 requests(comments) per month.

# Project-5
##  How to run our code
In the terminal, input the code:
```
python run.py readURL.txt
```
This should go through each URL located in readURL.txt. It extracts the comments from the URL and determines the sentiments of each comment. The limit of comments is 50.

Side Note: For this Project-5 we went all the way into folder CS325_p5 compared to Project-4 we stayed in ProjectReddit folder. So you do not need 'CS325_p4\\' to run this code.

# Project-6
## Creating Bar Graphs of the Sentiments
In the terminal, input the code:
```
python run.py readURL.txt
```
This should go through all the URL sentiment files and create a bar graph of each one.  
