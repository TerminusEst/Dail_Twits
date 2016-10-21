import tweepy as tw
import pandas as pd
import seaborn as sns; sns.set()
import parties
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

df = df[df.Followers != 0]
df = df.sort(['Followers'])

legend_patches = []

for i in parties.colour:

	patch = mpatches.Patch(color=parties.colour[i], label=i)
	legend_patches.append(patch)


labels = [i.get_label() for i in legend_patches]

df.Followers.plot(kind='bar', color=df.Colour, fontsize=7)
plt.ylabel('Followers')
plt.legend(legend_patches, labels, loc=2)

plt.show()


df = df.sort(['Tweets'])
df.Tweets.plot(kind='bar', color=df.Colour, fontsize=7)
plt.ylabel('Tweets')
plt.legend(legend_patches, labels)


plt.show()


df = df[(df.Party != 'ULP') & (df.Party != 'CC') & (df.Party != 'WUA')]
df.boxplot(column='Followers', by='Party')

plt.ylim([0,30000])
plt.ylabel('Followers')
plt.show()


