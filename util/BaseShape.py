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
