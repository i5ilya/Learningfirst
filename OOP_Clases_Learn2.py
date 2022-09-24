# Inheritance - Наследование - это механизм получения доступа к данным и поведению своего предка.
# И расширение (изменения поведения) классов не меняя код родительского класса
# IS A - является. Правильное наследование - наш наследник является тем же самым! Спрашиваем себя, является ли? Главное правило!
# HAS A - содержит. Композиция

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()} uah'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, 105000, 100)
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):  # мы тут переопределили функцию из родительского класса
        return 200_000

if __name__ == '__main__':
    masha = Cleaner('Anna Mikolaevna')
    print(masha)
    valera = Manager('Valerik')
    print(valera)
    igor_a = CEO('Ihor Alek', 107000, 101)
    print(igor_a)
