import tweepy
import time
print('this is my twitter bot')

CONSUMER_KEY = 'puJsx2ndvvXsnaZds0GtKrePW'
CONSUMER_SECRET = 'UPBYrinotmG6VkfIwrDWXUNBMo8Po4d3n9bCwPg6aqk2ss2KIX'
ACCESS_KEY = '1108309959056523264-uMCbmt5S4M11cet1F8ULED6dUJ95fv'
ACCESS_SECRET = 'FLVxHVZ7GJkRKtwTsTIxP88fHKeF7kJ1bgPSxvWgnSe4g'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)  # api object to talk(read and wirte data) to twitter

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    a = int(f_read.read().strip())
    f_read.close()
    return a

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweet():
    last_seen_id    = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended') 
    #this is function from tweepy lib
    #the id passed to this function will be skipped.
    #the tweets are stored as stacks. the first tweet goes to the bottom [n-1] and the latest with index [0]

    #once you run the script the latest tweet's id will be stored in the .txt file and when we further run the script no tweets will be displayed.
    #if you another tweet after running the python shell then it wont show up so restart the shell
    #TEST- If we put the id of tweet[2] in the .txt file then the output will show the tweet[1] and tweet[0] #latest
    for mention in reversed(mentions):
        print(str(mention.id) + "-" + mention.full_text)
        latest_id = mention.id                   #replace 
        store_last_seen_id(latest_id,FILE_NAME)  #store
        if '#helloworld' in mention.full_text.lower():   #check
            print("FOUND")
            print('RESPONDING BACK... ')
            api.update_status( '@'+mention.user.screen_name +'#hell to you',mention.id)
            
    #to respond to a tweet use api.update.status()
    
while True:
    reply_to_tweet()
    time.sleep(5)   #stop the process for 5 seconds and start again
                    #so it means reply every 5 seconds