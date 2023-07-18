import task_1
import task_2
import task_3


def start_program():
    print('\nДобро пожаловать в домашнюю работу № 3! '
          '\nТут находятся невыполненные задания с лекций: 1 номер. '
          '\nТак же тут домашняя работа 2 и 3 номер. Без 4го задания.'
          '\nДля выхода из программы введите 0. '
          '\n')
    tasks = int(input('Введите номер задания для проверки: '))
    if tasks == 1:
        print('Задание: Предметы друзей')
        task_1.start()
    elif tasks == 2:
        print('Задание: Вывод дубликов, без дублирующих элементов')
        task_2.start()
    elif tasks == 3:
        print('Задание: Десять повторяющихся слов')
        task_3.start()
    elif tasks == 0:
        exit()
    else:
        print('Задачи под таким номером тут нет')
        start_program()

start_program()