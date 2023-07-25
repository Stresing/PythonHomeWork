'''Создайте функцию генератор чисел Фибоначчи.'''

'''хотел запихнуть в list comprehension, но нашёл информацию, что "yield" не работает, 
в генераторе списков, хотя раньше это было возможно из-за бага'''


def fibinacci(quantity: int) -> object:
    first_num = 0
    second_num = 1
    for __ in range(quantity):
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def start():
    print('Список чисел Фибоначчи: ',
          list(fibinacci(int(input("Введите количество чисел Фибоначчи которое хотите получить: ")))))
