# main program will call other files for alerts


import Websites.newegg as ne
import Websites.bestbuy as bb
import winsound
import time
from datetime import datetime
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():
    newegg = ne.Newegg()
    bestbuy = bb.BestBuy()
    driver = webdriver.Chrome(PATH)

    while True:
        time.sleep(3)
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        newegg_results = newegg.parsePage()
        # bestbuy_results = bestbuy.parsePage()
        if newegg_results:
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 500  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            for title, url, addToCartURL in newegg_results:
                driver.get(addToCartURL)

                # print timestamp
                print("Timestamp: " + dt_string)
                print("Title: " + title)
                print("URL: " + url)
                print("Add to cart: " + addToCartURL)
                print()
                break
        # else:
        #     print(f'{dt_string}: Nothing in stock from Newegg')


main()
