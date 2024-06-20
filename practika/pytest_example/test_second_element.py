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

@pytest.mark.login
def test_valid_login(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'openModalButton')))
    login.click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'loginModal')))
    username = driver.find_element(By.ID,'username')
    username.send_keys('testuser')
    password = driver.find_element(By.ID,'password')
    password.send_keys('password123')
    time.sleep(5)
 
    btn  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ['type="submit'])))
    btn.click()
    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ['type="submit'])))
        print('успех')
    except:
        print('косяк')








