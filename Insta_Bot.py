from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#define webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
cookie = {'domain': 'www.instagram.com', 'httpOnly': False, 'name': 'foo', 'path': '/', 'secure': True, 'value': 'bar'}
driver.add_cookie(cookie)
print(driver.get_cookies())

#wait 10s or till cookies loaded and accept
#element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.TAG_NAME, "button")))
#element.click()

#type username account, wait max 10s until searchbar loaded
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")))
element.send_keys("rn.brndl")
#hit enter
element.send_keys(Keys.RETURN)

#type password
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))
element.send_keys("Arne2005")
#hit enter
element.send_keys(Keys.RETURN)

#press the login button, press enter
element.send_keys(Keys.RETURN)

#click false on safe ur login information
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'sqdOP yWX7d')]")))
print(element)

sleep(30)

#quit
driver.quit()
driver.close()