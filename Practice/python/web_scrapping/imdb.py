
import urllib2
from bs4 import BeautifulSoup

imdb250 = 'http://www.imdb.com/chart/top'
page = urllib2.urlopen(imdb250)
soup = BeautifulSoup( page,"html.parser")

#print soup.prettify()
trow = soup.find_all('td')
print type(trow)
print len(trow)
fmovie = trow[0]
print fmovie




