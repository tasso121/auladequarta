from le1.expression.ValorConcreto import ValorConcreto
from le1.util.Tipo import Tipo


class ValorString(ValorConcreto[str]):
    """Encapsula um valor string."""

    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_STRING
