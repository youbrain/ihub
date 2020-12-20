from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
# import json
from bs4 import BeautifulSoup as bs4

import pickle
from time import sleep

config = {
    'insta_url': 'https://www.instagram.com/ihub_khm/tagged/'
}


def get_insta_posts():
    cookies = {
        "ig_did": "58971998-1837-4A06-B2DA-2DBEAB6B2250",
        "mid": "XrujiAALAAHHAKk-gpcHvE3x4TMV",
        "ds_user_id": "5961078248",
        "csrftoken": "mmc2td6kSwrZZzNMsu0F8fLCntQCxqLL",
        "sessionid": "5961078248%3AOLUa6tDvgbHjJz%3A15",
    }
    '''
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/ihub_khm/tagged/')

    for cookie in cookies.items():
        driver.add_cookie(
            {"name": cookie[0], "value": cookie[1], 'domain': '.instagram.com'})

    driver.refresh()

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_bz0w"))
    )

    page = bs4(driver.page_source)

    links = []
    for link in page.findAll('a'):
        link = link.get('href')
        if link.startswith('/p/'):
            links.append(link)
    '''
    links = ['/p/CIlPczyMKqp/',
             '/p/CIlIz8eosb7/',
             '/p/CITVAnvszSY/',
             '/p/CISvfrSotpD/',
             '/p/CILCeSgMFPF/',
             '/p/CIG4mHkFaUg/',
             '/p/CH_DGBjMIeB/',
             '/p/CH46lhOnZ3z/',
             '/p/CHaIxiRs8Rs/',
             '/p/CHaFchpsc0D/',
             '/p/CHZ21YfMRkq/',
             '/p/CHYYOh5M7yv/']

    for link in links:
        r = requests.get('https://www.instagram.com' + link, cookies=cookies)
        desc = r.text.split(
            ':{"edges":[{"node":{"text":"')[1].split(r'"}}]}')[0]


if __name__ == '__main__':
    print(get_insta_posts())
