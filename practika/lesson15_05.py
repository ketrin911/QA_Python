
# try:
#     a = int (input("введи число 1: "))
#     b = int (input("введи число 2: "))
#     result = a/b
#     print (result)

# except ZeroDivisionError:
#     print ("ошибка деления на ноль")

# except ValueError:
#     print ("введи только числа")

# try:
#     file = open ("rabota_s_tekstom1.txt", "r", encoding="utf-8")
#     print (file.read())
# except FileNotFoundError:
#     print ("файл не существует")

# def average (list):
    
#     average = sum (list) / len (list)
#     return average
# list = [6,7,9,6,10]
# print (average(list))

# def test_calc (operator, n1, n2):
#         if operator == "+":
#             return n1 + n2
#         elif operator == "-":
#             return n1 - n2 
#         elif operator =="*":
#             return n1 * n2
#         elif operator == "/":
#             if n2 == 0:
#                 return "делить нельзя"
#             return n1 / n2
#         else:
#             return "неверная операция"

       
    

print(test_calc("+",5,3))
print(test_calc("-",5,3))
print(test_calc("*",5,3))
print(test_calc("/",10,0))
print(test_calc("%",5,3))