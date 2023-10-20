def mid_letter_output():
    input_word = input("Введите пожалуйста слово: ")
    len_input_word = len(input_word) / 2
    if len(input_word) % 2 == 0:
        print(input_word[int(len_input_word - 1)] + input_word[int(len_input_word)])
    elif len(input_word) % 2 != 0 and len(input_word) > 1:
        print(input_word[int(len_input_word - 0.5)])
    else:
        print(input_word)


def sum_of_input_numbers():
    input_number = int(input("Введите число: "))
    input_arr = []

    while input_number != 0:
        input_arr.append(input_number)
        input_number = int(input("Введите число: "))

    input_sum = sum(input_arr)
    print(f'Сумма введенных чисел равна {input_sum}')


def dating_mvp(boys: [str], girls: [str]):
    if len(boys) == len(girls):
        boys.sort()
        girls.sort()
        print('Идеальные пары:')
        for b, g in zip(boys, girls):
            print(boys.index(b) + 1, b, ' и ', g)
    else:
        print('Внимание, кто-то может остаться без пары')


def mid_temperature(countries_temperature: []):
    countries_mid_temp_celcius = []
    for ct in countries_temperature:
        countries_mid_temp_celcius.append(
            [ct[0], round(((sum(ct[1]) / len(ct[1]) - 32) / 1.8), 1)]
        )
    print('Средняя температура в странах:')
    for cel in countries_mid_temp_celcius:
        print(countries_mid_temp_celcius.index(cel) + 1, cel[0], '-', cel[1])


def user_views_average(stream: []):
    count = []
    users = []
    for st in stream:
        count.append(
            int(st.split(',')[2])
        )
        users.append(
            st.split(',')[1]
        )
    users = set(users)
    views_average = round((sum(count) / len(users)), 2)

    print(f'Среднее количество просмотров на уникального пользователя: {views_average}')


def repeating_int_output():
    input_arr = input('Введите числа через пробел: ').split(' ')
    dnstr = str()
    for ia in range(len(input_arr)):
        input_arr[ia] = int(input_arr[ia])
    visited = set()
    duplicate_nums = list({x for x in input_arr if x in visited or (visited.add(x) or False)})
    duplicate_nums.sort()
    for dn in duplicate_nums:
        dnstr += str(dn) + ' '
    print(dnstr)



# mid_letter_output()
# sum_of_input_numbers()
# dating_mvp(['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])
# mid_temperature([
#     ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
#     ['Germany', [57.2, 55.4, 59, 59, 53.6]],
#     ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
#     ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ])

# stream_log = stream = [
#     '2018-01-01,user1,3',
#     '2018-01-07,user1,4',
#     '2018-03-29,user1,1',
#     '2018-04-04,user1,13',
#     '2018-01-05,user2,7',
#     '2018-06-14,user3,4',
#     '2018-07-02,user3,10',
#     '2018-03-21,user4,19',
#     '2018-03-22,user4,4',
#     '2018-04-22,user4,8',
#     '2018-05-03,user4,9',
#     '2018-05-11,user4,11',
# ]
#
# user_views_average(stream_log)
# repeating_int_output()


data = [
        [293.0, 101020, 0.35],
        [285.4, 101220, 0.43],
        [282.1, 102020, 0.36],
        [299.2, 100012, 0.32],
        [301.2, 101020, 0.45],
        [300.5, 101920, 0.65],
        [293.8, 101050, 0.45],
]

new_data = []
for row in data:
    temperature = round(row[0] - 272.15, 2)
    pressure = round(row[1]/101325, 2)
    humidity = round(row[2] *100, 2)
    if temperature > 15 and humidity < 60:
        new_data.append([temperature, pressure, humidity])
print(new_data)