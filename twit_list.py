# -*- coding: utf-8 -*-
import urllib2
import HTMLParser
pars = HTMLParser.HTMLParser()

"""
def GetTwitterFollowers(html):
	for i in html3:
		if 'data-nav="followers"' in i:
			followers = i.split('title="')[1].split(" F")[0]
			followers = int(followers.replace(",", ""))

			return followers

	return 0


url = "https://www.kildarestreet.com/tds/"
response = urllib2.urlopen(url)
html = response.readlines()

names, parties, follower_numb = [], [], []
twits = []
for index, value in enumerate(html):
	try:
		if "/td/" in value:
			name = pars.unescape(value.split('"')[-1][1:].split("<")[0])

			address = value.split('"')[3]
			party = html[index + 1].split(">")[1].split("<")[0]

			url2 = "https://www.kildarestreet.com" + address
			response2 = urllib2.urlopen(url2)
			html2 = response2.readlines()
		
			twit_switch = False
			for j in html2:
				if "http://twitter" in j:

					twitter_add = j.split('http://twitter.com/')[1].split('"')[0]
					twit_switch = True

					response3 = urllib2.urlopen("https://twitter.com/" + twitter_add)
					html3 = response3.readlines()
					followers = GetTwitterFollowers(html3)
					break

			if twit_switch == False:
				followers = 0
			print name, party, followers


			names.append(name)
			parties.append(party)
			follower_numb.append(followers)

	except:
		continue
"""

a = {"FG": "Fine Gael", "LAB": "Labour Party", "FF": "Fianna Fáil", "SF":"Sinn Féin", "AAA":"Ant-Austerity Alliance", "CC":"Ceann Comhairle", "GRN":"Green Party", "IND":"Independents", "PBP":"People Before Profits", "SD":"Social Democrats", "ULP":"United Labour Party", "WUA":"Workers and Unemployed Action"}

b = {"FG": "#6699FF", "LAB": "#CC0000", "FF": "#66BB66", "SF":"#008800", "AAA":"#E5E500", "CC":"yellow", "GRN":"#99CC33", "IND":"Black", "PBP":"#E5E500", "SD":"#752F8B", "ULP":"#CC0000", "WUA":"#D73D3D"}


follower_numb2, names2, parties2 = zip(*sorted(zip(follower_numb, names, parties)))


x_axis = arange(len(follower_numb2))

width = 1

clf()

ax = subplot(111)

barlist = bar(x_axis, follower_numb2, width, edgecolor = "k", linewidth = 1, log= False)

for index, value in enumerate(barlist):
	barlist[index].set_color(b[parties2[index]])

xticks(x_axis + 0.5)
ax.set_xticklabels(names2, rotation = 90)

show()












