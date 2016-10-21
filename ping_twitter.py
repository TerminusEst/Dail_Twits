import tweepy as tw



with open("api.keys", 'r') as f:

        keys = f.readlines()
        

for i, key in enumerate(keys):
        keys[i] = key.rstrip('\n')
        

auth = tw.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tw.API(auth)


