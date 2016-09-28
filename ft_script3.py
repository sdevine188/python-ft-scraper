__author__ = 'Steve'

## import libraries
from lxml import html, etree
import requests
import re
import os
import datetime


# set working directory
#%cd c://users//stephen//desktop//python
#%ls
#%pwd
os.chdir("c:/users/stephen/desktop/python/python-ft-scraper")

## enter api key as string
api_key = "hNIqHozr1JA4f2mU0uDZA2GkZfVzhpQC"

# example api call
# http://api.ft.com/content/c0dda1cc-664f-11e6-8310-ecf0bddad227?apiKey=hNIqHozr1JA4f2mU0uDZA2GkZfVzhpQC

# print page text
# print(africa_page.text)

# us section
us_links = []
while us_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    us_page = s.get("http://www.ft.com/world/us")
    us_tree = etree.HTML(us_page.text)
    us_items_links = us_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    us_lead_links_medium = us_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    us_lead_links_large = us_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    us_links = us_items_links + us_lead_links_medium + us_lead_links_large
print(us_links)

# africa section
africa_links = []
while africa_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    africa_page = s.get("http://www.ft.com/world/africa")
    africa_tree = etree.HTML(africa_page.text)
    africa_items_links = africa_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    africa_lead_links_medium = africa_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    africa_lead_links_large = africa_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    africa_links = africa_items_links + africa_lead_links_medium + africa_lead_links_large
print(africa_links)

# americas section
americas_links = []
while americas_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    americas_page = s.get("http://www.ft.com/world/americas")
    americas_tree = etree.HTML(americas_page.text)
    americas_items_links = americas_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    americas_lead_links_medium = americas_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    americas_lead_links_large = americas_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    americas_links = americas_items_links + americas_lead_links_medium + americas_lead_links_large
print(americas_links)

# asia-pacific section
asia_pacific_links = []
while asia_pacific_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    asia_pacific_page = s.get("http://www.ft.com/world/asia-pacific")
    asia_pacific_tree = etree.HTML(asia_pacific_page.text)
    asia_pacific_items_links = asia_pacific_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    asia_pacific_lead_links_medium = asia_pacific_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    asia_pacific_lead_links_large = asia_pacific_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    asia_pacific_links = asia_pacific_items_links + asia_pacific_lead_links_medium + asia_pacific_lead_links_large
print(asia_pacific_links)

# europe section
europe_links = []
while europe_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    europe_page = s.get("http://www.ft.com/world/europe")
    europe_tree = etree.HTML(europe_page.text)
    europe_items_links = europe_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    europe_lead_links_medium = europe_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    europe_lead_links_large = europe_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    europe_links = europe_items_links + europe_lead_links_medium + europe_lead_links_large
print(europe_links)

# mideast section
mideast_links = []
while mideast_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    mideast_page = s.get("http://www.ft.com/world/mideast")
    mideast_tree = etree.HTML(mideast_page.text)
    mideast_items_links = mideast_tree.xpath("""//li[@class='ft-list-item']/a/@href""")
    mideast_lead_links_medium = mideast_tree.xpath("""//h3[@class = 'ft-title ft-title-medium ft-spc-btm-qtr']/a/@href""")
    mideast_lead_links_large = mideast_tree.xpath("""//h3[@class = 'ft-title ft-title-large ft-spc-btm-qtr']/a/@href""")
    mideast_links = mideast_items_links + mideast_lead_links_medium + mideast_lead_links_large
print(mideast_links) 

# comment section
comment_links = []
while comment_links == []:
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    comment_page = s.get("http://www.ft.com/comment")
    comment_tree = etree.HTML(comment_page.text)
    # for some reason, the comments site is not parsing like the others
    # the content url after the columnist name works, but there are two name entries for each 
    # columnist, so you need to ignore the url that does not contain content
    comment_urls = comment_tree.xpath("""//a/@href""")
    columnists = ["edluce", "lawrence-summers", "wolfgang-munchau", "philip-stephens", "gideonrachman",
                  "janan-ganesh", "davidpilling", "robert-shrimsley", "gillian-tett", "martin-wolf"]
    columnist_urls = []
    columnist_flag = 0
    for columnist in columnists:
        for url in comment_urls:
            if(columnist_flag == 1):
                columnist_urls.append(url)
                columnist_flag = 0
            if(url.find(columnist) > 0):
                columnist_flag = 1
    columnist_urls = list(set(columnist_urls))
    comment_links = []
    for url in columnist_urls:
        string = "content"
        if(url.find(string) > 0):
            full_url = "http://www.ft.com/cms/s/0/" + url + ".html"
            comment_links.append(full_url)
print(comment_links)
            
## compile all the section links into one list
section_links = us_links + europe_links + asia_pacific_links + mideast_links + africa_links + americas_links + comment_links
#section_links = list(set(section_links))

## create variables for total number of articles and range of each section's article count
total_articles = len(section_links) + 1

range_us = range(len(us_links))
range_europe = range(range_us[-1] + 1, range_us[-1] + 1 + len(europe_links))
range_asia_pacific = range(range_us[-1] + 1 + len(europe_links), 
        range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links))
range_mideast = range(range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links), 
        range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + len(mideast_links))
range_africa = range(range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + 
    len(mideast_links), range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + 
    len(mideast_links) + len(africa_links))
range_americas = range(range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + 
    len(mideast_links) + len(africa_links), range_us[-1] + 1 + len(europe_links) + 
    len(asia_pacific_links) + len(mideast_links) + len(africa_links) + len(americas_links))
range_comment = range(range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + 
    len(mideast_links) + len(africa_links) + len(americas_links), 
    range_us[-1] + 1 + len(europe_links) + len(asia_pacific_links) + len(mideast_links) + 
    len(africa_links) + len(americas_links) + len(comment_links)) 

## fetch articles from each section of the paper and append to text file
text = []
match_articles = []
current_date = datetime.datetime.now()
current_date = current_date.isoformat()[0:10]

article_number = 0
for i in range(len(section_links)):
        article = section_links[i]
        article_id = article[(article.rfind("/")+1) : article.rfind(".html")]
        article_url = "http://api.ft.com/content/" + article_id + "?apiKey=" + api_key
        
        article_section = ""
        if i in range_us:
                article_section = "U.S. section"
        elif i in range_europe:
                article_section = "Europe Section"
        elif i in range_asia_pacific:
                article_section = "Asia-Pacific Section"
        elif i in range_mideast:
                article_section = "Middle East and North Africa Section"
        elif i in range_africa:
                article_section = "Africa Section"
        elif i in range_americas:
                article_section = "Americas Section"
        elif i in range_comment:
                article_section = "Comment Section"
        
        try:
            article_page = requests.get(article_url)
            article_page = article_page.json()
            if(article_page["publishedDate"][0:10] == current_date):
                if not any(article_url in match_url for match_url in match_articles):
                    print("match: " + article_url)
                    match_articles.append(article_url)
                    article_body = article_page["bodyXML"]
                    article_text1 = re.sub(r"<.*?>", "", article_body)
                    article_number = article_number + 1
                    article_text2 = "The Financial Times - {section} - article number {number}. ".format(section = article_section, number = article_number) + article_text1 + "{{split}}"
                    text.append(article_text2.encode("utf8"))
        except:
            continue
        	
open_file = open("ft_text.txt", "wb")
open_file.writelines(text)
print("ft_text.txt created")
open_file.close()

