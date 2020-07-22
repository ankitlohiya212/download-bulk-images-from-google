from selenium import webdriver
from time import sleep

search = "your_query"
num_imgs = 100

driver = webdriver.Chrome('path/to/chromedriver_win32/chromedriver')
url = "https://www.google.com/search?q={}&tbm=isch".format(search)
driver.get(url)

for i in range(1, num_imgs+1):
    try:
        xpath = "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{}]/a[1]/div[1]/img".format(i)
        element = driver.find_element_by_xpath(xpath)
		element.screenshot("path/to/directory/"+search+str(i)+".png")
        sleep(0.1)
        print(i)
    except:
        continue

