from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PositionSearchAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def open_page(self, url):
        """Verilen URL'yi aç."""
        self.driver.get(url)

    def get_positions(self):
        """Açık pozisyonları çek ve döndür."""
        positions = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-title"))
        )
        return [position.text for position in positions]

    def filter_positions(self, filter_input):
        """Belirtilen filtreleme girişi ile pozisyonları filtrele."""
        filter_input_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#filterSearch"))
        )
        filter_input_element.clear()
        filter_input_element.send_keys(filter_input)
        time.sleep(2)  # Sayfanın dinamik olarak güncellenmesi için bekle

    def validate_search_result(self, filter_input):
        """Arama sonuçlarını doğrula."""
        filtered_positions = self.get_positions()
        for position in filtered_positions:
            assert filter_input.lower() in position.lower(), f"{position} arama terimini içermiyor."

    def run_test(self, url, filter_input):
        """Testi çalıştır."""
        try:
            self.open_page(url)
            self.filter_positions(filter_input)
            self.validate_search_result(filter_input)
            print("Tüm testler başarılı!")
        except AssertionError as ae:
            print(f"Test başarısız: {ae}")
        except Exception as e:
            print(f"Hata oluştu: {e}")
        finally:
            self.driver.quit()

# Testi çalıştır
if __name__ == "__main__":
    test = PositionSearchAutomation()
    test.run_test("https://kariyer.baykartech.com/tr/open-positions/?type=1&page=1", "TEST")  # Burada
    # istediğin pozisyonu yaz.
