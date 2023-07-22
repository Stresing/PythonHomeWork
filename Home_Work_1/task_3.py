import click
import os


def task_3():
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