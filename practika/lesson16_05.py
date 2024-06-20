# import re
# def check(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z-0-9.-]+\.[a-zA-Z]{2,}$'
#     if not re.match(pattern, email):
#         return False
#     parts = email.split("@")
#     if len (parts[0])<4:
#         return False
#     else:
#         return True

# print (check ("example@email.com"))         
# print (check ('invalid.email@domain  '))
# print (check ("another.example@sub.domain.com"))
# print (check ("invalid_enother?@domain.name"))
# print (check ('we@domain.name'))


# def check_emails(email):


#     #проверка на наличие собаки
#     if '@' not in email:
#         return False
#     #делим адрес по символу собаки
#     parts = email.split('@')


#     #проверку н наличие логина и домена
#     if len(parts) != 2:
#         return False
   
#     login,domain = parts[0],parts[1]
#     if len (login)<4:
#         return False
   
#     #проверка формата логина
#     if not login or not login.replace('.','').isalnum():
#         return False
    

   
#     #проверка формы домена
#     domain_par = domain.split('.')
#     if len(domain_par) <2 or any(not part.isalnum() for part in domain_par):
#         return False
#     return True


# print(check_emails('example@email.com')) # True
# print(check_emails('invalid.email@domain'))  #False
# print(check_emails('another.example@sub.domain.com'))  #True
# print(check_emails('invalid_enother?@domain.name')) # false
# print(check_emails('we@domain.name')) # false

# list1 = [1,2,3,4,5]
# list2 = [1,2,3,4,1]

# def check_identical(lst):
#     # return all(x == lst[0] for x in lst)
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i]==lst[j]:
#                 return False
#     return True        
            

# print (check_identical(list1))
# print (check_identical(list2))

# import re
# user_database = {
#     "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
#     "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
#     "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
#     "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
# }
# def add_user ():
#     while True:
#         name = input()
#         email = input ()
#         password = input()
#         if not re.match(pattern,mail):
#             pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#             return False
#         if len(password) <8:
#             return False
#         for i in password:
#             if i.islower:
#                 return True
#             if i.isdigit:
#                 return True
#             if i.isspace:
#                 return True
#         if not re.match(pattern2, name):
#             pattern2 = r'[A-Za-z-]'
#             return False
#         if len (name) <2:
#             return False
#         if email in user_database:
#             print ("такой уже есть")
#             continue
#         user_database[email] = {'name': name, 'password': password}


#         print('новый чувак создан')
#         view_database = input('смотрим базу? y/n')
#         if view_database.lower() == 'y':
#             print(user_database)
#             break
# add_user()


        