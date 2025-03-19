from selenium.webdriver.common.by import By

from pages.ShopPage import ShopPage

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.userNameElem = 'username'
        self.userPasswordElem = 'password'
        self.singupBtn = 'signInBtn'

        self.userNameData = 'rahulshettyacademy'
        self.userPassword = 'learning'

    def login(self):
        self.driver.find_element(By.ID,self.userNameElem).send_keys(self.userNameData)
        self.driver.find_element(By.ID,self.userPasswordElem).send_keys(self.userPassword)
        self.driver.find_element(By.ID,self.singupBtn).click()
        shopPage = ShopPage(self.driver)
        return shopPage