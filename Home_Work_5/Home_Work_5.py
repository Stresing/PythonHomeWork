import task_1
import task_2
import task_3


def start_program():
    print('\nДобро пожаловать в домашнюю работу № 5! '
          '\nТут находится домашняя работа c 1 по 3 номер.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        print('\nЗадание: Вернуть путь, имя и расширение файла \n')
        task_1.start()
    elif tasks == 2:
        print('\nЗадание: Расчёт зарплаты с учётом премиальной ставки')
        task_2.start()
    elif tasks == 3:
        print('\nЗадание: Генератор чисел Фибоначчи')
        task_3.start()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет')
        start_program()


start_program()