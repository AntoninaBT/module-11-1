# Teplova //
import requests

data = {'key': 'value'}
response = requests.post('https://www.kinopoisk.ru/', data=data)
print(response.text)
# Вывела в консоль все данные со страницы кинопоиска

import pandas
read = pandas.read_csv("example.txt", sep=" ")
"""использую функцию read_csv() для чтения файла."""
print(read)

import numpy
a = numpy.array([8, 4, 5])
print(a)
# вывод списка в консоль