class Bird:
    rusClassName = 'Птица'
    count = 0

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        Bird.count += 1

    def info(self):
        print(f'Имя: {self.name}, Род: {Bird.rusClassName}, Возраст: {self.age}, Идентификационный номер: {self.id},', end = ' ')

class Duck(Bird):
    species = "Утка"
    def __init__(self, name, id, age, fly_speed, fly_height):
        super().__init__(name, id, age)
        ''' вместо Bird.__init__(self, name, id, age) Только заметьте, что слово Bird мы заменяем на специальное
        слово super(). Оно обозначает базовый класс. Если не углубляться в дебри, то просто примите, что super()
        используется для вызова инициализатора и методов родительского класса внутри класса-наследника.'''
        self.fly_speed = fly_speed
        self.fly_height = fly_height

    def info(self):
        super().info()  # вместо Bird.info(self)
        print(f'Вид птиц: {Duck.species}', end = ' ')
        print(f'Скорость полета: {self.fly_speed}', end = ' ')
        print(f'Высота полета: {self.fly_height}')

class GalaBacklane (Bird):
    species = "Галапагосский баклан"

    def __init__(self, name, id, age, population):
        super().__init__(name, id, age)
        self.population = population

    def info(self):
        super().info()
        print(f'Вид птиц: {GalaBacklane.species},', end = ' ')
        print(f'Количество особей: {self.population}')



d1 = Duck('Donald Duck', 2, 3, 100, 1000)
d2 = Duck('Jack Duck', 1, 2, 50, 750)
g1 = GalaBacklane('Бакланчик',3, 4, 100)
d1.info()
d2.info()
g1.info()
print(f'Количество птиц: {Bird.count}')
