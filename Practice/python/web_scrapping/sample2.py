
#import urllib2
from bs4 import BeautifulSoup
import requests
import re

# request the webpage
url = 'http://www.imdb.com/chart/top'
req = requests.get(url)
page = req.text

soup = BeautifulSoup(page, 'html.parser')
#print soup.prettify()
# get top 250 movie names and years, may take ~30 seconds
movie_names = []
movie_year = [0] * 250

j = 0
for i in range(250):
    content = str(soup.findAll('td', {'class':'titleColumn'})[i])
    content = content.decode("UTF-8")#.encode("ASCII")
    name = re.findall ( '>(.*?)</a>', content)
    movie_names.insert(len(movie_names), name)
    
    year = str(soup.findAll('span', {'class':'secondaryInfo'})[i])
    movie_year[i] = int(re.findall(r"\(([0-9_]+)\)", year)[0])
 
# keep track of the progress   
print('We now have ' + str(j) + ' movies') 
j = j+1



print movie_names
print len(movie_names)
print movie_year