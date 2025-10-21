import math
from .BaseShape import Shape, Point
class Triangle(Shape):
    def __init__(self, tp1: Point, tp2: Point, tp3: Point):
        vertices = [tp1, tp2, tp3]
        super().__init__(vertices)

    def compute_area(self):
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        semiperimeter = (a+b+c)/2
        area = (semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c))**0.5
        self._is_regular = a == b == c
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Los puntos no forman un triángulo válido.")
        return area

    def compute_inner_angles(self):
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        C = 180 - A - B
        self._inner_angles = [A, B, C]
        return self._inner_angles

class Isosceles(Triangle):
    def __init__(self, tp1: Point, tp2: Point, tp3: Point):
        super().__init__(tp1, tp2, tp3)
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        if not ((a == b and b != c) or (a == c and a != b) or (b == c and b != a)):
            raise ValueError("Los lados no corresponden a un triángulo isósceles.")

    def compute_it_area(self):
        return super().compute_area()
    def compute_it_perimeter(self):
        return super().compute_perimeter()
    def compute_it_inner_angles(self):
        return super().compute_inner_angles()

class Equilateral(Triangle):
    def __init__(self, tp1: Point, tp2: Point, tp3: Point):
        super().__init__(tp1, tp2, tp3)
        self._is_regular = True
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        if not (a == b == c):
            raise ValueError("Los lados no corresponden a un tringulo equilatero")

    def compute_et_area(self):
        return super().compute_area()
    def compute_et_perimeter(self):
        return super().compute_perimeter()
    def compute_et_inner_angles(self):
        return super().compute_inner_angles()

class Scalene(Triangle):
    def __init__(self, tp1: Point, tp2: Point, tp3: Point):
        super().__init__(tp1, tp2, tp3)
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        if a == b or a == c or b == c:
            raise ValueError("Los lados no corresponden a un triangulo escaleno")

    def compute_st_area(self):
        return super().compute_area()
    def compute_st_perimeter(self):
        return super().compute_perimeter()
    def compute_st_inner_angles(self):
        return super().compute_inner_angles()

class TriRectangle(Triangle):
    def __init__(self, tp1: Point, tp2: Point, tp3: Point):
        super().__init__(tp1, tp2, tp3)
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        if not (math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2)):
            raise ValueError("No es un triángulo rectángulo")

    def compute_Trt_area(self):
        return super().compute_area()
    def compute_Trt_perimeter(self):
        return super().compute_perimeter()
    def compute_Trt_inner_angles(self):
        return super().compute_inner_angles()