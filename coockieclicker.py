from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users/Leon/Desktop/pycharm_files/chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
choose_language = driver.find_element(By.ID, 'langSelect-EN')
choose_language.click()

time.sleep(3)
cockie = driver.find_element(By.ID, "bigCookie")

cursor_botton0 = driver.find_element(By.ID, "product0")
cursor_botton1 = driver.find_element(By.ID, "product1")


for i in range(1,2000):
    cockie.click()
    price0 = ((driver.find_element(By.ID, "productPrice0")).text)
    price0 = int(price0)
    price1 = int((driver.find_element(By.ID, "productPrice1")).text)

    amount_of_cookies = driver.find_element(By.CSS_SELECTOR, "#cookies")
    cookies_display = (amount_of_cookies.text).split()
    number_of_cookies = int(cookies_display[0])

    number_of_cookies_per_second = cookies_display[4]
    if number_of_cookies > price0:
        cursor_botton0.click()
    elif number_of_cookies > price1:
        cursor_botton1.click()

time.sleep(3)
print(f"number of cookies per second{number_of_cookies_per_second}")