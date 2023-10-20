import math


def compare_phrase_length(terminate_cycle=None):
    while terminate_cycle != 'y':
        print("Введите первую фразу:")
        phrase_1 = input()
        print("Введите вторую фразу:")
        phrase_2 = input()
        if len(phrase_1) > len(phrase_2):
            print("Фраза 1 длиннее фразы 2")
        elif len(phrase_1) < len(phrase_2):
            print("Фраза 2 длиннее фразы 1")
        else:
            print("Фразы равной длины")
        terminate_cycle = input("Если хотите завершить цикл, введите 'y':")


def leap_year(terminate_cycle=None):
    def check_int(a):
        try:
            int(a)
            return True
        except ValueError:
            return False

    while terminate_cycle != 'y':
        year_input = input("Введите год для проверки:")
        while not check_int(year_input):
            year_input = input("Некорректный формат данных, попробуйте ввести год еще раз:")
        if int(year_input) % 4 == 0 and int(year_input) % 100 != 0 or int(year_input) % 400 == 0:
            print(f'Год {year_input} является високосным')
        else:
            print(f'Год {year_input} не является високосным')
        terminate_cycle = input("Если хотите завершить цикл, введите 'y':")


def zodiac():
    month_to_int = {
        "Январь": 1,
        "Февраль": 2,
        "Март": 3,
        "Апрель": 4,
        "Май": 5,
        "Июнь": 6,
        "Июль": 7,
        "Август": 8,
        "Сентябрь": 9,
        "Октябрь": 10,
        "Ноябрь": 11,
        "Декабрь": 12,
    }
    day_of_zodiac = int(input("Введите день: "))
    month_of_zodiac = month_to_int[input("Введите месяц: ")]
    if (20 <= day_of_zodiac <= 31 and month_of_zodiac == 1) or (
            1 <= day_of_zodiac <= 18 and month_of_zodiac == 2):
        print("Знак зодиака: Водолей")
    elif (19 <= day_of_zodiac <= 29 and month_of_zodiac == 2) or (
            1 <= day_of_zodiac <= 20 and month_of_zodiac == 3):
        print("Знак зодиака: Рыбы")
    elif (21 <= day_of_zodiac <= 31 and month_of_zodiac == 3) or (
            1 <= day_of_zodiac <= 19 and month_of_zodiac == 4):
        print("Знак зодиака: Овен")
    elif (20 <= day_of_zodiac <= 30 and month_of_zodiac == 4) or (
            1 <= day_of_zodiac <= 20 and month_of_zodiac == 5):
        print("Знак зодиака: Телец")
    elif (21 <= day_of_zodiac <= 31 and month_of_zodiac == 5) or (
            1 <= day_of_zodiac <= 21 and month_of_zodiac == 6):
        print("Знак зодиака: Близнецы")
    elif (22 <= day_of_zodiac <= 30 and month_of_zodiac == 6) or (
            1 <= day_of_zodiac <= 22 and month_of_zodiac == 7):
        print("Знак зодиака: Рак")
    elif (23 <= day_of_zodiac <= 31 and month_of_zodiac == 7) or (
            1 <= day_of_zodiac <= 22 and month_of_zodiac == 8):
        print("Знак зодиака: Лев")
    elif (23 <= day_of_zodiac <= 31 and month_of_zodiac == 8) or (
            1 <= day_of_zodiac <= 22 and month_of_zodiac == 9):
        print("Знак зодиака: Дева")
    elif (23 <= day_of_zodiac <= 30 and month_of_zodiac == 9) or (
            1 <= day_of_zodiac <= 22 and month_of_zodiac == 10):
        print("Знак зодиака: Весы")
    elif (23 <= day_of_zodiac <= 31 and month_of_zodiac == 10) or (
            1 <= day_of_zodiac <= 22 and month_of_zodiac == 11):
        print("Знак зодиака: Скорпион")
    elif (23 <= day_of_zodiac <= 30 and month_of_zodiac == 11) or (
            1 <= day_of_zodiac <= 21 and month_of_zodiac == 12):
        print("Знак зодиака: Стрелец")
    else:
        print("Знак зодиака: Козерог")


def box_selection():
    width = int(input("Введите ширину коробки в сантиметрах: "))
    length = int(input("Введите длину коробки в сантиметрах: "))
    height = int(input("Введите высоту коробки в сантиметрах: "))
    if width <= 15 and length <= 15 and height <= 15:
        print("Коробка №1")
    elif 15 <= width < 50 or 15 <= length < 50 or 15 <= height < 50:
        print("Коробка №2")
    elif length > 200:
        print("Упаковка для лыж")
    else:
        print("Стандартная коробка №3")


def lucky_ticket():
    ticket = list(input("Введите шестизначный номер билета: "))
    for i in range(len(ticket)):
        ticket[i] = int(ticket[i])
    if sum(ticket[:3]) == sum(ticket[3:]):
        print("Счастливый билет")
    else:
        print("Несчастливый билет")


def figure_area():
    figure = input("Введите тип фигуры (Круг, Треугольник, Прямоугольник: ")
    area = 0
    radius = 0
    a = 0
    b = 0
    c = 0
    if figure == "Круг":
        radius = int(input("Введите радиус круга: "))
        area = round((math.pi * radius ** 2), 2)
    elif figure == "Прямоугольник":
        a = int(input("Введите длину стороны А: "))
        b = int(input("Введите длину стороны В: "))
        area = a * b
    elif figure == "Треугольник":
        a = int(input("Введите длину стороны А: "))
        b = int(input("Введите длину стороны В: "))
        c = int(input("Введите длину стороны С: "))
        p = (a + b + c) / 2
        area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    else:
        print("Некорректный формат данных")
        return

    print(f"Площадь {figure}а равна {area}")
    return
