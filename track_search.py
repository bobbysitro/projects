import urllib2
from BeautifulSoup import BeautifulSoup

print "<<<----Searching through the soup to find new tracks---->>>"

i = 1
# Fetch and parse the data
url = 'http://freshnewtracks.com/index.php'
data = urllib2.urlopen(url).read()
soup = BeautifulSoup(data)

for anchor in soup.findAll('a', title=True):
    print "#" +  str(i) + ":" + " Song: " + anchor['title']
    i = i + 1
