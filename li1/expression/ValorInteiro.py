from li1.expression.ValorConcreto import ValorConcreto
from li1.util.TipoPrimitivo import TipoPrimitivo


class ValorInteiro(ValorConcreto[int]):
    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ValorInteiro":
        return ValorInteiro(self.valor())
