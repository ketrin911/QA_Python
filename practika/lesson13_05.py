# import my_module

# my_module.greew("erik")


# my_number = 12



# for i in range(5):
#     a = int(input ("Введите число: "))
#     if a== my_number:
#         print ("Ты угадал чило")
#         break
#     elif a > my_number:
#         print ("мое число меньше, пиши еще раз") 
#     else:
#         print ("мое число больше, пиши еще раз")       
# else:        
#     print ("ты не угадал число")


import random
# my_list = [2,5,9,7,6,7]
# random.shuffle(my_list)
# print (my_list)


# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))
# num = random.randint(a,b)
# print (num)



# num = random.randint(1,6)
# print(num)

# my_list =  ["орел", "решка"]
# result = random.choice(my_list)
# print (result)
    
with open ("rabota_s_tekstom.txt", "r", encoding='utf-8') as file:
    # print (file.read())

    lines = file.readlines()
    print (lines[1::2])
    


