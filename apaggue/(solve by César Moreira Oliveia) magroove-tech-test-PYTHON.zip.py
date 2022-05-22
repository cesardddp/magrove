# Magroove Tech Test:

# This is a very simple test to assess your hability to learn by yourself.

# Goal: 

# Learn to use the Python libraries requests and BeautifulSoup. Your script can be writen using python 2 or 3.

# Steps:

# - Create a Python script that gets the HTML source of this page: https://qz.com/africa/latest/ using the requests library.
# - Your program must print the title and the link of all articles on the page
# - You can follow this format : 
# 	Title: {article_title}
# 	Link: {article_link}\n

# Pro-tip:

# Article titles on that page are wrapped in 'h3' tags. The corresponding links are 'a' tags wrapping those 'h3' tags.

import requests
from bs4 import BeautifulSoup


url =  "https://qz.com/africa/latest/"

response = requests.get(url)

html_text = response.text

html_parsed = BeautifulSoup(html_text,"html.parser")

articles = html_parsed.find_all('h3')
if not articles:
    # the "Pro-tip" is outdated, the articles aren't wraped in h3, but the article 
    # links are <a> tags have a attr class with the class "eBKpx"
    
    print("<h3> elements not found!!!\n"+
        'The "Pro-tip" is outdated, the articles aren\'t wraped in h3, but the article\n'+
    'links are <a> tags have a attr class with the class "eBKpx", we\'ll use this to get the articles!')
    
    # get all articles <a> links
    articles = html_parsed.find_all(class_='eBKpx')



for article in articles:

    # article is a <a> link, lets get href
    article_link = url[0:14] + article.get('href')

    # get the div wrapper inside each link
    div_in_link = next(article.children)

    # get text section from article, assuming child[0] is the img section
    text_section = [child for child in div_in_link.children][1]

    # are 3 divs in text: theme article, title and date&time
    # lets get the title
    title_element = [child for child in text_section.children][1]
    article_title = title_element.text

    result = f"""
Title: {article_title}
Link: {article_link}"""

    print(result)

