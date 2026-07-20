from le1.expression.ExpBinaria import ExpBinaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorString import ValorString
from le1.util.Tipo import Tipo


class ExpConcat(ExpBinaria):
    """Expressao de concatenacao entre strings (++)."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorString = self.getEsq().avaliar(ambiente)
        dir_val: ValorString = self.getDir().avaliar(ambiente)
        return ValorString(esq_val.valor() + dir_val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente).eString() and self.getDir().getTipo(ambiente).eString()

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_STRING
