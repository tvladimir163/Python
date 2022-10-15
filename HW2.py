# # Задача 1. Напишите программу, которая принимает на вход число N и выдает список 
# # факториалов для чисел от 1 до N.


print("Задача 1")
def zadacha_1(n):
    factorial = 1
    print(f'Фактоиалы числа {n}:')
    for i in range(2, n+1):
        factorial *= i
        print(factorial, end=' ')
    print('\n')
n = int(input("Введите число: "))
zadacha_1(n)


# # Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


print("\nЗадача 2\n")
def zadacha_2():
    print('x | Y | z | ¬(X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} | {int(not(x and y) or z)}')
zadacha_2()


# # Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается 
# # во второй «one» «onetwonine» - o – 2, n – 3, e – 2


print("\nЗадача 3\n")
def zadacha_3():
    element = 'one'
    sentence = 'onetwonine'
    print(f'элементы {element} повторяются:')
    for i in element:
        print(f'{i} {sentence.count(i)} раз/а')
zadacha_3()


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.


print("\nЗадача 4\n")
def zadacha_4():
    numbers = [-3, -2, -1, 0, 1, 2, 3]
    print(numbers)
    print(numbers[len(numbers)-2:len(numbers)]+ numbers[:len(numbers) -2])
zadacha_4()
