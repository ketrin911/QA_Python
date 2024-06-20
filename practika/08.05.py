# expenses_icomes = {
#     "monday": {"expenses":0, "income":0}, 
#     "tuesday": {"expenses":0, "income":0},
#     "wednsday": {"expenses":0, "income":0},
#     "thursday": {"expenses":0, "income":0},
#     "friday": {"expenses":0, "income":0},
#     "saturday": {"expenses":0, "income":0},
#     "sunday": {"expenses":0, "income":0},
# }

# for day in expenses_icomes:
#     expenses = int(input(f"введте расходы {day}: "))
#     income = int(input(f"введте доходы {day}: "))


# word = input("введите слово: ")
# my_dict = {}
# for i in word:
#     if i in my_dict:
#         my_dict[i] +=1
#     else:
#         my_dict[i] = 1    
# print (my_dict)



work_hours = {}


while True:
    name = input('имя свое пиши или exit: ')
    if name.lower() == 'exit':
        break


    hours_worked = int(input('количество часов пиши: '))
    work_hours[name] = hours_worked


for name, horus in work_hours.items():
    print(f'{name}: {horus}')




