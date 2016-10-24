import tweepy as tw
import pandas as pd
import parties

def stats(handle):
	
	print(handle)
	try:	
		user = api.get_user(handle)

		followers = user.followers_count
		tweets    = user.statuses_count
		out = pd.Series({'Followers':followers, 'Tweets':tweets})
	except:
		out = pd.Series({'Followers':0, 'Tweets':0})

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

none_series = pd.Series({'Followers': 0, 'Tweets':0})

df[['Followers', 'Tweets']] = df.Handle.apply(lambda x: stats(x) if x != None else none_series)
	
df = df.set_index(df.Name)

df.to_csv('twit_stats.csv')
