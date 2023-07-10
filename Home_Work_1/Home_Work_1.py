from random import randint

import click
import task_1
import task_2
import task_3
import task_4
import task_5

def start_program():
    print('\nДобро пожаловать в домашнюю работу! №1 '
          '\nТут находятся невыполненные задания с лекций: 1 и 2 '
          '\nТак же тут домашняя работа с 3 по 5 номер.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        task_1.task_1()
    elif tasks == 2:
        task_2.task_2()
    elif tasks == 3:
        task_3.task_3()
    elif tasks == 4:
        task_4.task_4()
    elif tasks == 5:
        task_5.task_5()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет =(')
        start_program()
    start_program()

start_program()
