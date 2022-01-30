""" Расчет идеального веса по формуле Брока. Формула была предложена французским антропологом Полем Броком.
Наиболее простая формула для расчета
— вес равен росту минус коэффициент. При росте до 165 см коэффициент равен 100, до 175 см — 105, выше 175 см — 110.
В формуле можно учесть возраст:
для 20–30 летних вес должен быть уменьшен примерно на 11%, для людей после 50 — увеличен примерно на 6%.
В формуле можно учесть тип телосложения человека — астенический (тонкокостный), нормостенический (нормокостный)
и гиперстенический (ширококостный). Тип телосложения определяют по обхвату запястья рабочей руки.
Для женщин астенический тип — обхват менее 16 см, нормостенический — 16–18 см, больше — гиперстенический.
Для мужчин астенический тип — обхват менее 17 см, нормостенический — 17–20 см, больше — гиперстенический.
Соответственно, для астенического типа вес надо уменьшить примерно на 10%, для гиперстенического — увеличить."""

print('Программа для расчета идеального веса, нужно ввести Ваш рост, возраст, пол, и длину обхвата запястья: ')


def get_height():  # Ввод роста с проверками.
    global height
    while True:
        try:
            height = int(input('Укажите Ваш рост в сантиметрах: '))
            if 120 <= height <= 220:
                return height
            else:
                print('Введены не числа от 120 до 220, повторите ввод: ')
        except ValueError:
            print('Введены не цифры: ')


height = get_height()


def get_age():
    while True:
        try:
            a = int(input('Укажите Ваш возраст (больше 20 лет): '))
            if 20 <= a <= 99:
                return a
            if a <= 19:
                print('Вы слишком молоды для теста')
            if a >= 100:
                print('Вы слишком стары для теста, возраст должен быть от 20 до 99 лет')
            else:
                print('Возраст должен быть от 20 до 99 лет')
        except ValueError:
            print('Ожидаем ввод цифр от 20 до 99')


age = get_age()


def get_user_sex():  # ввод пола пользователя с проверкой
    global sex
    while True:
        sex = input('Укажите Ваш пол "М, м" или "Ж, ж": ')
        sex = sex.lower()
        if sex == 'м' or sex == 'ж':
            return sex
        else:
            print('Введены не верные данные, повторите ввод Вашего пола: ')


sex = get_user_sex()


def get_hand_length():  # Ввод длины запястья с проверками.
    global hand
    while True:
        try:
            hand = int(input('Введите длину обхвата запястья в сантиметрах: '))
            if 10 <= hand <= 30:
                return hand
            else:
                print('Введены не цифры из диапазона от 10 до 30 см: ')
        except ValueError:
            print('Введены не цифры: ')


hand = get_hand_length()


def calc_factor(h):  # Считаем коэффициент, в функцию будем передаем рост - h
    global factor
    if h <= 165:
        factor = 100
    if 166 >= h <= 174:
        factor = 105
    if h >= 175:
        factor = 110
    return factor


factor = calc_factor(height)

# У нас есть 3 типа телосложения. Их нужно определить и ввести.


def calc_body_type(s, h):  # В функцию передаем пол -s и длину запястья -h
    if s == 'ж' and h <= 16 or s == 'м' and h <= 17:
        return 'small'
    elif s == 'ж' and 17 <= h <= 18 or s == 'м' and 18 <= h <= 19:
        return 'normal'
    else:
        return 'big'


body_type = calc_body_type(sex, hand)


if 20 <= age <= 30:
    if body_type == "small":
        ves = ((height - factor) - ((height - factor) * 0.2))  # вычли 20% т.к. вес -10% и тонкость кости -10%
        print(f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "normal":
        ves = ((height - factor) - ((height - factor) * 0.1))  # вычли 10%, т.к. действует условие возраст
        print(f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "big":
        ves = (height - factor)  # не вычитали % , т.к. за возраст должны вычесть 10%, а за ширококстность прибавить.
        print(f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
if 31 <= age <= 49:
    if body_type == "small":
        ves = ((height - factor) - ((height - factor) * 0.1))  # вычли 10% за тонкость кости
        print(f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "normal":
        ves = (height - factor)  # нет условий возраст и нет тонкости кости или толстости кости.
        print(f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "big":
        ves = ((height - factor) + ((height - factor) * 0.1))  # прибавили 10% за толстость кости
        print(f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
if age >= 50:
    if body_type == "small":
        ves = ((height - factor) - ((height - factor) * 0.04))  # вычли 10% за тонкость кости и прибавили 0.6 за возраст
        print(f'У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "normal":
        ves = ((height - factor) + ((height - factor) * 0.06))  # прибавили 6% за возраст
        print(f'У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
    elif body_type == "big":
        ves = ((height - factor) + ((height - factor) * 0.16))  # прибавили 10% за толстость кости и 6 за возраст
        print(f'У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: {round(ves)} кг')
