from li1.expression.ExpBinaria import ExpBinaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorBooleano import ValorBooleano
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpOr(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "or")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorBooleano = self.getEsq().avaliar(ambiente)
        dir_val: ValorBooleano = self.getDir().avaliar(ambiente)
        return ValorBooleano(esq_val.valor() or dir_val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eBooleano() and self.getDir().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO
