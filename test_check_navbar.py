import unittest
from selenium.webdriver.support.wait import WebDriverWait
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NavbarTest(BaseTest):
    def test_navbar_clickable(self):
        driver = self.driver
        driver.get("https://kariyer.baykartech.com/tr/")

        navbar_elements = driver.find_elements(By.CSS_SELECTOR, "nav-item")
        for element in navbar_elements:
            element_text = element.text
            print(f"Tıklanıyor: {element_text}")
            element.click()
            WebDriverWait(driver, 10).until(EC.title_contains(element_text))
            driver.back()
            navbar_elements = driver.find_elements(By.CSS_SELECTOR, "nav-item")

if __name__ == "__main__":
    unittest.main()
