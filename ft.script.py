__author__ = 'Steve'

## import libraries
from lxml import html, etree
import requests
import re

## ft api key
## url is http://api.ft.com/content/insert.article.id.here?apiKey=
## article id is everything from last forward slash to ".html" in url
## url to webpage with hyperlinks to today's articles is "http://www.ft.com/intl/international-edition"

## enter api key as string
api_key =

## fetch and parse html
url = "http://www.ft.com/intl/international-edition"
page = requests.get("http://www.ft.com/intl/international-edition")
tree = etree.HTML(page.text)

## gather links from each section of the paper
front_links = tree.xpath("""//div[@class = 'feedBox']/h4/a[contains(text(), 'Front Page & Second Front')]/
        ../../ul/li/a/@href""")
world_links = tree.xpath("""//div[@class = 'feedBox']/h4/a[contains(text(), 'World')]/
        ../../ul/li/a/@href""")
analysis_links = tree.xpath("""//div[@class = 'feedBox']/h4/a[contains(text(), 'Analysis')]/
        ../../ul/li/a/@href""")
notebook_links = tree.xpath("""//div[@class = 'feedBox']/h4/a[contains(text(), 'Notebook')]/
        ../../ul/li/a/@href""")
editorial_links = tree.xpath("""//div[@class = 'feedBox']/h4/a[contains(text(), 'Opinion & Editorial')]/
        ../../ul/li/a/@href""")

## compile all the section links into one list
section_links = front_links + world_links + analysis_links + notebook_links + editorial_links

## fetch articles from each section of the paper and append to text file
text = []

for i in section_links:
        article_id = i[(i.rfind("/")+1) : i.rfind(".html")]
        article_url = "http://api.ft.com/content/" + article_id + "?apiKey=" + api_key
        article_page = requests.get(article_url)
        article_page = article_page.json()
        article_body = article_page["bodyXML"]
        article_text1 = re.sub(r"<.*?>", "", article_body)
        ##article_text2 = re.sub(r"\n", "", article_text1)
        ##article_text3 = re.sub(r"\u2009", "", article_text3)
        article_text3 = article_text1 + "{{split}}"
        text.append(article_text3.encode("utf8"))

open_file = open("ft_text.txt", "wb")
open_file.writelines(text)
