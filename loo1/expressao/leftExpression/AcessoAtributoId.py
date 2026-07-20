from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.expressao.leftExpression.Id import Id


class AcessoAtributoId(AcessoAtributo):
    """Acesso de atributo a partir de uma LeftExpression qualquer (ex.:
    aux.prox), diferente de AcessoAtributoThis (this.prox)."""

    def __init__(self, av, id_: Id):
        super().__init__(id_)
        self._av = av

    def avaliar(self, ambiente=None):
        referencia = self._av.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        return objeto.getEstado().get(self.getId())

    def getExpressaoObjeto(self):
        return self._av

    def getAv(self):
        return self._av

    def checaTipo(self, ambiente=None) -> bool:
        if not self._av.checaTipo(ambiente):
            return False
        try:
            t = self._av.getTipo(ambiente)
            defClasse = ambiente.getDefClasse(t.getTipo())
            defClasse.getTipoAtributo(self.getId())
            return True
        except (VariavelNaoDeclaradaException, ClasseNaoDeclaradaException):
            return False

    def getTipo(self, ambiente=None):
        nomeClasse = self._av.getTipo(ambiente).getTipo()
        defClasse = ambiente.getDefClasse(nomeClasse)
        return defClasse.getTipoAtributo(self.getId())
