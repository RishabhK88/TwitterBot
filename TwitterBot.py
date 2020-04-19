import tweepy

# The below key and tokens are specific to you and you can get those for your twitter account
consumer_key = "Enter your consumer key here"
consumer_secret = "Enter you consumer secret key here"
access_token = "Enter your access token here"
access_token_secret = "Enter your access token secret key here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print(user.name)

for follower in tweepy.Cursor(api.followers).items():
	follower.follow()    
print("Followed everyone that is following " + user.name)


def mainFunction():
	search = ["political", "comedy"]
	numberOfTweets = 1

	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):    
		try:        
			tweet.retweet()        
			tweet.favorite()
			print('Retweeted the tweet')
		except tweepy.TweepError as e:        
		 	print(e.reason)
		except StopIteration:
			break


	tweetId = tweet.user.id
	username = tweet.user.screen_name
	phrase = "Heyy, Wassup?"

	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):            
		try:                
			tweetId = tweet.user.id                
			username = tweet.user.screen_name                
			api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)                
			print ("Replied with " + phrase)                       
		except tweepy.TweepError as e:                
			print(e.reason)
		except StopIteration:
		 	break


mainFunction()
