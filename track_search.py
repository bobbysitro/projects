import re
from mechanize import Browser

br = Browser()
br.open("http://www.freshnewtracks.com")

# ...

# .links() optionally accepts the keyword args of .follow_/.find_link()
for link in br.links():
    print link
    br.follow_link(link)  # takes EITHER Link instance OR keyword args
    br.back()
