import Crawler
links = Crawler.crawler("http://www.doggycraft.dk", 5)  # url and maxPages to crawl
print(links)
raw_input()