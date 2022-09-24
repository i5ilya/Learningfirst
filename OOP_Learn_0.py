class Person:
    def __init__(self, first_name, second_name, age):
        self._first_name = first_name
        self._second_name = second_name
        self.__age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError('Age must be in range 1 - 120')
        self.__age = age

    def describe(self):
        print(f'Im {self._first_name} {self._second_name} and Im {self.__age} years old')



if __name__ == '__main__':
    ilya = Person('ilya', "ilyin", 43)
    ilya.age = 1000  # вообще игнорируется
    ilya.set_age(1)  # и мы должны использовать сеттер
    ilya.describe()
    print(dir(ilya))
