import Crawler
spider = Crawler.Crawler()
links = spider.crawler("http://www.doggycraft.dk", 5)  # url and maxPages to crawl
print(links)
raw_input()