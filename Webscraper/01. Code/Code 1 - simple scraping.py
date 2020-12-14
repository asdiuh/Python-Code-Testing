from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)

title_index = html.find("<title>")

start_index = title_index + len("<title>")

end_index = html.find("</title>")

end_index

title = html[start_index:end_index]

#########################################################################
#########################################################################
#########################################################################
######################################################################### 
# new run for poseidon where table <title> is mis-spelt

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)

title_index = html.find("<title>")

start_index = title_index + len("<title>")

end_index = html.find("</title>")

end_index

title = html[start_index:end_index]

#########################################################################
#########################################################################
#########################################################################
######################################################################### 
# where instead of using find, use regexpressions
# <ab*c> = will find ac, abc, abbc, abbbc, abbbbc, etc
# <a.*c> = will find a?c, a??c, a???c, a????c (longest string) 
# <a.*?c> = will find a?c (shortest string)

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)
# pattern we will look at is beginning and ending of title html
pattern = "<title.*?>.*?</title.*?>"

match_results = re.search(pattern, html, re.IGNORECASE)

title = match_results.group()

title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)

#########################################################################
#########################################################################
#########################################################################
#########################################################################
# using beautiful soup

from bs4 import BeautifulSoup
from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"

url = "https://www.reddit.com/r/OutOfTheLoop/comments/k6vysl/whats_going_on_with_dragon_age_actor_greg_ellis/"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.find_all("img")

soup.title

soup.title.string

# beautifulsoup wont be able to interact with 

import mechanicalsoup  
browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text
print(f"the result of your dice roll is: {result}")

url = "http://olympus.realpython.org/login"
page = browser.get(url)
type(page.soup)
page.soup