from le1.expression.ValorConcreto import ValorConcreto
from le1.util.Tipo import Tipo


class ValorInteiro(ValorConcreto[int]):
    """Encapsula um valor inteiro."""

    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_INTEIRO
