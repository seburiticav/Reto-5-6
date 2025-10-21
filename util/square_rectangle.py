from .BaseShape import Shape, Point

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