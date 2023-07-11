# Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

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


def select_operation():
    print(f'Здравствуйте ваш баланс равен: {balance}'
          '\nВведите номер операции для выполнения:'
          '\nПополнение счёта = 1'
          '\nСнять со счёта = 2'
          '\nВыход = 3')  # replenish, withdraw, exit
    choice = input_num()
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
            print(f'Недостаточно денежных средств для снятие: {choice} необходимо: {commission(choice)} из-за комиссии')
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


def surcharge():  # доплата
    global transaction_counting, balance, tax
    if transaction_counting == 0:
        print("доп", transaction_counting)
        tax = balance // 100 * ACCRUED_INTEREST
        print(tax)
        balance += tax
        transaction_counting = 3


def attention_withdrawn_tax():
    print(f'Был удержан налог на богатство {tax}')


def replenish(sum_add: decimal.Decimal):  # пополнение
    global balance
    collection_rich_tax()
    balance += sum_add
    transaction_count()
    surcharge()
    show_balance()


def withdrawals(sum_lose: decimal.Decimal):  # снятие
    global balance
    collection_rich_tax()
    balance -= sum_lose
    transaction_count()
    surcharge()
    show_balance()


def transaction_count():  # Подсчёт транзакций для доплаты
    global transaction_counting
    transaction_counting -= 1


def show_balance():
    print(f'Ваш баланс равен {balance}\n')
    select_operation()


def input_num() -> int:  # Ввод данных
    num = int(input('Введите число: '))
    return num

# select_operation()  # task_1.py
