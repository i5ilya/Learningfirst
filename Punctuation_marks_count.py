# Программа для подсчета знаков препинания в введенной пользователем строке.

print('Простейшая программа для подсчета знаков препинания ')
s = str(input('Введите строку и нажмите Enter: '))
z = 0
punctuation = ['.', ',', ';', ':', '!', '?', '-', '"', "'", '(', ')', '...', '—', '«', '»']
for x in s:
    if x in punctuation:
        z = z + 1
print('Знаков препинания в введенной строке: ' + str(z))
