from random import randint
import math
import click
import os


def task_1():
    os.system('cls')
    print('Задача №1:\nНарисовать в консоли ёлку \nЗапросить у пользователя количество рядов.\n')
    row = int(input('Введите количество рядов: '))  # task 1 star-tree
    star = '*'
    empty = ' '
    for i in range(row):
        print(empty * (row - i) + (star * i * 2) + star)
    click.pause()
    start_program()


def task_2():
    os.system('cls')
    print('Задача №2:\nВыведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.\n')
    for multiplier in range(2, 11):  # multiplication table
        for multiplicand in range(2, 6):
            exaple = '{0:>2} X {1:^2} = {2:^4}'.format(multiplicand, multiplier, multiplicand * multiplier)
            print(exaple, end='  ')
        print("")
    print("\n ")
    for multiplier in range(2, 11):
        for multiplicand in range(6, 10):
            exaple = '{0:>2} X {1:^2} = {2:^4}'.format(multiplicand, multiplier, multiplicand * multiplier)
            print(exaple, end='  ')
        print("")
    click.pause()
    start_program()


def task_3():
    os.system('cls')
    print('Задача №3:\nДано a, b, c —стороны предполагаемого треугольника \n'
          'Проверить треугольник на существование,\n'
          'Определить этот треугольник: разносторонний, равнобедренный или равносторонний. \n')

    a, b, c = map(int, input('Введите  три стороны треугольника через пробел: ').split())

    if a + b > c and a + c > b and c + b > a:
        print("Треугольник существует и он", end=' ')
        if (a == c and b == c and b == a):
            print('равносторонний.')
        elif a == c or b == c or b == a:
            print('равнобедренный.')
        else:
            print('разносторонний.')
    else:
        print('Такого треугольника не существует.')
    click.pause()
    start_program()


def task_4():
    os.system('cls')
    print('Задача №4: Проверить является введённое число простым\nДелится только на 1 и на себя\n')

    num = -1.0
    while not 0 <= num <= 100000:
        print('Введите целое положительное число, не больше 100 000')
        num = float(input('Ввод: '))
    if num % 2 == 0 and num > 2:
        print('Число чётное и больше 2 значит не простое. ', end='')
    check = True

    while check:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                check = False
                print("Число составное.")
                break
        else:
            print('число простое.')
            break
    click.pause()
    start_program()


def task_5():
    os.system('cls')
    print('Задача №5: 10 попыток на угадывания числа от 0 до 1000\n С подсказками от самой программы=)\n')
    ATTEMPTS = 10
    attempts_left = ATTEMPTS
    num = randint(0, 1000)
    print('Я загадал число от 0 до 1000, угадай его!')

    while attempts_left > 0:
        print('Попыток осталось:', attempts_left, end=' ')
        turn = int(input('Будь осторожен: '))
        attempts_left -= 1
        if turn == num:
            print('Потрясающе ты угадал!')
            break
        elif attempts_left == 0:
            print('попыток не осталось, ты проиграл, пока!')
        elif turn < num and attempts_left == 1:
            print('Число больше, это твоя последняя попытка!')
        elif turn > num and attempts_left == 1:

            print('Число меньше, это твоя последняя попытка!')
        elif turn < num:

            print('Ха, число больше! попробуй снова!')
        elif turn > num:

            print('Ты переборщил, попробуй снова!')
    click.pause()
    start_program()


def start_program():
    os.system('cls')
    print('\nДобро пожаловать в домашнюю работу! '
          '\nТут находятся невыполненные задания с лекций: 1 и 2 '
          '\nТак же тут домашняя работа с 3 по 5 номер.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        task_1()
    elif tasks == 2:
        task_2()
    elif tasks == 3:
        task_3()
    elif tasks == 4:
        task_4()
    elif tasks == 5:
        task_5()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет =(')
        start_program()


start_program()
