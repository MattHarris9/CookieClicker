from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

s = Service("C:/WebDriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]



actions = ActionChains(driver)


for i in range(5000):
    actions.click(cookie)
    print(i)




actions.perform()
sleep(2)
driver.quit()

