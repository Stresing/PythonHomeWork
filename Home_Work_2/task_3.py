# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей.

import re
import turtle


def pars_fraction(fraction_list: list) -> turtle:  # распарсить дроби
    numerator_1: int = int(fraction_list[0])
    numerator_2: int = int(fraction_list[2])
    denominator_1: int = int(fraction_list[1])
    denominator_2: int = int(fraction_list[3])
    return numerator_1, denominator_1, numerator_2, denominator_2


def multiplying(turtle_factrioal: turtle) -> turtle:  # умножение дробей
    common_denominator: int = turtle_factrioal[1] * turtle_factrioal[3]
    common_numerator: int = turtle_factrioal[0] * turtle_factrioal[2]
    return common_numerator, common_denominator


def sum_calculation(turtle_fraction: turtle) -> turtle:  # умножение числителей на множители и
    numerator_1: int = turtle_fraction[0] * turtle_fraction[3]  # приведение к общему знаменателю
    numerator_2: int = turtle_fraction[2] * turtle_fraction[1]
    common_denominator: int = turtle_fraction[1] * turtle_fraction[3]
    common_numerator = numerator_1 + numerator_2
    return common_numerator, common_denominator


def g_c_d(big_num: int, low_num: int) -> int:  # Greatest Common Divisor = НОД =  наибольший общий делитель
    remainder = 1
    if big_num == low_num:
        return low_num
    elif big_num > low_num:
        while remainder != 0:
            remainder = big_num % low_num
            if remainder == 0:
                return low_num
            else:
                big_num, low_num = low_num, remainder
    else:
        big_num, low_num = low_num, big_num
        return g_c_d(big_num, low_num)


def gather_sum(result_turple: turtle):  # сбор ответа по сумме
    if result_turple[1] == 1:
        print(f'ваш результат cуммы : {result_turple[0]}')
    else:
        print(f'ваш результат cуммы : {result_turple[0]}/{result_turple[1]}')


def gather_mult(result_turple: turtle):  # сбор ответа по умножению
    if result_turple[1] == 1:
        print(f'ваш результат умножения : {result_turple[0]}')
    else:
        print(f'ваш результат умножения : {result_turple[0]}/{result_turple[1]}')


def sum_fraction(fraction_list: list):  # сумма дробей
    sum_fractions: turtle = sum_calculation(pars_fraction(fraction_list))
    common_divisor: int = g_c_d(sum_fractions[0], sum_fractions[1])
    gather_sum(reduction_fraction(sum_fractions, common_divisor))


def multiplication(fraction_list: list):  # произведение дробей
    multiple_fractions: turtle = multiplying(pars_fraction(fraction_list))
    common_divisor: int = g_c_d(multiple_fractions[0], multiple_fractions[1])
    gather_mult(reduction_fraction(multiple_fractions, common_divisor))


def reduction_fraction(reduct_turtle: turtle, divisor: int) -> turtle:
    result_numerator: turtle = reduct_turtle[0] // divisor
    result_denominator: turtle = reduct_turtle[1] // divisor
    return result_numerator, result_denominator


def input_fraction():
    text = input('Введите 2 дроби в виде "X/Y" через пробел'
                 '\nДля получения суммы и произведения этих дробей'
                 '\nВвод: ')
    fractions_list = re.split('[/ ]', text)  # 5/2 8/3
    sum_fraction(fractions_list)
    multiplication(fractions_list)


# input_fraction() # task_3
