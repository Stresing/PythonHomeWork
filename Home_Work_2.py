import math
import decimal

MULTIPLICITY: int = 50
WITHDRAWAL_COMMISSION: float = 1.5
WITHDRAWAL_MIN_COMMISSION: int = 30
WITHDRAWAL_MAX_COMMISSION: int = 600
ACCRUED_INTEREST: decimal.Decimal = 3
TAX_OF_RICHES: float = 10
transaction_counting: int = 3
balance: decimal.Decimal = 0


def select_operation():
    surcharge()
    choice = int(input(f'Здравствуйте ваш баланс равен: {balance}'
                       '\nВведите операцию для выполнения:'
                       '\nПополнение счёта = 1'
                       '\nСнять со счёта = 2'
                       '\nВыход = 3'
                       '\nВвод: '))  # replenish, withdraw, exit
    if choice == 1:
        print(f'\nВыбрана операция пополнения!')

        choice_sum(1)
    elif choice == 2:
        print('\nВыбрана операция снятия!'
              f'\nВнимание за снятие взимается комиссия равная {WITHDRAWAL_COMMISSION}% от суммы снятия')
        choice_sum(2)
    elif choice == 3:
        exit()
    else:
        print('Введённая команда не распознана, попробуйте снова.')


def choice_sum(choice_operation: int):
    global balance
    choice = int(input('Введите сумму с кратностью 50: '))
    if choice_operation == 1 and choice % MULTIPLICITY == 0:
        replenish(choice)
    elif choice_operation == 2 and choice % MULTIPLICITY == 0:
        if commission(choice) <= balance:
            withdrawals(commission(choice))
        else:
            print('Недостаточно денежных средств')
            show_balace()
    else:
        print('Данная сумма не имеет кратность 50. Попробуйте снова.')
        show_balace()


def commission(withdrawal_sum: int):
    sum_commission = withdrawal_sum * WITHDRAWAL_COMMISSION // 100
    if WITHDRAWAL_MIN_COMMISSION < sum_commission < WITHDRAWAL_MAX_COMMISSION:
        withdrawal_sum += sum_commission
    elif WITHDRAWAL_MIN_COMMISSION > sum_commission:
        withdrawal_sum += WITHDRAWAL_MIN_COMMISSION
    elif WITHDRAWAL_MAX_COMMISSION < sum_commission:
        withdrawal_sum += WITHDRAWAL_MAX_COMMISSION
    return withdrawal_sum


def surcharge():
    global transaction_counting, balance
    if transaction_counting == 0:
        balance += (balance * ACCRUED_INTEREST) // 100
        transaction_counting = 3
    return balance


def replenish(sum_add: int):
    global balance
    balance += sum_add
    transaction_count()
    show_balace()



def withdrawals(sum_lose: int):
    global balance
    balance -= sum_lose
    transaction_count()
    show_balace()

def transaction_count():
    global transaction_counting
    transaction_counting -= 1

def show_balace():
    print(f'Ваш баланс равен {balance}\n')
    select_operation()





select_operation()
