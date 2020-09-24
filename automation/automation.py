#Able to inspect through page and find out what I want to control

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('GET RICH!!!')
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'GET RICH!!!' in output_message.text
chrome_browser.close()