from le1.expression.ExpUnaria import ExpUnaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorInteiro import ValorInteiro
from le1.expression.ValorString import ValorString
from le1.util.Tipo import Tipo


class ExpLength(ExpUnaria):
    """Expressao de tamanho de uma string."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorString = self.getExp().avaliar(ambiente)
        return ValorInteiro(len(val.valor()))

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eString()

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_INTEIRO
