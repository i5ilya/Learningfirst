# Простой калькулятор
print("Простой калькулятор. Делает 4 действия с двумя введенными числами.")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
except ValueError:
    print('Нужно указывать цифры')
    exit(0)
what = input("Что делаем с числами (+, -, *, /) ? ")
# нужно добавить проверку, что введено число а не буквы
if what == "+":
    c = a + b
    print("результат: " + str(c))
elif what == "-":
    c = a - b
    print("результат: " + str(c))
elif what == "*":
    c = a * b
    print("результат: " + str(c))
elif what == "/":
    c = a / b
    print("результат: " + str(c))
# Второй if или elif. elif пришется тогда, когда после первого if больше не выполнять второй блок.
else:
    print("Выбрана не верная операция")
