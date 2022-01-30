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

print('Программа для расчета идеального веса, нужно ввести Ваш рост, возраст, пол, и длинну обхвата запястья: ')
rost = int(input('Укажите Ваш рост в сантиметрах: '))
while rost <= 120 or rost >= 220:
    rost = int(input('Рост указан не верно, повторите ввод роста: '))

age = int(input('Укажите Ваш возраст (больше 20 лет): '))
if age <= 19:
    print('Вы слишком молоды для теста.')
    exit(0)
if age >= 100:
    print('Вы слишком стары для теста.')
    exit(0)
else:
    sex = input('Укажите Ваш пол "М, м" или "Ж, ж": ')
    sex = sex.lower()  # как бы пользователь не указал, переводим в нижний регистр
    while sex != 'м' and sex != 'ж':
        sex = input("Введены не верные данные, повторите ввод Вашего пола: ")
        sex = sex.lower()


def get_hand_length():
    while True:
        try:
            hand = int(input('Введите длинну обхвата запястья в сантиметрах: '))
            if 10 <= hand <= 30:
                return hand
            else:
                print('Введены не цифры из диапазона от 10 до 30 см: ')
        except(ValueError):
            print('Введены не цифры: ')

hand = get_hand_length()

def calc_coef(rost):
    if rost <= 165:
        coef = 100
    if 166 >= rost <= 174:
        coef = 105
    if rost >= 175:
        coef = 110
    return coef


# У нас есть 3 типа телосложения. Их нужно определить и ввести.
if sex == 'ж' and hand <= 16 or sex == 'м' and hand <= 17:
    body_type = "small"

elif sex == 'ж' and 17 <= hand <= 18 or sex == 'м' and 18 <= hand <= 19:
    body_type = "normal"

elif sex == 'ж' or hand < 19 or sex == 'м' and hand >= 20:
    body_type = "big"


if 20 <= age <= 30:
    if body_type == "small":
        ves = ((rost - calc_coef(rost)) - ((rost - calc_coef(rost)) * 0.2))  # вычли 20% т.к. вес -10% и тонкость кости -10%
        print('У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "normal":
        ves = ((rost - calc_coef(rost)) - ((rost - calc_coef(rost)) * 0.1))  # вычли 10%, т.к. действует условие возраст
        print('У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "big":
        ves = (rost - calc_coef(rost))  # не вычитали % , т.к. за возраст должны вычесть 10%, а за ширококстность прибавить.
        print('У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
if 31 <= age <= 49:
    if body_type == "small":
        ves = ((rost - calc_coef(rost)) - ((rost - calc_coef(rost)) * 0.1))  # вычли 10% за тонкость кости
        print('У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "normal":
        ves = (rost - calc_coef(rost))  # нет условий возраст и нет тонкости кости или толстости кости.
        print('У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "big":
        ves = ((rost - calc_coef(rost)) + ((rost - calc_coef(rost)) * 0.1))  # прибавили 10% за толстость кости
        print('У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
if age >= 50:
    if body_type == "small":
        ves = ((rost - calc_coef(rost)) - ((rost - calc_coef(rost)) * 0.04))  # вычли 10% за тонкость кости и прибавили 0.6 за возраст
        print('У Вас астенический (тонкокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "normal":
        ves = ((rost - calc_coef(rost)) + ((rost - calc_coef(rost)) * 0.06))  # прибавили 6% за возраст
        print('У Вас нормостенический (нормокостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
    elif body_type == "big":
        ves = ((rost - calc_coef(rost)) + ((rost - calc_coef(rost)) * 0.16))  # прибавили 10% за толстость кости и 6 за возраст
        print('У Вас гиперстенический (ширококостный) тип телосложения, расчетный вес равен: ' + str(round(ves)))
