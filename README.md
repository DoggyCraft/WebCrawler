# WebCrawler

How to use:

first you will need BeautifulSoup
you can install it using 'pip install BeautifulSoup4'

import Crawler
links = Crawler.crawler("http://www.yourwebsite.dk", MaxPages)
print(links)

as for now it will only crawl websites and look for links