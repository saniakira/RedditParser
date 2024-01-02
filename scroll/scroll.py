from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

driver.get("https://instagram.com/accounts/login")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username1 = 'instagram' # change it!
password1 = 'instagrampassword1' # change it!

username.send_keys(username1)
password.send_keys(password1)

submit_button = driver.find_element_by_css_selector(
    '#react-root > div > article > div > div:nth-child(1) > div > form > span > button')
submit_button.click()

sleep(2)

link = 'https://www.instagram.com/youtube/'
driver.get(link)

driver.implicitly_wait(2)
driver.find_elements_by_class_name("_218yx")[2].click()