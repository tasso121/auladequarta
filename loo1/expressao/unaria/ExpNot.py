from loo1.expressao.unaria.ExpUnaria import ExpUnaria
from loo1.expressao.valor.ValorBooleano import ValorBooleano


class ExpNot(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao, "~")

    def avaliar(self, ambiente=None) -> ValorBooleano:
        return ValorBooleano(not self.getExp().avaliar(ambiente).valor())

    def checaTipo(self, ambiente=None) -> bool:
        return super().checaTipo(ambiente) and self.getExp().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_BOOLEANO
