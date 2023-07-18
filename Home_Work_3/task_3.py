import re
from collections import Counter

#  В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
TOPTEN = 10

text = "Задумка по реализации языка появилась в конце 1980-х годов, а разработка его реализации началась в 1989 году " \
       "сотрудником голландского института CWI Гвидо ван Россумом. " \
       "Для распределённой операционной системы Amoeba требовался расширяемый скриптовый язык," \
       " и Гвидо начал разрабатывать Python на досуге, позаимствовав некоторые наработки для языка ABC " \
       "(Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). " \
       "В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. " \
       "С самого начала Python проектировался как объектно-ориентированный язык."

some_dict = {}
txt_list = re.findall('\w+', text)

counters = Counter(txt_list)
def start():
       print(f'Используемый текст: {text} \n')
       print(sorted(counters, key=counters.get)[-TOPTEN:])
