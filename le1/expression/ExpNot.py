from le1.expression.ExpUnaria import ExpUnaria
from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorBooleano import ValorBooleano
from le1.util.Tipo import Tipo


class ExpNot(ExpUnaria):
    """Expressao de negacao logica (~)."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self, ambiente=None) -> Valor:
        val: ValorBooleano = self.getExp().avaliar(ambiente)
        return ValorBooleano(not val.valor())

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return self.getExp().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente=None) -> Tipo:
        return Tipo.TIPO_BOOLEANO
