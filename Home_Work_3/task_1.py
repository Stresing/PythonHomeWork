# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции', 'Ножи', 'Вода', 'Еда'
# с множествами. Код должен расширяться , 'Палатка', 'Посуда','Одежда'
# на любое большее количество друзей. , 'Аптечка', 'Палатка', 'Посуда', 'Газовая горелка', 'Фотоаппарат'


friends_Cargo = {'Анатолий': ('Одежда', 'Посуда',),
                 'Сергей': ('Аптечка', 'Еда', 'Одежда',),
                 'Александр': ('Газовая горелка', "Одежда",)}


def uniq_things(some_dict: tuple) -> set:  # все вещи друзей без повторений
    set_1 = set()
    for val in friends_Cargo.values():
        for item in val:
            set_1.add(item)
    return f'Все вещи только без повторов: {set_1}'


def all_things(dic: dict) -> str:  # вещи друзей с повторением
    friend = ''
    for dictionary_tuple in dic.values():
        for item in dictionary_tuple:
            friend += item + ' '

    return f'все предметы которые есть у друзей: {friend}'


def except_things(d: dict, name: str):  # вещи каждого друга
    for key, value in d.items():
        if key != name:
            print(f'{key} взял с собой {value}')


def start():
    print(all_things(friends_Cargo))
    print(uniq_things(friends_Cargo))
    except_things(friends_Cargo, friends_Cargo.values())
