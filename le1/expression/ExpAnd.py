from le1.expression.ExpBinaria import ExpBinaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorBooleano import ValorBooleano
from le1.util.Tipo import Tipo


class ExpAnd(ExpBinaria):
    """Expressao de conjuncao logica (and)."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "and")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorBooleano = self.getEsq().avaliar(ambiente)
        dir_val: ValorBooleano = self.getDir().avaliar(ambiente)
        return ValorBooleano(esq_val.valor() and dir_val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eBooleano() and self.getDir().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_BOOLEANO
