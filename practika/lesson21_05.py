# def divisible_three(num):
#     lst_2 = []
#     for i in num:
#         if i % 3 == 0:
#            lst_2.append(i)
#     return lst_2

# print (divisible_three([6,8,3,7,4]))

      
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     if y == 0:
#         return None
#     return x/y
# def calc():
#     while True:
#         n1 = input('Введите число:')
#         n2 = input('Введите число:')
#         # пример валидации всех проверок
#         if not (n1.isnumeric() or (n1.startswith('-') and n1[1:].isnumeric())):
#             print('ошибка введи число')
#             continue
#         if not (n2.isnumeric() or (n2.startswith('-') and n2[1:].isnumeric())):
#             print('ошибка введи число')
#             continue
#         # if not is_valid(n1) or not is_valid(n2):
#         #     print('ошибка введи число')
#         #     continue
#         n1 = int(n1)
#         n2 = int(n2)


#         operator = input('+-/*')


#         if operator == "+":
#             result = add(n1,n2)
#         elif operator == "-":
#             result = subtract(n1,n2)
#         elif operator == "*":
#             result = multiply(n1,n2)
#         elif operator == "/":
#             result = divide(n1,n2)
#             if result is None:
#                 print('Ошибка деления на 0')
#                 continue
#         else:
#             print("неверная операция")
#             continue
#         print(result)
# calc()
# def find_word():
#     text = input("Введите текст: ")
#     word = input("Введите слово для поиска: ") 
#     words = text.split() 
#     if word in words: 
#         return print(f"Слово '{word}' найдено в строке.") 
    
#     else: 
#         return print(f"Слово '{word}' не найдено в строке.")
# find_word ()    
    
# tel_number = [
#    {"name":"маша", "telephone" :"89214521455"},
#    {"name":"вася", "telephone" :"89214455655"},
#    {"name":"катя", "telephone" :"84525662855"}
# ]

# def add_name():
#     while True:
#         name = input ("введите имя: ")
#         telephone = input ("введите телефон: ")
#         tel_number.append  ({'name': name, 'telephone': telephone})
#         print ("сохранено в книгу")
        
#         view_database = input('смотрим базу? y/n')
#         if view_database.lower() == 'y':
#             print(tel_number)
#             break
# add_name()


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Вопросы и ответы
# questions = [
#     Question("Сколько планет в Солнечной системе? (Введите цифру): ", "8"),
#     Question("Как называется самая высокая гора на Земле? ", "Эверест"),
#     Question("Кто написал 'Войну и мир'? ", "Толстой"),
#     Question("Как называется столица Франции? ", "Париж"),
#     Question("Как называется столица Японии? ", "Токио")
# ]

# # Функция для проведения викторины
# def run_quiz(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer.lower() == question.answer.lower():
#             score += 1
#     print("Вы ответили правильно на", score, "из", len(questions), "вопросов.")

# run_quiz(questions)



