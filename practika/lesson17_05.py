import requests


# resp = requests.get('https://ya.ru')
# print(resp.text)
# import requests


# data = {'username': 'user', 'password' : 'pass'}
# resp = requests.post('https://flowerline.shop/wp-login.php', data=data)


# print(resp.json())

# try:
#     response = requests.get('https://easysmarthub.ru/2')
#     response.raise_for_status()
# except:
#     print('ошибка запроса')

# def check_sait(url):
#     resp = requests.get(url)
#     if resp.status_code==200:
#         return True
#     else:
#         return False
# print (check_sait ('https://easysmarthub.ru/2') )    
# print (check_sait ('https://easysmarthub.ru')  )  

import string
import random

# def gener_password():
#     lenght = random.randint(8,32)
#     char = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
#     password = ''.join(random.choice(char) for _ in range(lenght))
#     return password
   
# print (gener_password())    
    
# def sumdigit():
#     summ = 0
#     number = int (input("введите число:"))
#     number = str(number)

#     for digit in number:
#         summ += int(digit)
#     return summ
# print (sumdigit())
    
# def gener_fraza():
#     with open (r"rabota_s_tekstom.txt", 'r', encoding="utf-8"):

# joke_template = [
#     'Почему {} катится вниз?',
#     'Потому что {} смеятся над ним!',
#     'Кто {} в книгах?',
#     'Кто {}?',
#     'Что сказал {} ему {} когда они встретились ?'
# ]
# joke_elements = [
#     'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
#     'водитель','улитка'
# ]

# def generate_joke(): 
#     # Выбираем случайный шаблон 
#     template = random.choice(joke_template) 
#     # Подсчитываем количество элементов, необходимых для заполнения шаблона 
#     num_elements = template.count('{}') 
#     # Выбираем случайные элементы для заполнения шаблона 
#     elements = random.sample(joke_elements, num_elements) 
#     # Заполняем шаблон элементами 
#     joke = template.format(*elements) 
 
#     return joke 
 
# random_joke = generate_joke() 
# print(random_joke)


