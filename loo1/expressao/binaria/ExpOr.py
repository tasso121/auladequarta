from loo1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.expressao.valor.ValorBooleano import ValorBooleano


class ExpOr(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "or")

    def avaliar(self, ambiente=None) -> ValorBooleano:
        return ValorBooleano(self.getEsq().avaliar(ambiente).valor() or self.getDir().avaliar(ambiente).valor())

    def checaTipo(self, ambiente=None) -> bool:
        return (
            super().checaTipo(ambiente)
            and self.getEsq().getTipo(ambiente).eBooleano()
            and self.getDir().getTipo(ambiente).eBooleano()
        )

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_BOOLEANO
