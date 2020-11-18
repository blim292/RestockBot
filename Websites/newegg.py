# this file will check the 3070 page for add to cart button and will return True if found
from bs4 import BeautifulSoup
import requests

class Newegg(object):
    def parsePage(self):
        url = "https://www.newegg.com/p/pl?d=rtx+3070&N=100007709%204841%20600007801&isdeptsrh=1"
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        print(soup.prettify())
    def test(self):
        print("This is a test")
