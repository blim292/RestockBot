from bs4 import BeautifulSoup
import requests

class BestBuy(object):
    # parse the text so that it can be processed using beautifulsoup
    def parsePage(self):
        # url = "https://www.bestbuy.com/site/searchpage.jsp?st=rtx+3070&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys?"
        url = "https://www.bestbuy.com/site/playstation-5/ps5-games/pcmcat1587395108347.c?id=pcmcat1587395108347"
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        urls = []
        print(soup.prettify())
        # for link in soup.find_all("li", class_='sku-item'):
        #     print(link.prettify())
            # if "Add to cart " in str(link):
            #     title = link.find('img')['title']
            #     url = link.a['href']
            #     # starting index to extra productID site specific
            #     startIndex = str(url).index('/p/') + 3
            #     productID = str(url)[startIndex:]
            #     cart = "https://secure.newegg.com/Shopping/AddtoCart.aspx?Submit=ADD&ItemList=" + productID
            #     # save as a tuple pair for unpacking when results found.
            #     urls.append((title, url, cart))
            #     # can add a break here if we only want return the first found item.
            #     # break

        # return urls
