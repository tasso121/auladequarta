from loo1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.util.TipoClasse import TipoClasse


class ExpEquals(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente=None) -> ValorBooleano:
        v1 = self.getEsq().avaliar(ambiente)
        v2 = self.getDir().avaliar(ambiente)
        if isinstance(v1, ValorConcreto) and isinstance(v2, ValorConcreto):
            compara = v1.equals(v2)
        else:
            # Valor nao declara equals -- e identidade de objeto (Object.equals
            # por padrao), exatamente como no Java original. E o que faz
            # "this.prox == null" ser False depois que 'prox' aponta para um
            # objeto real: ValorRef nao e ValorConcreto, entao cai aqui.
            compara = v1 is v2
        return ValorBooleano(compara)

    def checaTipo(self, ambiente=None) -> bool:
        if not super().checaTipo(ambiente):
            return False
        tipoEsq = self.getEsq().getTipo(ambiente)
        tipoDir = self.getDir().getTipo(ambiente)
        if isinstance(tipoEsq, TipoClasse):
            return tipoDir.equals(TipoClasse.TIPO_NULL) or tipoEsq.equals(tipoDir)
        return tipoEsq.equals(tipoDir)

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_BOOLEANO
