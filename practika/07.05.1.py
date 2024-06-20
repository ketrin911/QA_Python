# nums = [10,20,-5,40,50]

# for num in nums:
#     if num <0:
#         print (num)
#         print("число есть в списке")
#         break
# else:
#     print("нет такого числа")


# for i in range(1,11,1):
#     if i ==5:
#         print("исключение 1")
#         continue
#     if i ==6:
#         print("исключение 2")
#         continue
#     print(i)
   

# test_scores = [75,90,85,60,95]
# prog_scores = [80,70,90,85,75]

# for  item1, item2 in zip(test_scores,prog_scores):
    
#     if item1>80 and item2>80:
#         print(item1,item2) 

# num = 1
# while num <=10:
#     if num == 5 or num == 6:
#         num +=1
#         continue
#     print(num)
#     num +=1


# n = int(input("Число введи: "))
# total = 0
# #цикл for
# for i in range(1,n+1):
#     total+=i
# print(total)


number_copy = 0
max_number_copy = 10

while number_copy<max_number_copy:
    print ("Создание резервных копий", number_copy+1)
    number_copy +=1
    print ("Успешно сознаны")
print (f"тест завершен. Создано {number_copy} копий", "Успешно создана")    
