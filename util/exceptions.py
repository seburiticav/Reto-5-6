DEFAULT_OPERATION_LIMIT = 9_999_999
class OperationError(Exception):
    """Error base para operaciones."""
    pass

class OperationOverflowError(OperationError):
    """Resultado de la operación excede un limite permitido."""
    def __init__(self, result=None, limit=DEFAULT_OPERATION_LIMIT, message=None):
        msg = message or f"Resultado {result} excede el limite permitido {limit}"
        super().__init__(msg)
        self.result = result
        self.limit = limit

class NegativeSRError(OperationError):
    """Se intento calcular la raiz cuadrada de un numero negativo."""
    def __init__(self, value, message=None):
        msg = message or f"No se puede calcular la raiz de un numero negativo: {value}"
        super().__init__(msg)
        self.value = value

class InvalidOperandError(OperationError):
    """Operando invalido (tipo o formato no esperado)."""
    def __init__(self, operand, message=None):
        msg = message or f"Operando invalido: {operand}"
        super().__init__(msg)
        self.operand = operand
