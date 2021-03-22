import math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    """ Этот метод вызовиться автоматически если мы будем пытаться напечатать точку или преобразовать в строку: 
    p = Point(1,2)
    print(p)
    print("Точка: " + str(p))
     """
    def __str__(self):
        return "(x={0}; y={1})".format(str(self.x), str(self.y))

    """Перегрузка оператора: этот метод будет вызываться, когда мы будем использовать занк -,
      например p1 - p2
     """
    def __sub__(self, other):
        if not isinstance(other, Point):
            raise Error("нельзя вычитать не из точки баранов")

        return Point(self.x - other.x, self.y - other.y)

class Figure:

    def square(self):
        raise Exception("not implemented")

    def __str__(self):
        return "Perimeter of the figure with coord: {0} equals {1}".format(self.get_coord_str(), self.perimeter())

    def get_coord_str(self):
        raise Exception("not implemented")


class Triangle(Figure):

    def __init__(self, s):
        self.coord = [
            Point(s[3], s[5]),
            Point(s[9], s[11]),
            Point(s[15], s[17])
        ]

    def square(self):
        v13 = self.coord[0] - self.coord[2]
        v23 = self.coord[1] - self.coord[2]
        return 1/2* abs(v13.x * v23.y - v13.y * v23.x)

    def perimeter(self):
        a = math.sqrt((self.coord[0].x - self.coord[1].x)**2 + (self.coord[0].y - self.coord[1].y)**2)
        b = math.sqrt((self.coord[0].x - self.coord[2].x)**2 + (self.coord[0].y - self.coord[2].y)**2)
        c = math.sqrt((self.coord[1].x - self.coord[2].x)**2 + (self.coord[1].y - self.coord[2].y)**2)
        return a+b+c


    def get_coord_str(self):
        coord_string_list = [str(point) for point in self.coord]
        coord_string = ", ".join(coord_string_list)
        return "[{0}]".format(coord_string)


class Rectangle(Figure):
    def __init__(self, s):
        self.coord = [
            Point(s[3], s[5]),
            Point(s[9], s[11]),
            Point(s[15], s[17]),
            Point(s[21], s[23]),
        ]

    """ https://doza.pro/art/math/geometry/area-parallelogram """
    def square(self):
        a = (self.coord[3] - self.coord[0]).x
        h = (self.coord[1] - self.coord[0]).y
        return a*h

    def perimeter(self):
        a = (self.coord[3] - self.coord[0]).x
        h = (self.coord[1] - self.coord[0]).y
        return 2*a+2*h

    def get_coord_str(self):
        coord_string_list = [str(point) for point in self.coord]
        coord_string = ", ".join(coord_string_list)
        return "[{0}]".format(coord_string)


class Circle(Figure):
    def __init__(self, s):
        self.coord = [Point(s[3], s[5])]
        self.r = float(s[8])

    def square(self):
        return 3.14*self.r*self.r

    def perimeter(self):
        return 2*3.14*self.r

    def get_coord_str(self):
        coord_string_list = [str(point) for point in self.coord]
        coord_string = ", ".join(coord_string_list)
        return "[{0}]".format(coord_string)