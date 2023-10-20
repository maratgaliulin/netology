import os
import json

f = open('data/visit_log.csv', 'r', encoding='utf-8')

# print(f.readline())
#
# print(next(f))

# content = f.readlines()  # читает весь файл целиком, не рекомендуется использовать для больших файлов
# print(content[-1])

f.seek(0) # переводит курсор на начало читаемого файла

    # Вариант переборки файла №1 - с созданием переменной i:
# i = 0
# for line in f:
#     print(line)
#     i+=1
#     if i >5:
#         break

    # Вариант переборки №2 - с использованием метода enumerate():
# for i, line in enumerate(f):
#     print(i + 1, line)
#     if i > 5:
#         break

    # Использование методов strip() - удалаят символ переноса строки, и split() - разделяет файл по разделителю:

# another_line = f.readline()

# print(another_line.strip().split(','))

# for i, line in enumerate(f):
#     print(i+1, line.strip().split(','))
#     if i > 5:
#         break

f.close()   # Желательно при работе с файлом записать всю необходимую инфу в переменную и потом закрыть файл


# Нежелательный способ работы с файлами - без контекстного менеджера в файл запишутся строки и наложатся одна на другую:

# f = open('results.csv', 'w')
# f.write('Начинаю запись первой строки...\n')
# f.write('Начинаю запись второй строки...\n')
#
# my_friends_results = open('results.csv', 'w')
# my_friends_results.write('Тут еще результаты')
# f.close()
# my_friends_results.close()


# Желательный способ работы с файлами - с использованием контекстного менеджера (в рамках контекстного менеджера будут
# восприниматься только команды с f):

# with open('data/results.csv', 'w') as f:
#     f.write('Начинаю запись первой строки...\n')
#     f.write('Начинаю запись второй строки...\n')
#
#     my_friend_results = open('data/results.csv', 'w')
#     my_friend_results.write('Еще результаты')
#     my_friend_results.close()

# Комбинирование нескольких контекстных менеджеров:

# with open('data/visit_log.csv', 'r') as f:
#     with open('data/visits_context.csv', 'w') as f2write:
#         for line in f:
#             if 'context' in line:
#                 f2write.write(line)
#
# with open('data/visit_log.csv', 'r') as f:
#     with open('data/emails_context.csv', 'w') as f2write:
#         for line in f:
#             if 'email' in line:
#                 f2write.write(line)

# Чтение файлов с помощью модуля os:
# 1) чтение файлов из указанной директории:

# for file in os.listdir('data'):
#     print(file)

# 2) чтение всех файлов и папок, в т.ч. вложенных:

# for root, directory, file in os.walk('data'):
#     print(root, directory, file)


# Чтение файлов в формате json:

# with open('data/purchase_log.txt') as f:
#     print([json.loads(next(f)) for x in range(5)])