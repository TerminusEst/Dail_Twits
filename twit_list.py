import urllib
#import HTMLParser
#pars = HTMLParser.HTMLParser()


url = "https://www.kildarestreet.com/tds/"
response = urllib.request.urlopen(url)
html = response.readlines()

names, parties = [], []
for index, value in enumerate(html):

        value = value.decode()
        try:
                if "/td/" in value:

                        name = value.split('"')[-1][1:].split("<")[0]
                        names.append(name)                
                       # address = value.split('"')[3]
                       # party = html[index + 1].split(">")[1].split("<")[0]    
                        print(name, party)
        except:
                continue
