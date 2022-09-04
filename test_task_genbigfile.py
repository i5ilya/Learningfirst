#import os
import time
start_time = time.time()
import random

string_part = ('Apple', 'Something something something', 'Cherry is the best', 'Banana is yellow')

def make_file(size_bites):
    size = 0
    with open('text.txt', 'a') as test_file:
        while size < size_bites:
            one_str = str(random.randrange(1, 30432)) + '. ' + random.choice(string_part)
            test_file.write(one_str + '\n')
            size = size + len(one_str.encode("utf8"))

if __name__ == '__main__':
    #make_file(1073741824)  # 1 гигабайт
    make_file(1048576)  # 1 мегабайт
    #make_file(1024)  # 1 килобайт

    print("--- %s seconds ---" % (time.time() - start_time))
