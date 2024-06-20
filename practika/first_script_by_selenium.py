import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:

    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    time.sleep(2)
    #с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
    input_one = driver.find_element(By.ID,'phone')
    input_one.send_keys('89275698532')

    input_two = driver.find_element(By.ID,'email')
    input_two.send_keys('ex@gmail.com')

    input_three = driver.find_element(By.ID,'name')
    input_three.send_keys('ketrin')

    input_for = driver.find_element(By.ID,'password')
    input_for.send_keys('ketrin123')

    
    btn = driver.find_element(By.ID,"submitBtn")
    #с помощью click() мы кликаем по кнопке
    btn.click()
    time.sleep(5)


finally:
    driver.quit()








driver.quit()
