import time
import operator

start_time = time.time()

with open('text.txt') as text_file:
    lines = [line.rstrip() for line in text_file]

'''
Метод str.partition() разбивает строку при первом появлении разделителя sep и вернет кортеж,
содержащий часть строки str перед разделителем, сам разделитель sep и часть строки str после разделителя.
'''

raw_list = []
for item in lines:
    mini_list = []
    mini_list.append(int(item.partition('.')[0])), mini_list.append(item.partition('.')[2].lstrip())
    raw_list.append(mini_list)


sorted_list = sorted(sorted(raw_list, key = lambda x : x[0]), key = lambda x : x[1])

#sorted_list = sorted(raw_list, key=operator.itemgetter(1, 0))


def make_file():
    with open('sorted_text.txt', 'a') as sorted_file:
        # for value in sorted_list:
        #     sorted_file.write(str(value[0])+'. '+value[1] + '\n')
        [sorted_file.write(str(value[0]) + '. ' + value[1] + '\n') for value in sorted_list]


if __name__ == '__main__':
    make_file()
    print("--- %s seconds ---" % (time.time() - start_time))
