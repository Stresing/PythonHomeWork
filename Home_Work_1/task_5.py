from random import randint


def task_5():
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
