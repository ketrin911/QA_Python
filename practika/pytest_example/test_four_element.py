import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# @pytest.fixture
# def driver():
#     driver = webdriver.Firefox()
#     time.sleep(3)
#     yield driver
#     driver.quit()

# def test_forma(driver):
#     driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
#     driver.find_element(By.CSS_SELECTOR, '#login').send_keys('admin123')
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys('321drowssap')
#     driver.find_element(By.CSS_SELECTOR, '#database').send_keys('dovod_db')
#     driver.find_element(By.CSS_SELECTOR, '#host').send_keys('tsohlacol')
#     driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     alert = driver.switch_to.alert
#     alert.accept


#     driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
#     driver.find_element(By.CSS_SELECTOR, '#login').send_keys('admin123')
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys('321drowssap')
#     driver.find_element(By.CSS_SELECTOR, '#database').send_keys('dovod_db')
#     driver.find_element(By.CSS_SELECTOR, '#host').send_keys('tsohlacol')
#     driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    
driver = webdriver.Firefox()
driver.get('https://erikdark.github.io/dovod_repo_QA_form/')


#найти элементы
l_i = driver.find_element(By.ID,'login')
p_i = driver.find_element(By.ID,'password')
d_i = driver.find_element(By.ID,'database')
h_i = driver.find_element(By.ID,'host')
s_b = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')


#заполнил форму
l_i.send_keys('admin123')
p_i.send_keys('password123')
d_i.send_keys('bd_dovod')
h_i.send_keys('localhost')




#отправляю форму
s_b.click()
time.sleep(2)

alert = driver.switch_to.alert
alert.accept()




#очищаю поля


l_i.clear()
p_i.clear()
d_i.clear()
h_i.clear()






h_i.send_keys('tsohlacol')
d_i.send_keys('dovod_db')
p_i.send_keys('321drowssap')
l_i.send_keys('321nimda')




s_b.click()
time.sleep(2)    
    

