from li1.expression.ExpUnaria import ExpUnaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorInteiro import ValorInteiro
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorInteiro = self.getExp().avaliar(ambiente)
        return ValorInteiro(-val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO
