# You need install selenium and chrome webdriver in advance
# $ pip install selenium
# Download current chrome version of webdriver from http://chromedriver.chromium.org/downloads
# $ unzip chromedriver_mac64.zip
# $ mkdir /usr/local/bin/Cellar/web-driver
# $ mv chromedriver /usr/local/bin/Cellar/web-driver/
# $ ln /usr/local/Cellar/web-driver/chromedriver /usr/local/bin/chromedriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
chrome = webdriver.Chrome()

location = input('Place: ')
favorite_plays = ['hotel', 'museum', 'sightseeing', 'shopping', 'scenery']

for i, os in enumerate(favorite_plays):
    if i > 0:
        chrome.execute_script("window.open('', '_blank')")
        chrome.switch_to.window(chrome.window_handles[i])

    chrome.get('https://www.google.co.jp')

    search_box = chrome.find_element_by_name('q')
    search_words = location, os
    search_box.send_keys(' '.join(search_words))

    search_box.send_keys(Keys.RETURN)
    print(chrome.title)

chrome.switch_to.window(chrome.window_handles[0])

