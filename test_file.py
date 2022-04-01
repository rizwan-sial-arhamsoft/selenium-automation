import time
import pandas as pd
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

Driver = uc.Chrome()
Driver.maximize_window()
Driver.get('https://whatmobile.web.pk/honor-x9-4g.html')
Specs = Driver.find_element(by=By.XPATH, value="//div[@id='service-two']/section")
