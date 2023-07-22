"""Напишите функцию для транспонирования матрицы"""


def transpositing_any_matrix(some_list: list) -> list:
    matrix_list = [list(line) for line in zip(*some_list)]
    return matrix_list


def transpositing_square_matrix(some_list: list) -> list:
    if len(some_list) is len(some_list[1]):
        matrix_list = [list(line) for line in zip(*some_list)]
        return matrix_list
    else:
        print('Не квадратная матрица')


def print_matrix(matrix_list: list):
    if type(matrix_list) is list:
        print('\n'.join('\t'.join(map(str, row)) for row in matrix_list))


def start_task_1():
    non_square_matrix = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]]

    square_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
    print('№ 1')
    print_matrix(square_matrix)
    print('\n№ 2')
    print_matrix(non_square_matrix)
    print(f'матрица № 1  - квадратная\n'
          f'матрица № 2 - прямоугольная\n')
    choice = int(input('транспонировать матрицу под номером 1 или 2?\nВвод: '))
    choice_yes_or_no = input('Транспонировать не квадратные матрицы можно? да \ нет? \n')
    if choice_yes_or_no.lower() == "да":
        if choice == 1:
            print_matrix(transpositing_any_matrix(square_matrix))
        elif choice == 2:
            print_matrix(transpositing_any_matrix(non_square_matrix))
        else:
            print('вы не выбрали нужную таблицу, попробуйте снова')
            start_task_1()
    elif choice_yes_or_no.lower() == "нет":
        if choice == 1:
            print_matrix(transpositing_square_matrix(square_matrix))
        elif choice == 2:
            print_matrix(transpositing_square_matrix(non_square_matrix))
        else:
            print('вы не выбрали нужную таблицу, попробуйте снова')
            start_task_1()
    else:
        print('Необходимо ответить на вопрос, "да" или "нет" ')
        start_task_1()

# start_task_1()
