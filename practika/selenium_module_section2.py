import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

driver = webdriver.Chrome()


# text_challange = driver.find_element(By.CSS_SELECTOR,'#challenge').text
#     nums = re.findall(r'\d+',text_challange)
#     print(nums)
#     a = int(nums[0])

#     img = driver.find_element(By.CSS_SELECTOR,'#numberImage').text
#     b = img.get_attribute('data-b')
#     b = b.split('?')
#     print(b[1])

   
    


#     anser = a+b
   
#     driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(anser))


#     driver.find_element(By.CSS_SELECTOR, '#notRobot').click()


#     driver.find_element(By.CSS_SELECTOR, '#cool').click()


#     driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()




#     text = driver.find_element(By.CSS_SELECTOR,'#message').text


#     assert 'Поздравляю, Elon Musk!' == text


 

try:

    # driver.get('https://erikdark.github.io/QA_autotests_12/')
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,'#displayText').click()
    
    # confirm = driver.switch_to.alert
    # time.sleep(1)
    # confirm.accept()
    # prompt = driver.switch_to.alert.send_keys('50')

    # prompt.accept()
    
    # driver.find_element(By.CSS_SELECTOR,'#openNewPageBtn').click()
    # new_window = driver.window_handles[1]
    # driver.switch_to.window(new_window)
    # driver.find_element(By.CSS_SELECTOR,'#displayTextBtn').click()
    # text = driver.find_element(By.CSS_SELECTOR, '#displayText').text
    # assert text == 'Я СДЕЛАЛ'

    driver.get('https://erikdark.github.io/QA_autotest_16/')


    element = driver.find_element(By.CSS_SELECTOR,'#price1')
    print(element)
    condition = WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price1'),'550'))
    print(condition)    
  
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'buyButton1'))).click()
   
    message = driver.find_element(By.ID,'message1')
    assert 'Вы успешно купили автомобиль!' in message.text



    


    





   
   



finally:
    time.sleep(5)
    driver.quit()

