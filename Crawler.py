#! python2
import requests
from bs4 import BeautifulSoup

links = []
visited = []
allLinks = []


def crawler(url, maxPages):
    links.append(url)
    url = links.pop()
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
                if href not in allLinks:
                    links.append(href)
                    allLinks.append(href)
        except:
            if url == None:
                print(str(url)+" findes ikke")

        if len(links) == 0:
            print("har ikke flere links")
            break
        url = links.pop()
        page += 1

    print("links found: " + str(allLinks))
    print("visited: " + str(visited))

crawler("http://www.doggycraft.dk", 5)  # url and maxPages to crawl
raw_input()
