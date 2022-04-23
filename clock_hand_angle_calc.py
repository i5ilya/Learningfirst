#  Задача посчитать угол в градусах между стрелками часов. Время вводит пользователь как часы и минуты.

#  Шаг минутной стрелки в градусах. Весь круг 360 градусов, а стрелка делает 60 минут, значит в одной минуте 6
# градусов.
# Шаг в градусах у часовой стрелки. 0,5 градуса за минуту. (30/60), когда минутная стрелка от 0 часов делает 60
# (час дня), то часовая проходит 30 градусов.

# hour = int(input('Введите час: '))
# minute = int(input('Введите минуты: '))

# while True:
#     try:
#         hour = int(input('Введите час: '))
#         if 0 <= hour < 13:
#             break
#         else:
#             print('Введены не числа от 0 до 12, повторите ввод: ')
#     except ValueError:
#         print('Введены не цифры: ')
#
# while True:
#     try:
#         minute = int(input('Введите минуты: '))
#         if 0 <= minute < 60:
#             break
#         else:
#             print('Введены не числа от 0 до 59, повторите ввод: ')
#     except ValueError:
#         print('Введены не цифры: ')

#degree_minute_hand = 6 * minute
#degree_hour_hand = (hour * 30) + (minute * 0.5)


def degree_between_hand(value_degree_minute_hand, value_degree_hour_hand):
    check1 = all([value_degree_hour_hand == 0, value_degree_minute_hand == 0])
    check2 = any([value_degree_hour_hand == 0, value_degree_minute_hand == 0])
    if check1:
        return 0
    if check2:
        if value_degree_minute_hand == 0:
            return 360 - value_degree_hour_hand
        elif value_degree_hour_hand == 0:
            return 360 - value_degree_minute_hand
    if value_degree_hour_hand < value_degree_minute_hand:
        return value_degree_minute_hand - value_degree_hour_hand
    if value_degree_minute_hand < value_degree_hour_hand:
        return value_degree_hour_hand - value_degree_minute_hand


def correction(main_func):
    if main_func >= 181:
        return 360 - main_func
    else:
        return main_func


#right_angle = correction(degree_between_hand(degree_minute_hand, degree_hour_hand))
#angle = 30 * hour + 0.5 * minute - 6 * minute  # какая-то формула

if __name__ == '__main__':
    # print(f'Угол часовой стрелки от нуля часов: {degree_hour_hand}')
    # print(f'Угол минутной стрелки от нуля часов: {degree_minute_hand}')
    # print(f'Угол между стрелками: {degree_between_hand(degree_minute_hand, degree_hour_hand)}')
    # print(f'С учетом коррекции(показываем острый угол): {right_angle}')
    # print(f'Расчет по формуле из интернетов: {angle}')
    minute = 0
    hour = 0
    degree_minute_hand = 6 * minute
    degree_hour_hand = (hour * 30) + (minute * 0.5)

    for hour in range(12):
        for minute in range(60):
            print(f'Время {hour}:{minute}, Угол между стрелками: {correction(degree_between_hand(6 * minute, (hour * 30) + (minute * 0.5)))}')

