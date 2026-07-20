from li1.expression.ValorConcreto import ValorConcreto
from li1.util.TipoPrimitivo import TipoPrimitivo


class ValorString(ValorConcreto[str]):
    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.STRING

    def __str__(self) -> str:
        return f'"{super().__str__()}"'

    def clone(self) -> "ValorString":
        return ValorString(self.valor())
