# main program will call other files for alerts


import Websites.newegg as ne
import winsound
import time
import os
from datetime import datetime

def main():
    newegg = ne.Newegg()

    while True:
        time.sleep(3)
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        newegg_results = newegg.parsePage()
        if newegg_results:
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 500  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            for title, url in newegg_results:
                # print timestamp
                print("Timestamp: " + dt_string)
                print("Title: " + title)
                print("URL: " + url)
                print()
        else:
            print(f'{dt_string}: Nothing in stock from Newegg')


main()
