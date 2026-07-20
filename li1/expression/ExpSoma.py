from li1.expression.ExpBinaria import ExpBinaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorInteiro import ValorInteiro
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "+")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorInteiro = self.getEsq().avaliar(ambiente)
        dir_val: ValorInteiro = self.getDir().avaliar(ambiente)
        return ValorInteiro(esq_val.valor() + dir_val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eInteiro() and self.getDir().getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO
