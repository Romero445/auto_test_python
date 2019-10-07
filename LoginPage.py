from selenium import webdriver
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginGameMag(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        baseUrl = "https://gamemag.ru"
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(20)

    def test_login(self):
        self.logoButton = self.driver.find_element_by_xpath(
            "//button[@class = 'gm-btn gm-btn--login'] //span[@class='gm-btn__login-img gm-btn__login-img--passive gm-btn__logout__img']")
        self.logoButton.click()

        self.clearPassword = self.driver.find_element_by_id("login-form-login")
        self.clearPassword.clear()

        self.sendPassword = self.driver.find_element_by_id("login-form-login")
        self.sendPassword.send_keys("Password")

        self.sendLogin = self.driver.find_element_by_name("login-form[password]")
        self.sendLogin.send_keys("login")

        self.loginButton = self.driver.find_element_by_xpath(
            "//div[@class='login-active login-active--show']//button[text()='Войти']")
        self.loginButton.click()

        time.sleep(5)

        endTest = self.driver.find_element(By.XPATH, "//div[text()='Неправильный логин или пароль']")

        self.assertTrue(self.is_element_present(By.XPATH, "//div[text()='Неправильный логин или пароль']"))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
