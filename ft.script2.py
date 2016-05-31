__author__ = 'Steve'

## import libraries
from lxml import html, etree
import requests
import re
import os

# set working directory
#%cd c://users//stephen//desktop//python
#%ls
#%pwd
os.chdir("c:/users/stephen/desktop/python/python-ft-scraper")

## enter api key as string
api_key = "hNIqHozr1JA4f2mU0uDZA2GkZfVzhpQC"

## world section
## fetch and parse html
world_page = requests.get("http://www.ft.com/intl/world")
world_tree = etree.HTML(world_page.text)

## world section
# us section
us_lead_links = world_tree.xpath("""//a[text() = 'US & CANADA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
us_lead_titles = world_tree.xpath("""//a[text() = 'US & CANADA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

us_links = world_tree.xpath("""//a[text() = 'US & CANADA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
us_titles = world_tree.xpath("""//a[text() = 'US & CANADA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

us_links = us_lead_links + us_links 
us_titles = us_lead_titles + us_titles 

# europe section
europe_lead_links = world_tree.xpath("""//a[text() = 'EUROPE']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
europe_lead_titles = world_tree.xpath("""//a[text() = 'EUROPE']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

europe_links = world_tree.xpath("""//a[text() = 'EUROPE']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
europe_titles = world_tree.xpath("""//a[text() = 'EUROPE']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

europe_links = europe_lead_links + europe_links 
europe_titles = europe_lead_titles + europe_titles 

# africa section
africa_lead_links = world_tree.xpath("""//a[text() = 'AFRICA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
africa_lead_titles = world_tree.xpath("""//a[text() = 'AFRICA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

africa_links = world_tree.xpath("""//a[text() = 'AFRICA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
africa_titles = world_tree.xpath("""//a[text() = 'AFRICA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

africa_links = africa_lead_links + africa_links 
africa_titles = africa_lead_titles + africa_titles 

# middle east and north africa section
mideast_lead_links = world_tree.xpath("""//a[text() = 'MIDDLE EAST & NORTH europe']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
mideast_lead_titles = world_tree.xpath("""//a[text() = 'MIDDLE EAST & NORTH europe']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

mideast_links = world_tree.xpath("""//a[text() = 'MIDDLE EAST & NORTH europe']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
mideast_titles = world_tree.xpath("""//a[text() = 'MIDDLE EAST & NORTH AFRICA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

mideast_links = mideast_lead_links + mideast_links 
mideast_titles = mideast_lead_titles + mideast_titles 

# asia section
asia_lead_links = world_tree.xpath("""//a[text() = 'ASIA-PACIFIC']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
asia_lead_titles = world_tree.xpath("""//a[text() = 'ASIA-PACIFIC']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

asia_links = world_tree.xpath("""//a[text() = 'ASIA-PACIFIC']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
asia_titles = world_tree.xpath("""//a[text() = 'ASIA-PACIFIC']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

asia_links = asia_lead_links + asia_links 
asia_titles = asia_lead_titles + asia_titles 

# latin america section
latin_lead_links = world_tree.xpath("""//a[text() = 'LATIN AMERICA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
latin_lead_titles = world_tree.xpath("""//a[text() = 'LATIN AMERICA']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

latin_links = world_tree.xpath("""//a[text() = 'LATIN AMERICA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
latin_titles = world_tree.xpath("""//a[text() = 'LATIN AMERICA']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

latin_links = latin_lead_links + latin_links 
latin_titles = latin_lead_titles + latin_titles 

# global economy section
global_lead_links = world_tree.xpath("""//a[text() = 'GLOBAL ECONOMY']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
global_lead_titles = world_tree.xpath("""//a[text() = 'GLOBAL ECONOMY']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

global_links = world_tree.xpath("""//a[text() = 'GLOBAL ECONOMY']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a/@href""")
global_titles = world_tree.xpath("""//a[text() = 'GLOBAL ECONOMY']/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../..//li[@class = 'ft-list-item']/a[text()]""")

global_links = global_lead_links + global_links 
global_titles = global_lead_titles + global_titles 


# comment section
## fetch and parse html
comment_page = requests.get("http://www.ft.com/intl/comment")
comment_tree = etree.HTML(comment_page.text)

comment_lead_links = comment_tree.xpath("""//a[text() = 'COLUMNISTS']/../
    ../span[2]/a[not(contains(text(), 'Instant'))]/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
comment_lead_titles = comment_tree.xpath("""//a[text() = 'COLUMNISTS']/../
    ../span[2]/a[not(contains(text(), 'Instant'))]/../../
    span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")

opinion_lead_links = comment_tree.xpath("""//a[text() = 'OPINION']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a/@href""")
opinion_lead_titles = comment_tree.xpath("""//a[text() = 'OPINION']/../
    ../span[1][contains(text(), 'pm') or contains(text(), 'am')]/../../h3/a[text()]""")
    
comment_links = comment_lead_links + opinion_lead_links
comment_titles = comment_lead_titles + opinion_lead_titles


## compile all the section links into one list
section_links = us_links + europe_links + africa_links + mideast_links + asia_links + latin_links + global_links + comment_links

## create variables for total number of articles and range of each section's article count
total_articles = len(section_links) + 1

range_us = range(len(us_links))
range_europe = range(range_us[-1] + 1, range_us[-1] + 1 + len(europe_links))
range_africa = range(range_us[-1] + 1 + len(europe_links), 
        range_us[-1] + 1 + len(europe_links) + len(africa_links))
range_mideast = range(range_us[-1] + 1 + len(europe_links) + len(africa_links), 
        range_us[-1] + 1 + len(europe_links) + len(africa_links) + len(mideast_links))
range_asia = range(range_us[-1] + 1 + len(europe_links) + len(africa_links) + 
    len(mideast_links), range_us[-1] + 1 + len(europe_links) + len(africa_links) + 
    len(mideast_links) + len(asia_links))
range_latin = range(range_us[-1] + 1 + len(europe_links) + len(africa_links) + 
    len(mideast_links) + len(asia_links), range_us[-1] + 1 + len(europe_links) + 
    len(africa_links) + len(mideast_links) + len(asia_links) + len(latin_links))
range_global = range(range_us[-1] + 1 + len(europe_links) + len(africa_links) + 
    len(mideast_links) + len(asia_links) + len(latin_links), range_us[-1] + 1 + 
    len(europe_links) + len(africa_links) + len(mideast_links) + len(asia_links) + 
    len(latin_links) + len(global_links))
range_comment = range(range_us[-1] + 1 + len(europe_links) + len(africa_links) + 
    len(mideast_links) + len(asia_links) + len(latin_links) + len(global_links), 
    range_us[-1] + 1 + len(europe_links) + len(africa_links) + len(mideast_links) + 
    len(asia_links) + len(latin_links) + len(global_links) + len(comment_links)) 

## fetch articles from each section of the paper and append to text file
text = []

for i in range(len(section_links)):
        article = section_links[i]
        article_number = i + 1
        
        article_section = ""
        if i in range_us:
                article_section = "U.S. and Canada section"
        elif i in range_europe:
                article_section = "Europe Section"
        elif i in range_africa:
                article_section = "Africa Section"
        elif i in range_mideast:
                article_section = "Middle East and North Africa Section"
        elif i in range_asia:
                article_section = "Asia Section"
        elif i in range_latin:
                article_section = "Latin America Section"
        elif i in range_global:
                article_section = "Global Economy Section"
        elif i in range_comment:
                article_section = "Comment Section"
        print(article_section)

        print(article)
        article_id = article[(article.rfind("/")+1) : article.rfind(".html")]
        article_url = "http://api.ft.com/content/" + article_id + "?apiKey=" + api_key
        article_page = requests.get(article_url)
        article_page = article_page.json()
        article_body = article_page["bodyXML"]
        article_text1 = re.sub(r"<.*?>", "", article_body)
        article_text2 = "The Financial Times - {section} - article number {number} of {total}. ".format(section = article_section, 
                number = article_number, total = total_articles) + article_text1 + "{{split}}"
        text.append(article_text2.encode("utf8"))

open_file = open("ft_text.txt", "wb")
open_file.writelines(text)
print("ft_text.txt created")
open_file.close()


