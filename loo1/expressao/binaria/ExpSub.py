from loo1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.expressao.valor.ValorInteiro import ValorInteiro


class ExpSub(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "-")

    def avaliar(self, ambiente=None) -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar(ambiente).valor() - self.getDir().avaliar(ambiente).valor())

    def checaTipo(self, ambiente=None) -> bool:
        return (
            super().checaTipo(ambiente)
            and self.getEsq().getTipo(ambiente).eInteiro()
            and self.getDir().getTipo(ambiente).eInteiro()
        )

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_INTEIRO
