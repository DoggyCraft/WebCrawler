import Crawler
spider = Crawler.Crawler("http://www.doggycraft.dk", 5)
print(spider.getLinks)
raw_input()