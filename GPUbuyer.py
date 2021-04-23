import notify
import selenium
import urllib
import time
from selenium import webdriver
import smtplib
import os
import config

links = config.items
# test link
# link = "https://www.bestbuy.com/site/hyperx-alloy-core-rgb-wired-gaming-membrane-keyboard-with-rgb-lighting-black/6283508.p?skuId=6283508"
interval = 60
browser = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
def openWebpage(link):
    browser.get(link)
    return browser

buyButton = False
while not buyButton:
    for name, link in links.items():
        try:
            browser = openWebpage(link)
            addToCartButton = addButton = browser.find_element_by_class_name("btn-disabled")
            print("Item not in stock at", name)
            time.sleep(interval)
            browser.refresh()
            browser.close()
        except:
            
            addToCartButton = addButton = browser.find_element_by_class_name("btn-primary")

            print("Item in stock")
            addToCartButton.click()
            buyButton = True
            notify.send_email(config.send_to, "In Stock Now!!", "Your item is in stock at" + " " + name)