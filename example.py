import Crawler
spider = Crawler.Crawler("http://www.doggycraft.dk", 5)
print(spider.getLinks)
print(spider.getTitle)
raw_input()