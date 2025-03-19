import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


URL = 'https://rahulshettyacademy.com/angularpractice/'

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get(URL)
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

print('---------------------')
print('products --- ', products)

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    print("Name -- ",productName)
    if productName == "iphone X":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

time.sleep(2)