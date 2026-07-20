from le1.expression.ExpBinaria import ExpBinaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorBooleano import ValorBooleano
from le1.expression.ValorConcreto import ValorConcreto
from le1.util.Tipo import Tipo


class ExpEquals(ExpBinaria):
    """Expressao de igualdade entre expressoes que avaliam para o mesmo valor primitivo."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente=None) -> Valor:
        esq_val: ValorConcreto = self.getEsq().avaliar(ambiente)
        dir_val: ValorConcreto = self.getDir().avaliar(ambiente)
        return ValorBooleano(esq_val.isEquals(dir_val))

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getEsq().getTipo(ambiente) == self.getDir().getTipo(ambiente)

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_BOOLEANO
