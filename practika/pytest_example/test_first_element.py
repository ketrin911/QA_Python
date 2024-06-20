import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_exection1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
        input1 = driver.find_elements(By.CSS_SELECTOR,'[required]')
        for i in input1:
            i.send_keys('test@mail.ru')

        btn = driver.find_element(By.CSS_SELECTOR, 'button').click()
        text = driver.find_element(By.CSS_SELECTOR, '#success-message').text
        assert text == "Вы успешно зарегистрированы!"    
        
    finally:
        driver.quit()








# def test_sum():
#     assert 5+3==8
# def test_upper():
#     assert 'hello'.upper() == "HELLO"