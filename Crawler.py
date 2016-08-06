#! python2
import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, url, maxPages):
        self.url = url
        self.maxPages = maxPages
        data = self.Crawl()
        self.getLinks = data["links"]
        self.getTitle = data["titles"]

    def Crawl(self):
        data = {}
        url = self.url
        maxPages = self.maxPages
        queue = []
        visited = []
        titles = []
        links = []
        queue.append(url)
        url = queue.pop()
        page = 0
        while page < maxPages:
            try:
                visited.append(url)
                code = requests.get(url)
                plain_text = code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                for link in soup.findAll("a"):
                    href = link.get("href")
                    if href.split()[0][0] == "/":
                        href = url + href
                    if href.split()[0][0] == "#":
                        href = url + "/" + href
                    if href not in links:
                        queue.append(href)
                        links.append(href)
            except:
                if url == None:
                    print(str(url)+" does not exist!")

            if len(queue) == 0:
                print("I do not have more pages to crawl..")
                break
            url = queue.pop()
            page += 1
            data["links"] = links
            titles.append(soup.title.string)
            data["titles"] = titles
        return data
