# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.


# number = int(input("Введите число: "))
# if number == 1:
#     print("'Это понедельник")
# elif number == 2:
#     print("Это вторник")
# elif number == 3:
#     print("Это среда")
# elif number == 4:
#     print("Это четверг")
# elif number == 5:
#     print("Ура, пятница")
# elif number == 6:
#     print("Это суббота")
# elif number == 7:
#     print("Это воскресенье")
# else:
#     print("Такого дня недели нет... (")



# Задача 2. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


# import math
# x1 = float(input("Введите координаты X1: "))
# y1 = float(input("Введите координаты Y1: "))
# x2 = float(input("Введите координаты X2: "))
# y2 = float(input("Введите координаты Y2: "))
# result = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(result)



# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).


# x = float(input("Введите число X: "))
# y = float(input("Введите число Y: "))

# if x > 0 and y > 0:
#     print("координаты первой четверти")
# elif x < 0 and y > 0:
#     print("координаты второй четверти")
# elif x < 0 and y < 0:
#     print("координаты третей четверти")
# elif x > 0 and y < 0:
#     print("координаты четвертой четверти")



# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе 
# показывает все чётные числа от 1 до N.


number = int(input("Введите число: "))
for i in range(2, number + 2, 2):
    print(i, end=", ")