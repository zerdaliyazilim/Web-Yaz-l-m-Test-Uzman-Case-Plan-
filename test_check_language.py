from base_test import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LanguageSwitchTest(BaseTest):
    def test_language_switch(self):
        driver = self.driver
        driver.get("https://kariyer.baykartech.com/tr/")

        # Sağlanan dilleri topla
        languages = driver.find_elements(By.CSS_SELECTOR, ".nav-item.top-btn")
        supported_languages = [lang.text for lang in languages]

        # Her dil için geçiş yap ve doğrula
        for lang in supported_languages:
            print(f"Dil değiştiriliyor: {lang}")
            driver.find_element(By.LINK_TEXT, lang).click()
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".current-language"), lang)
            )

if __name__ == "__main__":
    unittest.main()
