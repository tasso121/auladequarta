from li1.expression.ExpUnaria import ExpUnaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorInteiro import ValorInteiro
from li1.expression.ValorString import ValorString
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpLength(ExpUnaria):
    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorString = self.getExp().avaliar(ambiente)
        return ValorInteiro(len(val.valor()))

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eString()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO
