import time
import pandas as pd
import undetected_chromedriver as uc
from openpyxl.workbook import Workbook
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, expected_conditions

Driver = uc.Chrome()
Driver.maximize_window()
Driver.get('https://whatmobile.web.pk/')
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
mobile_images = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/div/a")
mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/b/a")
mobile_prices = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/div/div")
mobile_companies = Driver.find_elements(by=By.XPATH, value="//ul[@class='brb']/a")
hrefs = []
images_data = []
spec_data = []
names_data = []
prices_data = []
for m in range(len(mobile_names)):
    images_data.append(mobile_images[m].get_attribute("href"))
    names_data.append(mobile_names[m].text)
    prices_data.append(mobile_prices[m].text)
    hrefs.append(mobile_companies[m].get_attribute("href"))


for i in range(len(hrefs)):
    Driver.get(hrefs[i])
    mobile_images = Driver.find_elements(by=By.XPATH, value="//a[@class='link-text']")
    mobile_names = Driver.find_elements(by=By.XPATH, value="//h6[@class='mt-3']/a")
    mobile_prices = Driver.find_elements(by=By.XPATH, value="//div[@class='price small']")
    for j in range(len(mobile_names)):
        images_data.append(mobile_images[j].get_attribute("href"))
        names_data.append(mobile_names[j].text)
        prices_data.append(mobile_prices[j].text)

for i in range(len(images_data)):
    Driver.get(images_data[i])
    Specs = Driver.find_element(by=By.XPATH, value="//div[@id='service-two']/section")
    spec_data.append(Specs.text)
#
# for i in range(len(mobile_companies)):
#     time.sleep(3)
#     hrefs.append(mobile_companies[i].get_attribute("href"))
    # Driver.get(href)
    # your_element = WebDriverWait(Driver, 5, ignored_exceptions=ignored_exceptions) \
    #     .until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[@class='link-text']")))
    # print(your_element)
    # time.sleep(3)

data = {"Name": names_data, "Price": prices_data, "Images": images_data, "Specs": spec_data}

df = pd.DataFrame(data=data)
df.to_excel("Mobile_data.xlsx")
print(Driver.title)
print(hrefs)
time.sleep(10)
