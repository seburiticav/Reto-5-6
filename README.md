# Reto #05 // #06 de POO
Entrega del quinto y sexto reto planteados por Felipe Gonzales Roldan para programacion orientada objetos en la Universidad Nacional de Colombia
## Codigo Planteado (UTILS)
```python
import math
class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self._x = x
        self._y = y

    def move(self, new_x: float, new_y: float):
        self._x = new_x
        self._y = new_y

    def reset(self):
        self._x = 0
        self._y = 0

    def compute_distance(self, point: "Point")-> float:
        return ((self._x - point._x)**2 + (self._y - point._y)**2)**0.5

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_x(self, x: float):
        self._x = x
    def set_y(self, y: float):
        self._y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    def length(self):
        return self._start.compute_distance(self._end)

    def move(self, Lx: float, Ly: float):
        self._start.move(self._start.get_x() + Lx, self._start.get_y() + Ly)
        self._end.move(self._end.get_x() + Lx, self._end.get_y() + Ly)

    def __str__(self):
        return f"({self._start.get_x()}, {self._start.get_y()}) → ({self._end.get_x()}, {self._end.get_y()})"

class Shape:
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
        self._vertices = vertices
        self._edges = self._compute_edges()
        self._is_regular = False
        self._inner_angles = []

    def _compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start, end))
        return edges

    def compute_perimeter(self):
        total = 0
        for edge in self._edges:
            total += edge.length()
        return total

    def compute_area(self):
        raise NotImplementedError("Este método debe implementarse en la subclase.")

    def compute_inner_angles(self):
        raise NotImplementedError("Este método debe implementarse en la subclase.")

    def get_vertices(self):
        return self._vertices
    def get_edges(self):
        return self._edges
    def get_inner_angles(self):
        return self._inner_angles
    def get_is_regular(self):
        return self._is_regular
    def set_vertices(self, vertices):
        self._vertices = vertices
        self._edges = self._compute_edges()
    def set_is_regular(self, value: bool):
        self._is_regular = value
    def set_inner_angles(self, angles):
        self._inner_angles = angles

class Rectangle(Shape):
    def __init__(self, Rp1: Point, Rp2: Point):
        vertices = [
            Point(min(Rp1.get_x(), Rp2.get_x()), min(Rp1.get_y(), Rp2.get_y())),  # bottom-left 
            Point(max(Rp1.get_x(), Rp2.get_x()), min(Rp1.get_y(), Rp2.get_y())),  # bottom-right
            Point(max(Rp1.get_x(), Rp2.get_x()), max(Rp1.get_y(), Rp2.get_y())),  # top-right
            Point(min(Rp1.get_x(), Rp2.get_x()), max(Rp1.get_y(), Rp2.get_y()))   # top-left
        ]
        super().__init__(vertices)
        self._width = self._vertices[1].get_x() - self._vertices[0].get_x()
        self._height = self._vertices[3].get_y() - self._vertices[0].get_y()
        self._is_regular = self._width == self._height

    def compute_area(self):
        return self._width * self._height

    def compute_interference_point(self, point: Point) -> bool:
        return (self._vertices[0].get_x() <= point.get_x() <= self._vertices[2].get_x() and
                self._vertices[0].get_y() <= point.get_y() <= self._vertices[2].get_y())

    def compute_inner_angles(self):
        self._inner_angles = [90, 90, 90, 90]
        return self._inner_angles

class Square(Rectangle):
    def __init__(self, Sp1: Point, Sp2: Point):
        super().__init__(Sp1, Sp2)
        self._is_regular = True
        if self._width != self._height:
            raise ValueError("Los lados no son iguales: no es un cuadrado.")

    def compute_s_area(self):
        return super().compute_area()
    def compute_s_perimeter(self):
        return super().compute_perimeter()
    def compute_s_inner_angles(self):
        return super().compute_inner_angles()

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
```
## Codigo Planteado (MAIN)
```python
if __name__ == "__main__":
    r_p1 = Point(0, 0)
    r_p2 = Point(4, 3)      
    s_p1 = Point(1, 1)
    s_p2 = Point(5, 5)       
    iso_p1 = Point(0, 0)
    iso_p2 = Point(2, 0)
    iso_p3 = Point(1, 2)     
    eq_p1 = Point(0, 0)
    eq_p2 = Point(2, 0)
    eq_p3 = Point(1, math.sqrt(3))
    sc_p1 = Point(0, 0)
    sc_p2 = Point(4, 0)
    sc_p3 = Point(1, 3)      
    tr_p1 = Point(0, 0)
    tr_p2 = Point(3, 0)
    tr_p3 = Point(0, 4)      
    
    rectangle = Rectangle(r_p1, r_p2)
    square = Square(s_p1, s_p2)
    isosceles = Isosceles(iso_p1, iso_p2, iso_p3)
    equilateral = Equilateral(eq_p1, eq_p2, eq_p3)
    scalene = Scalene(sc_p1, sc_p2, sc_p3)
    trirectangle = TriRectangle(tr_p1, tr_p2, tr_p3)

    print("RECTANGULO")
    print("Área:", rectangle.compute_area())
    print("Perímetro:", rectangle.compute_perimeter())
    print("Ángulos internos:", rectangle.compute_inner_angles())
    print("\nCUADRADO")
    print("Area:", square.compute_s_area())
    print("Perimetro:", square.compute_s_perimeter())
    print("Angulos internos:", square.compute_s_inner_angles())
    print("\nISOSCELES")
    print("Area:", isosceles.compute_it_area())
    print("Perimetro:", isosceles.compute_it_perimeter())
    print("Angulos internos:", isosceles.compute_it_inner_angles())
    print("\nEQUILATERO")
    print("Area:", equilateral.compute_et_area())
    print("Perimetro:", equilateral.compute_et_perimeter())
    print("Ángulos internos:", equilateral.compute_et_inner_angles())
    print("\nESCALENO")
    print("Area:", scalene.compute_st_area())
    print("Perimetro:", scalene.compute_st_perimeter())
    print("Ángulos internos:", scalene.compute_st_inner_angles())
    print("\nTRIANGULO RECTANGULO")
    print("Area:", trirectangle.compute_Trt_area())
    print("Perimetro:", trirectangle.compute_Trt_perimeter())
    print("Angulos internos:", trirectangle.compute_Trt_inner_angles())
  #VALORES UTILIZADOS PARA EL EJEMPLO GENERADOS VIA CHAT GPT PARA MAYOR FACILIDAD
```
