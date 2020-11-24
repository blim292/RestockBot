# this file will check the 3070 page for add to cart button and will return True if found
from bs4 import BeautifulSoup
import requests
# use selenium here, if result found, open carted item in browser...
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
                strURL = str(url)
                # starting index to extra productID site specific
                startIndex = strURL.index('/p/') + 3
                productID = strURL[startIndex:]
                endIndex = productID.index('?')
                productID = productID[:endIndex]
                cart = "https://secure.newegg.com/Shopping/AddtoCart.aspx?Submit=ADD&ItemList=" + productID
                # save as a tuple pair for unpacking when results found.
                urls.append((title, url, cart))
                # can add a break here if we only want return the first found item.
                # break

        return urls
