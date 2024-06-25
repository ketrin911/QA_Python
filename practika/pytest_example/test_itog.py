import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# def test_registr(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     time.sleep(2)
#     name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys('ketrin-d')
#     email = driver.find_element(By.CSS_SELECTOR, "#email").send_keys('ketrin125@mail.ru')
#     password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys('Password123%')
#     confirm_password = driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys('Password123%')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#message').text
#     assert 'Регистрация успешна!' == messege

# def test_name(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys("123")
#     time.sleep(1)
#     email = driver.find_element(By.CSS_SELECTOR, "#email").send_keys('ketrin125@mail.ru')
#     password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys('Password123%')
#     confirm_password = driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys('Password123%')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#message').text
#     assert 'Имя может содержать только буквы и знак "-"' == messege

# def test_email(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys("ketrin-d")
#     email = driver.find_element(By.CSS_SELECTOR, "#email")
#     email.clear()
#     email.send_keys("ketrin@")
#     driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
#     valid_mes = email.get_property('validationMessage')
#     print(f'Valid message{valid_mes}')


# def test_password(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys("ketrin-d")
#     email = driver.find_element(By.CSS_SELECTOR, "#email").send_keys('ketrin125@mail.ru')
#     password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys('Password123%')
#     confirm_password = driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys('Password123')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#message').text
#     assert 'Пароли не совпадают' == messege

# def test_password_2(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     name = driver.find_element(By.CSS_SELECTOR, "#name").send_keys("ketrin-d")
#     email = driver.find_element(By.CSS_SELECTOR, "#email").send_keys('ketrin125@mail.ru')
#     password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys('Password')
#     confirm_password = driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys('Password')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#message').text
#     assert 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'== messege


# def test_login(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Вход').click()   
#     driver.find_element(By.CSS_SELECTOR, '#login').send_keys("user1")
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)
    
#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user2")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)
    
#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user3")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)

#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user4")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)

#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user5")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)

#     log = driver.find_element(By.CSS_SELECTOR, '#newLogin').send_keys('user6')
#     password = driver.find_element(By.CSS_SELECTOR, '#newPassword').send_keys('Pass1234')
#     driver.find_element(By.CSS_SELECTOR,'#addUserForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#addUserMessage').text
#     assert 'Пользователь добавлен!' == messege
#     time.sleep(1)

#     log = driver.find_element(By.CSS_SELECTOR, '#newLogin')
#     log.clear()
#     log.send_keys('user7')
#     password = driver.find_element(By.CSS_SELECTOR, '#newPassword')
#     password.clear()
#     password.send_keys('Pass1234')
#     driver.find_element(By.CSS_SELECTOR,'#addUserForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#addUserMessage').text
#     assert 'Пользователь добавлен!' == messege
#     time.sleep(1)

#     log = driver.find_element(By.CSS_SELECTOR, '#newLogin')
#     log.clear()
#     log.send_keys('user8')
#     password = driver.find_element(By.CSS_SELECTOR, '#newPassword')
#     password.clear()
#     password.send_keys('Pass1234')
#     driver.find_element(By.CSS_SELECTOR,'#addUserForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#addUserMessage').text
#     assert 'Пользователь добавлен!' == messege
#     time.sleep(1)

#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user6")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)

#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user7")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)

#     login = driver.find_element(By.CSS_SELECTOR, '#login')
#     login.clear()
#     login.send_keys("user8")
#     pas = driver.find_element(By.CSS_SELECTOR, '#password')
#     pas.clear()
#     pas.send_keys("Pass1234")
#     driver.find_element(By.CSS_SELECTOR,'#loginForm button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#loginMessage').text
#     assert 'Вход успешен!' == messege
#     time.sleep(1)


# def test_shop(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Магазин').click() 
#     producy_to_click = [0,1,2]
#     for i in producy_to_click:
        
#         btn_scc = f'.products .product:nth-child({i+1}) button.add-to-cart'
#         product = driver.find_element(By.CSS_SELECTOR, btn_scc)
#         product.click()
#         time.sleep(2)
#         alert = driver.switch_to.alert
#         alert.accept()
    
#     driver.find_element(By. ID, 'cartButton').click()
#     time.sleep(3)


# def test_shop(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'Магазин').click() 
#     producy_to_click = [0,1,2,0]
#     for i in producy_to_click:
        
#         btn_scc = f'.products .product:nth-child({i+1}) button.add-to-cart'
#         product = driver.find_element(By.CSS_SELECTOR, btn_scc)
#         product.click()
#         time.sleep(2)
#         alert = driver.switch_to.alert
#         alert.accept()
    
#     driver.find_element(By. ID, 'cartButton').click()
#     time.sleep(3)

def test_shop(driver):
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.LINK_TEXT, 'Магазин').click() 
    

# def test_db_1(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'База данных').click()
#     request = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     request.send_keys("SELECT * FROM TABLE WHERE name = 'Иван'")
#     driver.find_element(By. ID, 'executeButton').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text
#     assert 'Найдено 1 записей.' == messege
#     time.sleep(2)

# def test_db_2(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'База данных').click()
#     request = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     request.send_keys("DELETE FROM TABLE WHERE ID = 1")
#     driver.find_element(By. ID, 'executeButton').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text
#     assert 'Запись с ID 1 удалена.' == messege
#     time.sleep(2)        

# def test_db_3(driver):
#     driver.get('https://erikdark.github.io/QA_DIPLOM/')
#     driver.find_element(By.LINK_TEXT, 'База данных').click()
#     request = driver.find_element(By.CSS_SELECTOR, '#sqlQuery')
#     request.send_keys("ORDER BY AGE")
#     driver.find_element(By. ID, 'executeButton').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#sqlMessage').text
#     assert 'Данные отсортированы по age.' == messege
#     time.sleep(2)  
   





    










