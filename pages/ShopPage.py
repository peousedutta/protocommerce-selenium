from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CheckoutPage import CheckoutPage

class ShopPage():
    def __init__(self, driver):
        self.driver = driver

        self.productElem = (By.XPATH,"//div[@class='card h-100']")
        self.productSpecificTitlePath = (By.XPATH, "div/h4/a")
        self.productSpecificAddBtn = (By.XPATH, "div/button")

        self.gotToCartBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
        self.proceedWithCheckoutBtn =(By.XPATH, "//button[@class='btn btn-success']")

    def addProduct(self, inputProductName):
        products = self.driver.find_elements(*self.productElem)
        for product in products:
            productName = product.find_element(*self.productSpecificTitlePath).text
            if productName == inputProductName:
                product.find_element(*self.productSpecificAddBtn).click()

    def goToCart(self):
        self.driver.find_element(*self.gotToCartBtn).click()
    
    def proceedWithCheckout(self):
        self.driver.find_element(*self.proceedWithCheckoutBtn).click()
        return CheckoutPage(self.driver)