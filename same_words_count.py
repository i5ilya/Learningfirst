#  Программа подсчитает каких слов больше всего во введённом тексте
import pyperclip
import string

print('Убедитесь, что заранее скопировали текст в буфер обмена')
s = pyperclip.paste()

s = s.replace('\n', ' ')  # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'
s = s.replace('\r', ' ')  # Удалить знаки переноса строк, которые в Python пишется как '\n' и '\r'


def marks_remove(some_string: str) -> str:  # Удалим знаки препинания
    # punctuation = string.punctuation
    punctuation = ['.', ',', ';', ':', '!', '?', '"', "'", '(', ')', '...', '—', '«', '»', '.', ' - ']
    return ("".join(elements for elements in some_string if elements not in punctuation))


new_s = marks_remove(s)
new_s = new_s.lower()

mas = new_s.split(' ')  # split - метод, который разбивает сроку и делает из нее новый список
for x in mas:  # лишние пробелы превратились в '', удалим их:
    if '' in mas:
        mas.remove('')

unique = set(mas)  # set - метод создания множества. Мы превращаем список в множество. Множества не содержат дублей.

raw_dic = {}  # создадим и зполним словарь, ключ - это слово, значение - число повторений слова в списке.
for word in unique:
    raw_dic[word] = int(mas.count(word))

sorted_dict = {}  # создадим новый словарь
''' Сортировка:  Тут с помощью параметра "key" - указываем как именно осуществлять сортировку
 И мы сортируем по значениям (метод .get возвращает значение ключа). Тоесть, значение - у нас кол-во слов, по нему и сортируем.
 reverse - перевернуть'''
sorted_keys = sorted(raw_dic, key=raw_dic.get, reverse=True)

for k in sorted_keys:  # заполним новый словарь: ключ - отсортированные ключи = значение (число) по ключу из первого словаря.
    sorted_dict[k] = raw_dic[k]

list_one_word = []  # это под список слов, повторяющихся один раз.
for key, value in sorted_dict.items():
    if value > 1:
        print(f'Слово "{key}" : повторений: {value}')
    if value == 1:
        list_one_word.append(key)  # добавим в цикле в список

print(f'Не повторяющиеся слова: {", ".join(list_one_word)}')

# говно код одного "обучателя":

# for x in mas:
#     if len(x) > 3:
#         k = s.count(x)
#         dic[x] = k
# dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
#
# q = 1
# for z in dic:
#     if q > 5:
#         break
#     q = q + 1
#     print(str(z))
