import tweepy as tw
import pandas as pd
import parties

def stats(handle):
	
	
	try:	
		user = api.get_user(handle)
		
		out = pd.Series({'Followers':user.followers_count, 
                                 'Tweets':user.statuses_count,
			         'Created':user.created_at})
	except:
		out = pd.Series({'Followers':0, 'Tweets':0, 'Created':0})

	return out


with open("api.keys", 'r') as f:

        keys = f.readlines()
        

for i, key in enumerate(keys):
        keys[i] = key.rstrip('\n')
        

auth = tw.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tw.API(auth)


df = pd.read_csv('twits.csv')

df['Colour'] = df['Party'].map(parties.colour)

none_series = pd.Series({'Followers': 0, 'Tweets':0, 'Created':0})

df[['Followers', 'Tweets', 'Created']] = df.Handle.apply(lambda x: stats(x) if x != None else none_series)
	

#df.to_csv('twit_stats.csv')

