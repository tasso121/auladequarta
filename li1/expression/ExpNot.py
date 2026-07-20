from li1.expression.ExpUnaria import ExpUnaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorBooleano import ValorBooleano
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpNot(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorBooleano = self.getExp().avaliar(ambiente)
        return ValorBooleano(not val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO
