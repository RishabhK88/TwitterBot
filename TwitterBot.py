import tweepy

consumer_key = "ZJaj0TpG8ngUl3k47mXakbEK5"
consumer_secret = "5jNopjaWWJwvKJfpLKsO0kaYetutxys9YTj628C6sN8CJs1Ekp"
access_token = "1137258859788025856-k5nWb8wwhE890inSkyLv1zxXTsRtma"
access_token_secret = "Ukftq6iabV5CaPgVwl1MAXfBSzznhPmFyXbXq5yk02d6x"

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