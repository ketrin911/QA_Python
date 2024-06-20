import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.xfail
def test_open_main_page(driver):
    driver.get("http://selenium1py.pythonanywhere.com/ru/")
    driver.find_element(By.CSS_SELECTOR,'href="/ru/offers/"').click()
   
    books = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
    for book in books[:4]:
        book.click()
   
    basket = driver.find_element(By.LINK_TEXT, "Посмотреть корзину").click()

    


            


    time.sleep(5)




