from datetime import datetime as dt
from datetime import timedelta


# Задание 1
# Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:

def newspapers_datetime_formatter():
    dict_of_newspapers = {
        'The Moscow Times': dt.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y'),
        'The Guardian': dt.strptime('Friday, 11.10.13', '%A, %m.%d.%y'),
        'Daily News': dt.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
        }

    for key in dict_of_newspapers:
        print(key, dict_of_newspapers[key])


def date_stream_checker(streamdata: list):
    for st in streamdata:
        try:
            dt.strptime(st, '%Y-%m-%d')
            print("True")
        except ValueError:
            print("False")


def date_range():
    start_date = input("Введите начальную дату в формате 'YYYY-MM-DD': ")
    end_date = input("Введите конечную дату в формате 'YYYY-MM-DD': ")

    try:
        start_date_converted = dt.strptime(start_date, '%Y-%m-%d')
        end_date_converted = dt.strptime(end_date, '%Y-%m-%d')
        date_range_list = []
        if start_date_converted > end_date_converted:
            date_range_list = []
            print(date_range_list)
        else:
            while start_date_converted <= end_date_converted:
                date_range_list.append(start_date_converted.strftime('%Y-%m-%d'))
                start_date_converted += timedelta(days=1)

            print("Список дат от начальной до конечной: ")
            for i, dlt in enumerate(date_range_list):
                print(i+1, dlt)

    except ValueError:
        date_range_list = []
        print(date_range_list)



# newspapers_datetime_formatter()

# stream = ['2018-04-02', '2018-02-29', '2018-19-02']
# date_stream_checker(stream)
# date_range()



# 1. Ошибка означает что указанный/получившийся индекс элемента списка находится вне диапазона длины списка
# 2. При первом запуске программа работает, т.к. ей нужно вернуть элемент списка под номером DEFAULT_USER_COUNT - 2, \
#    то есть второй по счету элемент списка (индекс 1); при первом запуске программы это 'А101'. При втором запуске
#    программы список укорачивается на 1 элемент, и получается что в списке остается лишь элемент 'А100' с индексом 0. Но
#    условием программы все равно является вывести элемент списка с индексом 1, который в списке отстутствует,
#    следовательно выводится ошибка IndexError: list index out of range