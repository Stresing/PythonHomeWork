import math


def task_4():
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