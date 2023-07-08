import math
import decimal

WITHDRAWAL_COMMISSION: float = 1.5
WITHDRAWAL_MIN_COMMISSION: int = 30
WITHDRAWAL_MAX_COMMISSION: int = 600
ACCRUED_INTEREST: float = 3
TAX_OF_RICHES: float = 10

def select_operation():
    choice = input('Пополнение счёта = 1\n'
                   'Снять со счёта = 2\n'
                   'Выход = 3\n'
                   'Выберите операцию для выполнения: ') # replenish, withdraw, exit
    if choice == 1:
    elif choice ==2:
    elif choice ==3:
    else:
        'Введёная команда не распознана, попробуйте снова.'


def replenish():


select_operation()