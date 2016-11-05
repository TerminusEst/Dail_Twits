import urllib.request as urlreq
import html


url = "https://www.kildarestreet.com/tds/"
response = urlreq.urlopen(url)
webpage = response.readlines()

names, parties, twits = [], [], []
for index, value in enumerate(webpage):

	value = html.unescape(value.decode('utf-8'))
	try:
		if "/td/" in value:

			name = value.split('"')[-1][1:].split("<")[0]

			names.append(name)                

			address = value.split('"')[3]
			next_line = html.unescape(webpage[index + 1].decode('utf-8'))
			party = next_line.split(">")[1].split("<")[0]    
			
			parties.append(party)	

			url2 = "https://www.kildarestreet.com" + address
			response2 = urlreq.urlopen(url2)
			webpage2 = response2.readlines()

			twit_switch = False
			for line_feed in webpage2:
				line_feed = html.unescape(line_feed.decode('utf-8'))				

				if "http://twitter" in line_feed:

					twitter_add = line_feed.split('http://twitter.com/')[1].split('"')[0]
					twit_switch = True
					break
				
			if twit_switch == False:
				twitter_add = None

			twits.append(twitter_add)

	
	except:
		continue

f = open('twits.csv', 'w')

for i in range(len(names)):
    f.write(names[i] +','+parties[i]+','+str(twits[i])+'\n')

f.close()


