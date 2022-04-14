""" This is a script to scrap the profiles
of specific area and specific technology developers
from linked In"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urls = []

Driver = webdriver.Firefox()
Driver.get('https://www.linkedin.com')

username = Driver.find_element(by=By.XPATH, value='//*[@id="session_key"]')
username.send_keys('786rizoo@gmail.com')
time.sleep(0.5)

password = Driver.find_element(by=By.XPATH, value='//*[@id="session_password"]')
password.send_keys('Rk@arhamsoft03')
time.sleep(0.5)

sign_in_button = Driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
time.sleep(0.5)

search_box = Driver.find_element(by=By.XPATH, value="//input[@class='gLFyf gsfi']")
search_box.clear()
search_box.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')
search = Driver.find_element(by=By.XPATH, value="//span[@class='z1asCe MZy1Rb']")
search.click()
time.sleep(0.5)
time.sleep(10)

linkedin_urls = Driver.find_elements(by=By.XPATH, value="//div[@class='yuRUbf']/a")

for i in range(len(linkedin_urls)):
    urls.append(linkedin_urls[i].get_attribute('href'))
time.sleep(0.5)

Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

NEXT_PAGE = Driver.find_element(by=By.XPATH, value="//a[@id='pnnext']/span[2]")
COUNT = 0

while NEXT_PAGE:
    if COUNT == 9:
        break
    NEXT_PAGE.click()
    linkedin_urls = Driver.find_elements(by=By.XPATH, value="//div[@class='yuRUbf']/a")
    COUNT = COUNT + 1
    for i in range(len(linkedin_urls)):
        urls.append(linkedin_urls[i].get_attribute('href'))
    time.sleep(0.5)
    Driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    try:
        NEXT_PAGE = Driver.find_element(by=By.XPATH, value="//*[@id='pnnext']/span[2]")
    except:
        NEXT_PAGE = None
    print(NEXT_PAGE)

print(urls)
data = {
    "Profiles": urls
}
df = pd.DataFrame(data=data)
df.to_excel("London.xlsx")

Driver.close()
Driver.quit()
