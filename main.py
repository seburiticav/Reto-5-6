# ...existing code...
import math
from util.BaseShape import Point, Line, Shape
from util.square_rectangle import Rectangle, Square
from util.triangles import Triangle, Isosceles, Equilateral, Scalene, TriRectangle
from util.exceptions import OperationOverflowError, NegativeSRError, InvalidOperandError, DEFAULT_OPERATION_LIMIT

def safe_add(a, b, limit=DEFAULT_OPERATION_LIMIT):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidOperandError((a, b), "Operandos deben ser numéricos")
    result = a + b
    if result > limit:
        raise OperationOverflowError(result=result, limit=limit)
    return result

def sqrt_op(x):
    if not isinstance(x, (int, float)):
        raise InvalidOperandError(x, "Operando debe ser numérico")
    if x < 0:
        raise NegativeSRError(x)
    return math.sqrt(x)
  
if __name__ == "__main__":
    try:
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

        created = True
        print("Figuras creadas correctamente.")
    except (InvalidOperandError, OperationOverflowError, NegativeSRError) as e:
        created = False
        print(f"Error de operación al crear figuras: {type(e).__name__}: {e}")
    except Exception as e:
        created = False
        print(f"Error inesperado al crear figuras: {type(e).__name__}: {e}")

    if created:
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
    else:
        print("No se pudieron crear las figuras; revisa los errores anteriores.")
#VALORES UTILIZADOS PARA EL EJEMPLO GENERADOS VIA CHAT GPT PARA MAYOR FACILIDAD
