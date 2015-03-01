#script to download the daily financial times in a friendly format
import sys
import requests
import os
import time
import re
import codecs
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from lxml import etree

def strip_html(val):
    return re.sub(r'<[^>]*?>', "", val)

def get_story(link):
    story_id = link[link.rfind('/') + 1:link.rfind('.html')]
    key = "hNIqHozr1JA4f2mU0uDZA2GkZfVzhpQC"
    
    data = requests.get("http://api.ft.com/content/{0}?apiKey={1}".format(story_id, key)).json()
    return ( data['title'], strip_html(data['bodyXML']))


story_list = []
included_sections = ['front page & second front', 'world', 'analysis', 'notebook', 'opinion & editorial']
us_ed_response = requests.get('http://www.ft.com/intl/international-edition')
html = etree.HTML(us_ed_response.text)
sections = html.xpath("//div[@class='feedBoxRow singleColumn']")

for section in sections:

    container_div = section.xpath("div[@class='feedBox']")[0]
    try:
        header = container_div.xpath("h4/a")[0].text
    except IndexError:
        header = container_div.xpath("h4")[0].text

    if header.strip().lower() in included_sections:

        story_list.append("\n\n\n================================\n%s\n=================================\n\n\n" % header)

        links = container_div.xpath('ul/li/a')
        for l in links:
            title, body = get_story(l.attrib['href'])
            story_list.append('\n' + title + '\n')
            story_list.append('\n' + body + '\n')
            story_list.append('\n{{split}}\n')

todays_paper = ''.join(story_list)

msg = MIMEText(todays_paper)
msg['Subject'] = 'Your daily Financial Times digest'
msg['From'] = 'Financial Times Bot at Finsbury'
msg['To'] = 'sdevine188@gmail.com'
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login('financialtimesbot@gmail.com', 'password')
#print todays_paper
s.sendmail('financialtimesbot@gmail.com', 'sdevine188@gmail.com', msg.as_string())

print(todays_paper)

print("Sent mail %s" % datetime.today().strftime("%m/%d %I:%M %p %z"))


                         
