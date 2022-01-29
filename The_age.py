name = input("Введите свое имя: ")
age = int(input("Укажите свой возраст: "))

if 5 <= age <= 20:
    print("Привет " + name + "!!! " + "Тебе уже " + str(age) + " лет!!!")
else:
    a = str(age)  # ввожу переменную a, которая равна age в виде сроки
    last_digit = int(a[-1])  # эту комбинацию подсмотрел, Получить последний символ строки и преобразовать его в число.

    if last_digit == 2 or last_digit == 3 or last_digit == 4:
        print("Привет " + name + "!!! " + "Тебе уже " + str(age) + " года!!!")
    elif last_digit == 1:  # elif пришется тогда, когда после первого if больше не выполнять второй блок.
        print("Привет " + name + "!!! " + "Тебе уже " + str(age) + " год!!!")
    else:
        print("Привет " + name + "!!! " + "Тебе уже " + str(age) + " лет!!!")

if age <= 20:
    print("Ты еще соплявка!!! Нет Входа")
    #exit(0)
elif age > 100:
    print("You are too old, no enter")
    #exit(0)
else:
    print("Вход разрешаю! ")