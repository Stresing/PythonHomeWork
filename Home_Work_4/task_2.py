'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.'''


def reversed_dict(**kwargs) -> dict:
    some_dict = kwargs
    modified_dict = {}
    for keys, val in some_dict.items():
        if isinstance(val, (int, str, tuple, frozenset)):
            modified_dict[val] = keys
        else:
            modified_dict[str(val)] = keys
    return modified_dict


def start_program():
    print('передаваемые данные: one="asd", two=2, tree=False, four=[4], five={1, 2,} \n',
          reversed_dict(one='asd', two=2, tree=False, four=[4], five={1, 2, }))
