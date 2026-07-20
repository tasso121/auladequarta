from li1.expression.ValorConcreto import ValorConcreto
from li1.util.TipoPrimitivo import TipoPrimitivo


class ValorBooleano(ValorConcreto[bool]):
    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ValorBooleano":
        return ValorBooleano(self.valor())
