# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

some_list = [1, 3, 4, 5, 1, 6, 3, 8, 2, 5, 7, 7]  # дублирующие 1, 3,5,7
some_set = set()

duplicate = {num for num in some_list if num in some_set or (some_set.add(num) or False)}


def start():
    print(f'Изначальный список элементов: {some_list}')
    print(f'Список с дублирующими списками', list(duplicate))
