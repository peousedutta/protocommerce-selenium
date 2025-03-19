from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.inputCountryElm = (By.ID, "country")
        self.dropDownElm = (By.LINK_TEXT, "India")
        self.termsAndConditionsCheckbox = (By.XPATH, "//input[@id='checkbox2']")
        self.purchaseBtn = (By.XPATH, "//input[@value='Purchase']")
        self.successMsgSection = (By.CLASS_NAME, "alert alert-success alert-dismissible")

    def enterDeliveryLocation(self, country):
        self.driver.find_element(*self.inputCountryElm).send_keys(country)

    def selectFromSuggestedLocations(self):
        waitTime = 10 # seconds
        WebDriverWait(self.driver, waitTime).until(
            EC.presence_of_element_located((By.LINK_TEXT, "India"))
        )
        self.driver.find_element(*self.dropDownElm).click()
    
    def confimAndPurchase(self):
        self.driver.find_element(*self.termsAndConditionsCheckbox).click()
        self.driver.find_element(*self.purchaseBtn).click()
        successMsg = self.driver.find_element(*self.successMsgSection).text
        assert "Success! Thank you!" in successMsg
       