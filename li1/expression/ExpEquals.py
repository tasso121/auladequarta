from li1.expression.ExpBinaria import ExpBinaria
from li1.expression.Expressao import Expressao
from li1.expression.Valor import Valor
from li1.expression.ValorBooleano import ValorBooleano
from li1.expression.ValorConcreto import ValorConcreto
from li1.util.TipoPrimitivo import TipoPrimitivo


class ExpEquals(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorConcreto = self.getEsq().avaliar(ambiente)
        dir_val: ValorConcreto = self.getDir().avaliar(ambiente)
        return ValorBooleano(esq_val.isEquals(dir_val))

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eIgual(self.getDir().getTipo(ambiente))

    def getTipo(self, ambiente=None) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO
