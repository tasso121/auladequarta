from loo1.expressao.unaria.ExpUnaria import ExpUnaria
from loo1.expressao.valor.ValorInteiro import ValorInteiro


class ExpLength(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao, "length")

    def avaliar(self, ambiente=None) -> ValorInteiro:
        return ValorInteiro(len(self.getExp().avaliar(ambiente).valor()))

    def checaTipo(self, ambiente=None) -> bool:
        return super().checaTipo(ambiente) and self.getExp().getTipo(ambiente).eString()

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_INTEIRO
