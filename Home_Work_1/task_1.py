import click
import os


def task_1():
    print('Задача №1:\nНарисовать в консоли ёлку \nЗапросить у пользователя количество рядов.\n')
    row = int(input('Введите количество рядов: '))  # task 1 star-tree
    star = '*'
    empty = ' '
    for i in range(row):
        print(empty * (row - i) + (star * i * 2) + star)