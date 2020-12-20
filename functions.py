from selenium import webdriver
# import requests
# import json
import pickle

config = {
    'insta_url': 'https://www.instagram.com/ihub_khm/tagged/'
}


def get_insta_posts():
    cookies = {
        'domain': '.instagram.com',
        "ig_did": "58971998-1837-4A06-B2DA-2DBEAB6B2250",
        "mid": "XrujiAALAAHHAKk-gpcHvE3x4TMV",
        "ds_user_id": "5961078248",
        "csrftoken": "mmc2td6kSwrZZzNMsu0F8fLCntQCxqLL",
        "sessionid": "5961078248%3AOLUa6tDvgbHjJz%3A15",
    }
    driver = webdriver.PhantomJS()  # or add to your PATH
    driver.get('https://www.instagram.com/ihub_khm/tagged/')

    # print(driver.get_cookies())

    # for cookie in cookies:
    driver.add_cookie(cookies)

    driver.refresh()
    driver.save_screenshot('screen.png')


if __name__ == '__main__':
    get_insta_posts()
