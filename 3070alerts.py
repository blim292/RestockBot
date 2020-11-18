# main program will call other files for alerts


import Websites.newegg as ne


newegg = ne.Newegg()
newegg.parsePage()
# while True:
# every 5 seconds, check availability
