class Figure:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimetr(self):
        pass

    def area(self):
        pass

    def __str__(self):
        return f'I am {self.__class__.__name__}, and my perimetr = {self.perimetr()}, my area = {self.area()}'


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b)

    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b)
        self.side_c = side_c

    def perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return (semi_perimeter * (semi_perimeter - self.side_a) * (semi_perimeter - self.side_b) * (
                    semi_perimeter - self.side_c)) ** 0.5


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimetr(self):
        return self.radius * 2 * 3.14


if __name__ == '__main__':
    rectangle = Rectangle(1, 1)
    triangle = Triangle(5, 5, 5)
    circle = Circle(3)
    print(rectangle)
    print(triangle)
    print(circle)
