from selenium import webdriver
import time
import unittest
import loging as cl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


class LoginGameMag(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        self.driver = webdriver.Firefox()
        baseUrl = "https://gamemag.ru"
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(20)

    def test_login(self):
        self.logoButton = self.driver.find_element(By.XPATH,"//button[@class = 'gm-btn gm-btn--login'] //span[@class='gm-btn__login-img gm-btn__login-img--passive gm-btn__logout__img']")
        self.logoButton.click()
        self.log.info("Вы нажали кнопку")
        
        self.clearLoggin = self.driver.find_element(By.ID, "login-form-login").clear()
        self.log.info("Поле чистое")

        self.sendLoggin = self.driver.find_element(By.ID, "login-form-login").send_keys("send_login")
        self.log.info("Вы ввели login")

        self.sendPassword = self.driver.find_element(By.NAME, "login-form[password]").send_keys("Password")
        self.log.info("Вы ввели password")

        self.loginButton = self.driver.find_element(By.XPATH,
                                                    "//div[@class='login-active login-active--show']//button[text()='Войти']").click()
        self.log.info("Упс ошибка")

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
