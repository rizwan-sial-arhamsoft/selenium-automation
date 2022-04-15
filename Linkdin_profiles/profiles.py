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

Driver.get('https:www.google.com')
time.sleep(3)

search_query = Driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "Lahore"')
time.sleep(0.5)

search_query.send_keys(Keys.RETURN)
time.sleep(3)
time.sleep(10)

linkedin_urls = Driver.find_elements(by=By.XPATH, value="//div[@class='yuRUbf']/a")

for i in range(len(linkedin_urls)):
    urls.append(linkedin_urls[i].get_attribute('href'))
time.sleep(0.5)

Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

try:
    NEXT_PAGE = Driver.find_element(by=By.XPATH, value="//a[@id='pnnext']/span[2]")
except:
    time.sleep(20)
    NEXT_PAGE = Driver.find_element(by=By.XPATH, value="//a[@id='pnnext']/span[2]")
COUNT = 0

while NEXT_PAGE:
    if COUNT == 90:
        break
    try:
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
    except:
        time.sleep(15)
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
df.to_excel("Lahore_Python_Developers.xlsx")
name_s = []
title_s = []
about_s = []
experience_s = []
education_s = []

for url in urls:
    Driver.get(url)
    time.sleep(5)
    name = Driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div['
                                                  '2]/div[2]/div[1]/div[1]/h1')
    name_s.append(name.text)
    title = Driver.find_element(by=By.XPATH,
                                value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div['
                                      '2]/div[2]/div[1]/div[2]')
    title_s.append(title.text)
    try:
        about = Driver.find_element(by=By.XPATH,
                                    value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[2]/div['
                                          '3]/div/div/div/span[1]')
        about_s.append(about.text)
    except:
        about_s.append(None)
    Driver.execute_script("window.scrollTo(0,1700)")
    education = Driver.find_elements(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section['
                                                        '5]/div[3]/ul/li/div/div[2]/div[1]/a/div/span/span[1]')
    detail = Driver.find_elements(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section['
                                                     '6]/div[3]/ul/li[1]/div/div[2]/div/a/span[1]/span[1]')
    ex_title = []
    ex_organization = []
    edu_institute = []
    edu_program = []
    for i in range(len(detail)):
        edu_institute.append(education[i].text)
        edu_program.append(detail[i].text)

    education = {
        "Institute": edu_institute,
        "Program": edu_program
    }
    education_s.append(education)
    experience_title = Driver.find_elements(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div['
                                                               '2]/div/div/main/section[5]/div[3]/ul/li/div/div['
                                                               '2]/div[1]/div[1]/div/span/span[1]')
    org = Driver.find_elements(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section['
                                                  '5]/div[3]/ul/li/div/div[2]/div[1]/div[1]/span[1]/span[1]')

    for i in range(len(experience_title)):
        ex_title.append(experience_title[i].text)
        ex_organization.append(org[i].text)

    experience = {
        "Title": ex_title,
        "Organization": ex_organization
    }
    experience_s.append(experience)

Data = {
    "Name": name_s,
    "Title": title_s,
    "About": about_s,
    "Education": education_s,
    "Experience": experience_s
}
df = pd.DataFrame(data=Data)
df.to_excel("Scraped_CV.xlsx")

Driver.close()
Driver.quit()
