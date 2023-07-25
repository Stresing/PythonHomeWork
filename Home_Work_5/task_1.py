"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""
import os

FILE_NAME: str = 'task_1.py'  # допустим мы не знаем имя файла.


def pars_path(path: str) -> tuple:
    start_name_file = path.rfind('\\')  # индекс последней обратной косой черты
    len_path = len(path)
    index_name_file_start = len_path - start_name_file - 1  # индекс где начинается название файла
    name_and_extension_file = path[-index_name_file_start::]  # нахождение файла с расширением
    name_file, extension_file = name_and_extension_file.split('.')
    path_file = path[:start_name_file + 1:]  # путь до файла без самого файла с расширением
    return path_file, name_file, extension_file  # не уверен надо ли имя файла добавлять или нет


def start():
    absolute_path: str = os.path.abspath(FILE_NAME)
    print(pars_path(absolute_path))



