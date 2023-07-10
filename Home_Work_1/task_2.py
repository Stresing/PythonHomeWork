import click
import os


def task_2():
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