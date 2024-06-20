import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# def test_registr(driver):
#     driver.get('https://erikdark.github.io/zachet_selenium_01/')
#     driver.find_element(By.LINK_TEXT, 'Регистрация').click()
#     login = driver.find_element(By.CSS_SELECTOR, "#name")
#     login.send_keys('kat')
#     email = driver.find_element(By.CSS_SELECTOR, "#email")
#     email.send_keys('kat@mail.ru')
#     password = driver.find_element(By.CSS_SELECTOR, "#password")
#     password.send_keys('password123')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     btn.click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#register-message').text
#     assert 'Пользователь зарегистрирован' == messege

# def test_login(driver):
#     driver.get('https://erikdark.github.io/zachet_selenium_01/')
#     driver.find_element(By.LINK_TEXT, 'Логин').click()  
#     driver.find_element(By.CSS_SELECTOR, '#email').send_keys('kat@mail.ru')
#     driver.find_element(By.CSS_SELECTOR, '#password').send_keys('password123')
#     btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#login-message').text 
#     assert 'Пользователь вошел в систему' == messege

# def test_profile(driver):
#     driver.get('https://erikdark.github.io/zachet_selenium_01/')
#     driver.find_element(By.LINK_TEXT, 'Профиль').click()  
#     btn = driver.find_element(By.CSS_SELECTOR, '#logout-button').click()
#     messege = driver.find_element(By.CSS_SELECTOR, '#logout-message').text 
#     assert 'Пользователь вышел из системы' == messege

# def test_database(driver):
#     driver.get('https://erikdark.github.io/zachet_selenium_01/')
#     driver.find_element(By.LINK_TEXT, 'Таблица данных').click()  
#     table = driver.find_element(By.CSS_SELECTOR, '#data-table')
#     for col_num in range(3):
#         header = table.find_element(By.XPATH, f"//th[{col_num+1}]")
#         header.click()
#     time.sleep(1)
#     data = [row.find_elements(By.TAG_NAME, "td")[col_num].text for row in table.find_elements(By.TAG_NAME, "tr")[1:]]
#     if data == sorted(data):
#         print(f"Колонка {col_num+1} отсортирована правильно")
#     else:
#         print(f"Колонка {col_num+1} НЕ отсортирована правильно")


# def test_dinamic_content(driver):
#     driver.get('https://erikdark.github.io/zachet_selenium_01/')
#     driver.find_element(By.LINK_TEXT, 'Динамический контент').click()
#     btn = driver.find_element(By.CSS_SELECTOR, '#add-element')
#     if btn:
#         print("Кнопка  присутствует")
#     else:
#         print("Кнопка  отстуствует")
#     btn.click()
#     new_element_text = "Новый элемент"
#     new_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content-area p')))
#     if new_element:
#         print("Новый элемент добавлен")
#     message_element =  WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'content-area'),'Элемент добавлен'))
#     if message_element:
#         print("Сообщение отображается")
  
def test_shadow_dom(driver):
    driver.get('https://erikdark.github.io/SHADOM-DOM-SELENIUM-QA/?name=df&email=EFE%40MAIL.RU')
    shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadow-host")   
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    
    shadow_host_two = shadow_root.find_element(By.CSS_SELECTOR, "#shadow-host-two-host")   
    shadow_root_two = driver.executet('return arguments[0].shadowRoot', shadow_host_two)   
    
    forms = shadow_root_two.find_element(By.CSS_SELECTOR, '#complex-form')
    input_name = forms.find_elements(By.CSS_SELECTOR, "#name")
    input_name.send_keys("Ket")
    input_email = forms.find_elements(By.CSS_SELECTOR, "#email")
    input_email.send_keys("Ket@mail.ru")
   
    time.sleep(3)
    btn = forms.find_elements(By.CSS_SELECTOR, '["type="submit"]')
    btn.click()



