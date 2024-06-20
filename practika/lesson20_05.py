# students = [
#     {"names":  "sergey", "grades": [4,3,4,5,3]},
#     {"names": "masha", "grades": [3,4,4,5,3]},
#     {"names": "petya",  "grades": [4,4,3,5,3]},
#     {"names": "katya",  "grades": []}
# ]
# def filter_students(st):
#     filtred_students = []
#     for i in st:
#         grades = i ["grades"]
#         average_grade = sum(grades) / len(grades) if grades else 0
#         if average_grade > 4:
#             filtred_students.append(i['name'])
#     return filtred_students

# print(filter_students(students))

# logs = [
#     '192.168.0.1 /home',
#     '192.168.0.1 /about',
#     '192.168.0.2 /home',
#     '192.168.0.1 /home',
#     '192.168.0.2 /contact',
#     '192.168.0.1 /about',
# ]
# def analyze_logs(logs):


#     ip_dict = {}


#     for log in logs:
#         ip,url = log.split()
#         print(ip,url)
#         if ip not in ip_dict:
#             ip_dict[ip] = set()
#             print(ip_dict)


#         ip_dict[ip].add(url)


#     uniq = {ip:len(url) for ip, url in ip_dict.items()}
#     return uniq


# print(analyze_logs(logs))

#функция для проверки маски ввода телефона

# import re


# def valid_num(num):


#     phone_pattern = r'^\+\d{11}$'


#     if re.match(phone_pattern, num):
#         return True
#     else:
#         return False
   
# print(valid_num('+79956247294'))
# print(valid_num('79956247294'))
# print(valid_num('+7995624'))
# print(valid_num('+asdjsadhsua'))
import re

# def validate_text_length(text, max_len):
#     text = input()
#     max_len = 0


# def check_pass(pas):
#     if len(pas)>8:
#         return True
#     for i in pas:
#         if i.isdigit():
#             return True
#         if i.isalpha():
#             return True
#         if i.find("+", [0],[-1]):
#             return True
#     return False    

# print (check_pass("+Qaewds67"))   
# print (check_pass("Qaewds67")) 
# print (check_pass("Qaewds"))    
    
   
    


        
        
