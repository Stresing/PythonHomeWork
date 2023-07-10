import task_1
import task_2
import task_3


def start_program():
    print('\nДобро пожаловать в домашнюю работу № 2! '
          '\nТут находятся невыполненные задания с лекций: 1 номер. '
          '\nТак же тут домашняя работа 2 и 3 номер.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        print('Задание: Банкомат \n')
        task_1.select_operation()
    elif tasks == 2:
        print('Задание: Число в шестнадцатеричную систему')
        task_2.hexadecimal_system()
    elif tasks == 3:
        print('Задание: Сумма и произведение дробей')
        task_3.input_fraction()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет =(')
        start_program()

start_program()
