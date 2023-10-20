import numpy as np
import re


pocket_money = 1_000_000_000


def the_game() -> int:
    print("Ставка сделана")
    rand_int = np.random.randint(0, 1000)
    print(f'Выпало число: {rand_int}')
    if rand_int == 777:
        print("Ваш выигрыш составил 200 рублей")
        return 200
    elif rand_int == 999:
        print("Ваш выигрыш составил 100 рублей")
        return 100
    elif rand_int == 555:
        print("Ваш выигрыш составил 50 рублей")
        return 50
    elif rand_int == 333:
        print("Ваш выигрыш составил 15 рублей")
        return 15
    elif rand_int == 111:
        print("Ваш выигрыш составил 10 рублей")
        return 10
    elif re.match(r"[1-9]77", str(rand_int)):
        print("Ваш выигрыш составил 5 рублей")
        return 5
    elif re.match(r'[1-9][0-9]7', str(rand_int)):
        print("Ваш выигрыш составил 3 рубля")
        return 3
    elif re.match(r'[1-9]00', str(rand_int)):
        print("Ваш выигрыш составил 2 рубля")
        return 2
    elif re.match(r'[1-9][0-9]0', str(rand_int)):
        print("Ваш выигрыш составил 1 рубль")
        return 1
    else:
        print("Вы не выиграли, вычитаем 1 рубль. Попробуйте еще раз")
        return -1


for i in range(10):
    pocket_money += the_game()
    print(i)

print(pocket_money)