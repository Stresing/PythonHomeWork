import decimal

# константы для банкомата.
MULTIPLICITY: int = 50
WITHDRAWAL_COMMISSION: decimal.Decimal = decimal.Decimal(1.500)
WITHDRAWAL_MIN_COMMISSION: decimal.Decimal = decimal.Decimal(30)
WITHDRAWAL_MAX_COMMISSION: decimal.Decimal = decimal.Decimal(600)
ACCRUED_INTEREST: decimal.Decimal = decimal.Decimal(3.0)  # 3
TAX_OF_RICHES: decimal.Decimal = decimal.Decimal(10.0)
RICH_BALANCE: int = 5_000_000
transaction_counting: int = 3
balance: decimal.Decimal = decimal.Decimal(0.0)
tax: decimal.Decimal = decimal.Decimal(0.0)
# константы для шестнадцатеричной системы
HEXADECIMAL_NUM: int = 16
hexadecimal: str = ''


def select_operation():
    surcharge()
    choice = input_num()
    print(f'Здравствуйте ваш баланс равен: {balance}'
          '\nВведите номер операции для выполнения:'
          '\nПополнение счёта = 1'
          '\nСнять со счёта = 2'
          '\nВыход = 3'
          '\nВвод: ')  # replenish, withdraw, exit
    if choice == 1:
        print(f'\nВыбрана операция: Пополнить!')
        choice_sum(1)
    elif choice == 2:
        print('\nВыбрана операция: Снять!'
              f'\nВнимание за снятие взимается комиссия равная {WITHDRAWAL_COMMISSION}% от суммы снятия')
        choice_sum(2)
    elif choice == 3:
        exit(f'Ваш баланс: {balance}'
             f'\nВсего доброго!')
    else:
        print('\nВведённая команда не распознана, попробуйте снова.')
        select_operation()


def choice_sum(choice_operation: int):
    global balance
    choice = decimal.Decimal(input('Введите сумму с кратностью 50: '))
    if choice_operation == 1 and choice % MULTIPLICITY == 0:
        replenish(choice)
    elif choice_operation == 2 and choice % MULTIPLICITY == 0:
        if commission(choice) <= balance:
            withdrawals(commission(choice))
        else:
            collection_rich_tax()
            print('Недостаточно денежных средств')
            show_balance()
    else:
        collection_rich_tax()
        print('Данная сумма не имеет кратность 50. Попробуйте снова.')
        show_balance()


def commission(withdrawal_sum: decimal.Decimal) -> decimal.Decimal:  # вычитание комиссии
    global tax
    tax = withdrawal_sum // 100 * WITHDRAWAL_COMMISSION
    if WITHDRAWAL_MIN_COMMISSION < tax < WITHDRAWAL_MAX_COMMISSION:
        withdrawal_sum += tax
    elif WITHDRAWAL_MIN_COMMISSION > tax:
        withdrawal_sum += WITHDRAWAL_MIN_COMMISSION
    elif WITHDRAWAL_MAX_COMMISSION < tax:
        withdrawal_sum += WITHDRAWAL_MAX_COMMISSION
    return decimal.Decimal(withdrawal_sum)


def collection_rich_tax():  # сбор налога для богатых
    global balance, tax
    if balance > RICH_BALANCE:
        tax = balance // 100 * TAX_OF_RICHES
        balance -= tax
        attention_withdrawn_tax()


def attention_withdrawn_tax():
    print(f'Был удержан налог на богатство {tax}')


def surcharge() -> decimal.Decimal:
    global transaction_counting, balance, tax
    if transaction_counting == 0:
        tax = balance // 100 * ACCRUED_INTEREST
        balance + tax
        transaction_counting = 3
    return balance


def replenish(sum_add: decimal.Decimal):
    global balance
    collection_rich_tax()
    balance += sum_add
    transaction_count()
    show_balance()


def withdrawals(sum_lose: decimal.Decimal):
    global balance
    collection_rich_tax()
    balance -= sum_lose
    transaction_count()
    show_balance()


def transaction_count():
    global transaction_counting
    transaction_counting -= 1


def show_balance():
    print(f'Ваш баланс равен {balance}\n')
    select_operation()


# select_operation()  # task_1


def input_num() -> int:  # Ввод данных
    num = int(input('Введите число: '))
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
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f']
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


hexadecimal_system()  # task_2
