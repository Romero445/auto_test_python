from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Test():

    def hover(self):
        baseUrl = "https://www.lamoda.ru/men-home/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(15)

        elmentHover = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='Новинки']")
        itemToClick = "//div[@id='menu-dropdowns__wrapper']//a[text()='Одежда']"
        try:
            action = ActionChains(driver)
            action.move_to_element(elmentHover).perform()
            print('Hovered')

            time.sleep(3)

            topLink = driver.find_element(By.XPATH, itemToClick)
            action.move_to_element(topLink).click().perform()
            print('Clicked')
        except:
            print('No')

        driver.quit()


ff = Test()
ff.hover()
