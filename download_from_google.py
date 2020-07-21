from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
from time import sleep

search = "dog"
num_imgs = 100

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwikzYbF1t3qAhVRX30KHRs7CWMQ_AUoAXoECCAQAw&biw=1366&bih=657".format(search)
driver.get(url)

for i in range(1, num_imgs+1):
    try:
        xpath = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{}]/a[1]/div[1]/img".format(i)
        element = driver.find_element_by_xpath(xpath)
        element.screenshot("downloaded_from_google/"+search+str(i)+".png")
        sleep(0.1)
        print(i)
    except:
        continue

