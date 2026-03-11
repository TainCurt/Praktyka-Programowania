import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

class Input_Test(TestCase):
    BLOG_URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2F"
    INPUT_NAME = "username"
    CLEAR_NAME = "clear"

    def test_input_value(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found")

        login_box.send_keys("your_username")
        inputValue = login_box.get_attribute("value")
        self.assertEqual("your_username", inputValue)

    def test_click_value(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found")

        try:
            clear_button = self.driver.find_element(by=By.NAME, value=self.CLEAR_NAME)
        except Exception:
            self.fail("Clear input not found")
        
        clear_button.click()
        inputValue = login_box.get_attribute("value")
        self.assertEqual("", inputValue)

if __name__ == '__main__':
    unittest.main()