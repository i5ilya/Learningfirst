from operator import itemgetter, attrgetter

a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}

sort_by_key = sorted(a_dict.items(), key=itemgetter(0))
sort_by_item = sorted(a_dict.items(), key=itemgetter(1))

# создаем новый отсортированный словарь:
b_dict_key = {key: items for key, items in sort_by_key}
b_dict_item = {key: items for key, items in sort_by_item}


def square(x):
    return x ** 2


square2 = lambda x: x ** 2
even_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'


cats = [Cat('Tom', 3), Cat('Angela', 4)]
cats_sort_by_name = sorted(cats, key=attrgetter('name'))
cats_sort_by_age = sorted(cats, key=attrgetter('age'))

if __name__ == '__main__':
    print(b_dict_key)
    print(b_dict_item)
    # print(sort_by_key)
    # print(sort_by_item)
    # print(cats_sort_by_name)
    # print(cats_sort_by_age)


