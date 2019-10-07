from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class TestSlider():

    def slider(self):
        baseUrl = 'https://www.asos.com/ru/men/rasprodazha/tufli-i-sportivnaya-obuv/cat/?cid=1935&cr=4&ctaref=shop%7Cfootwear%7Cmw_hp_sale'
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(15)

        buttonClick = driver.find_element(By.XPATH, '//div[text()="Цена"]').click()
        element = driver.find_element(By.XPATH, '//div[@class="_32dlQVv"]//div [1][@class="_1KjVORy"]')
        time.sleep(5)
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 40, 0).perform()
            print('sliding element successful')
        except:
            print('sliding element unsuccessful')

        time.sleep(5)

        driver.quit()


ff = TestSlider()
ff.slider()
