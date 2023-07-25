"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""
import decimal


def salary_bonus(name_employee: list, hourly_rate: list, interest_rate_str: list) -> dict:
    interest_rate: list = [decimal.Decimal(item[:-1]) for item in interest_rate_str]
    zip_data: zip = zip(name_employee, hourly_rate, interest_rate)
    result: dict = {key: (value * rate_bonus / 100) + value for key, value, rate_bonus in zip_data}
    return result


def start():
    print(salary_bonus(name_employee=["Adam", "Max", "Lana"],
                       hourly_rate=[10000, 12000, 10500],
                       interest_rate_str=["10.35%", "8.93%", "5.23%", ]))


"""Я много пробовал разными способами но запихнуть всё это в одну строку у меня не получилось"""
