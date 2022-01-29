#  Программа подсчитает каких слов больше всего во введённом тексте
import pyperclip
print('Убедитесь, что заранее скопировали текст в буфер обмена')
s = pyperclip.paste()
s = s.lower()  # Все буквы делаем с мальникой
s = s.replace('\n', '')   # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
s = s.replace('\r', '')   # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
#  Удалим знаки препинания
punctuation = ['.', ',', ';', ':', '!', '?', '-', '"', "'", '(', ')', '...', '—', '«', '»']
for i in punctuation:
    s = s.replace(i, '')
mas = s.split(' ')  # разобьем текст на слова, по разделителю пробел, Получим список mas всех слов в тексте.
dic = {}  # Создаем пустой словарь dic


# дальше пока ничего не понимаю...
for x in mas:
    if len(x) > 3:
        k = s.count(x)
        dic[x] = k
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

q = 1
for z in dic:
    if q > 5:
        break
    q = q + 1
    print(str(z))
