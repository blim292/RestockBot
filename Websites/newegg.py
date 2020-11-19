# this file will check the 3070 page for add to cart button and will return True if found
from bs4 import BeautifulSoup
import requests

class Newegg(object):

    # parse the text so that it can be processed using beautifulsoup
    def parsePage(self):
        url = "https://www.newegg.com/p/pl?d=rtx+3070&N=100007709%204841%20600007801&isdeptsrh=1"
        # url = "https://www.newegg.com/Computer-Cases/SubCategory/ID-7?Tid=7583"
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        urls = []
        for link in soup.find_all("div", class_='item-container'):
            if "Add to cart " in str(link):
                title = link.find('img')['title']
                url = link.a['href']
                # save as a tuple pair for unpacking when results found.
                urls.append((title, url))
                # can add a break here if we only want return the first found item.
                # break

        return urls
