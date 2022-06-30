import requests
import tweepy
 
# API keyws 
api_key = "4Pdn1XCGiMfa5S2hGZYlywGvC"
api_secrets = "1r56dtQVLyJJBwsoAal3wpr58VdaHPwYzSecLJlbWVFylRFUfm"
access_token = "932754647902715905-n5MIkuOYluM8Ph0Ntl6bQs4q6sUqvoj"
access_secret = "hWvlvmO34aN7wgIIBeVttL02ChFiS8MDXgubpwZ7LVIhr"
 
# test method to Authenticate to Twitter

auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')



#method to get user input; test for authentication
#make sure user gives a valid input
user = api.get_user('LemsonMureya') # Store user as a variable
 
# Get user Twitter statistics
#what format is the data going to be in? should i jsonify it
print(f"user.followers_count: {user.followers_count}") #check documenation for what format the data is in
#print(f"user.listed_count: {user.listed_count}")
# print(f"user.statuses_count: {user.statuses_count}")
 
# Show followers; test method to see user followers
for follower in user.followers():
    print('Name: ' + str(follower.name))
    print('Username: ' + str(follower.screen_name))
 
# Follow a user; test if user being followed actually has an account
# api.create_friendship('wildebeestMedia')
 
# Get tweets from a user tmeline; test method and see if user actually has tweets
tweets = api.user_timeline(id='LemsonMureya', count=20)
# tweets_extended = api.user_timeline(id='LemsonMureya', tweet_mode='extended', count=20)
# print(tweets_extended)
 
# Like or retweet tweets
# id = 'id_of_tweet' # tweet ID; check if valid id
# tweet = api.get_status(id) # get tweets with specific id
# tweet.favorite() # Like a tweet
# tweet.retweet() # Retweet