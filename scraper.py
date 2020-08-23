#Scrapes Rank, Title and Time from HN Posts and saves in database
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://news.ycombinator.com/"
uClient = uReq(my_url)  # opens stream and grabs webpage
page_html = uClient.read() # stores into variable
uClient.close() # closes stream

page = soup(page_html, "html.parser") # parses HTML file
table = page.find("table", {"class":"itemlist"}).findAll("tr", {"class":"athing"})
subtext = page.findAll("td", {"class":"subtext"})

titles = []
ranks = []
for athing in table:
    rank = athing.find("span", {"class":"rank"}).text.strip()[:-1]
    text = athing.find("a", {"class":"storylink"}).text.strip()
    ranks.append(rank)
    titles.append(text)

times = []
for x in subtext:
    time = x.find("span", {"class":"age"}).text.strip()
    times.append(time)

final = []
for i in range (0 , len(titles)):
    final.append([ranks[i],titles[i],times[i]]) 