from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
	return 100*float(part)/float(whole)
#Enter key from twitter developer account
consumerkey =" "
consumerSecert =" "
accesstoken =" "
accessTokenSecret =" "
#authorisation and access
auth = tweepy.OAuthHandler(consumer_key = consumerkey, consumer_secret = consumerSecert)
auth.set_access_token(accesstoken,accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter your keyword :")
noOfsearchTerm = int(input("Enter how many tweet to analyze:"))

tweets = tweepy.Cursor(api.search, q = searchTerm, Lang="English").items(noOfsearchTerm)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
        
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
        	neutral += 1
        elif (analysis.sentiment.polarity < 0):
        	negative += 1 
        elif (analysis.sentiment.polarity > 0):
        	positive += 1

positive = percentage(positive, noOfsearchTerm)
negative = percentage(negative, noOfsearchTerm)
neutral =  percentage(neutral, noOfsearchTerm)

positive = format(positive, '.2f')
negative = format(negative, ".2f")
neutral = format(neutral, ".2f")        

print('how people are reacting on '+searchTerm+' by analyzing '+str(noOfsearchTerm) +' tweets')

if (polarity ==0):
	print("neutral")
elif(polarity < 0):
	print("negative")
elif(polarity > 0):
	print("positive")

labels = ['positive ['+str(positive)+'%]', 'neutral ['+str(neutral)+'%]', 'negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen' , 'gold', 'red']
patches,texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('how people are reacting on ' +searchTerm+' by analyzing '+str(noOfsearchTerm)+' Tweet')
plt.axis('equal')
plt.tight_layout()
plt.show()
