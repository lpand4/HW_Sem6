# # Напишите1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# # *Пример: *
# #
# # - Для
# # N = 5: 1, -3, 9, -27, 81
#
# user_number = int(input("Введите количество итераций: "))
# my_list = [1]
# for i in range(1,user_number):
#     my_list.append(my_list[i-1]*-3)
# print(f"N = {user_number}: {my_list}")
#
# my_list1 = []
#
# for i in range(user_number):
#     my_list1.append((-3) ** i)
# print(my_list1)
# Тоже добавился генератор списков. Остальные сложные задачи изначально решались с использованием ускоренной обработки,
# поэтому выбрал, что было без их использования
user_number = int(input("Введите количество итераций: "))
print(*list((-3)**i for i in range(user_number)))