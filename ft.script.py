__author__ = 'Steve'

## import libraries
from lxml import html, etree
import requests
import re

## enter api key as string
api_key = "hNIqHozr1JA4f2mU0uDZA2GkZfVzhpQC"

## fetch and parse html
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

## create variables for total number of articles and range of each section's article count
total_articles = len(section_links) + 1

# range_front = range(len(front_links))
# range_world = range(range_front[-1] + 1, range_front[-1] + 1 + len(world_links))
# range_analysis = range(range_world[-1] + 1, range_world[-1] + 1 + len(analysis_links))
# range_notebook = range(range_analysis[-1] + 1, range_analysis[-1] + 1 + len(notebook_links))
# range_editorial = range(range_notebook[-1] + 1, range_notebook[-1] + 1 + len(editorial_links))

range_front = range(len(front_links))
range_world = range(range_front[-1] + 1, range_front[-1] + 1 + len(world_links))
range_analysis = range(range_front[-1] + 1 + len(world_links), range_front[-1] + 1 + len(world_links) + len(analysis_links))
range_notebook = range(range_front[-1] + 1 + len(world_links) + len(analysis_links), range_front[-1] + 1 + len(world_links) + len(analysis_links) + len(notebook_links))
range_editorial = range(range_front[-1] + 1 + len(world_links) + len(analysis_links) + len(notebook_links),     range_front[-1] + 1 + len(world_links) + len(analysis_links) + len(notebook_links) + len(editorial_links))

## fetch articles from each section of the paper and append to text file
text = []

for i in range(len(section_links)):
        article = section_links[i]
        article_number = i + 1
        
        article_section = ""
        if i in range_front:
                article_section = "Front section"
        elif i in range_world:
                article_section = "World Section"
        elif i in range_analysis:
                article_section = "Analysis Section"
        elif i in range_notebook:
                article_section = "Notebook Section"
        elif i in range_editorial:
                article_section = "Editorial Section"
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


