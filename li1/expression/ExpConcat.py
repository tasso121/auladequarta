from li1.expression.ExpBinaria import ExpBinaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorString import ValorString
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpConcat(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorString = self.getEsq().avaliar(ambiente)
        dir_val: ValorString = self.getDir().avaliar(ambiente)
        return ValorString(esq_val.valor() + dir_val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eString() and self.getDir().getTipo(ambiente).eString()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.STRING
