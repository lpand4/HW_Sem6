# # 1. Напишите программу, которая будет на вход принимать число N и выводить числа от - N до N
# # *Примеры: *
# # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#
# user_number = int(input("Введите число: "))
# list_m = []
# if user_number>0:
#     My_list = [*range(-user_number, user_number + 1, 1)]
# else:
#     My_list = [*range(user_number, -user_number + 1, 1)]
# print(My_list)
# Уменьшил кол-во кода используя генератор списков/


user_number = abs(int(input("Введите число: ")))
list_m = [i for i in range(-user_number, user_number+1)]
print(*list_m)
