from le1.expression.ValorConcreto import ValorConcreto
from le1.util.Tipo import Tipo


class ValorBooleano(ValorConcreto[bool]):
    """Encapsula um valor booleano."""

    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_BOOLEANO
