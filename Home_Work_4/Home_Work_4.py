import ATM_from_seminar_2
import task_1
import task_2


def start_program():
    print('\nДобро пожаловать в домашнюю работу № 4! '
          '\nТут находится домашняя работа c 1 по 3 номер.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        print('\nЗадание: Транспонирования матрицы \n')
        task_1.start_task_1()
    elif tasks == 2:
        print('\nЗадание: Переворот словаря (ключ-значение = значение ключ')
        task_2.start_program()
    elif tasks == 3:
        print('\nЗадание: Банкомат-> функции не менял, добавил функцию записи операций в файл "Operation.txt"')
        ATM_from_seminar_2.select_operation()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет')
        start_program()


start_program()
