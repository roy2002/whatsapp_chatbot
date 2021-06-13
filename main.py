from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')

time.sleep(5)

chat = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[11]/div/div/div[2]')
chat.click()

time.sleep(5)

text = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]')

for i in range(0, 10):

    text.send_keys('Hi')
    text.send_keys(Keys.ENTER)


