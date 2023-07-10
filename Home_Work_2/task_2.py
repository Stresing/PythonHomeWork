# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


HEXADECIMAL_NUM: int = 16
hexadecimal: str = ''


def input_num() -> int:  # Ввод данных
    num = int(input('Введите число для перевода его в шестнадцатеричную систему : '))
    return num


def hexadecimal_system():  # функция преобразования числа в 16ю систему
    # global check
    calculate_hexadecimal(num=input_num())
    print(revers_string(hexadecimal))


def calculate_hexadecimal(num: int):
    global hexadecimal
    while num > 16:
        remainder = num % HEXADECIMAL_NUM
        quotient = num // HEXADECIMAL_NUM
        hexadecimal += ''.join(map(str, list_entry(remainder)))
        num = quotient
    hexadecimal += ''.join(map(str, list_entry(num)))


def list_entry(variable: int) -> list[str | int]:  # по 1 цифре не больше 15
    letters_list = ['A', 'B', 'C', 'D', 'E', 'F']
    result_list = []
    if variable > 9:
        for item_index, val in enumerate(letters_list, 10):
            if variable == item_index:
                result_list.insert(0, val)
    else:
        result_list.insert(0, variable)
    return result_list


def revers_string(text: str) -> str:  # разворачивает строку
    global hexadecimal
    res = ''
    for i in range(len(text) - 1, -1, -1):
        res += text[i]
    return res

# hexadecimal_system()  # task_2
