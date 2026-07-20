from loo1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.expressao.valor.ValorString import ValorString


class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente=None) -> ValorString:
        return ValorString(str(self.getEsq().avaliar(ambiente)) + str(self.getDir().avaliar(ambiente)))

    def checaTipo(self, ambiente=None) -> bool:
        # Fielmente preservado do Java original: "&&" tem precedencia sobre
        # "||", entao isto e (super().checaTipo() and esq.eString()) or
        # dir.eString() -- se o lado direito for string, o resultado e
        # True independente do restante (peculiaridade do fonte original,
        # comentada no Java com "we changed && to ||").
        return (super().checaTipo(ambiente) and self.getEsq().getTipo(ambiente).eString()) or self.getDir().getTipo(
            ambiente
        ).eString()

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_STRING
