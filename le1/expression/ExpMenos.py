from le1.expression.ExpUnaria import ExpUnaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorInteiro import ValorInteiro
from le1.util.Tipo import Tipo


class ExpMenos(ExpUnaria):
    """Expressao de menos unario (negacao aritmetica)."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorInteiro = self.getExp().avaliar(ambiente)
        return ValorInteiro(-val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_INTEIRO
