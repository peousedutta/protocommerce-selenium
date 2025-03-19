import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.LoginPage import LoginPage

# URL = "https://rahulshettyacademy.com/angularpractice"
URL = "https://rahulshettyacademy.com/loginpagePractise/"

def test_e2e(browserInstance):
    driver = browserInstance
    driver.get(URL)

    productName = 'iphone X'    #Enter add to cart product name

    loginPage = LoginPage(driver) #Create page instances
    
    shopPage = loginPage.login() # perform login operation
    shopPage.addProduct(productName) # add specific product name to cart
    shopPage.goToCart() # proceed with the checkout operation
    checkoutPage = shopPage.proceedWithCheckout()
    checkoutPage.enterDeliveryLocation('Ind')
    checkoutPage.selectFromSuggestedLocations()
    checkoutPage.confimAndPurchase
    
    time.sleep(2)