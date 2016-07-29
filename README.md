# WebCrawler

How to use:

first you will need BeautifulSoup
you can install it using 'pip install BeautifulSoup4'

```python
import Crawler
spider = Crawler.Crawler("http://www.yourwebsite.dk", MaxPages)
print(spider.getLinks)
```

as for now it will only crawl websites and look for links
