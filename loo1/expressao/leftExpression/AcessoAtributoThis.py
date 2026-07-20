from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.expressao.leftExpression.Id import Id


class AcessoAtributoThis(AcessoAtributo):
    def __init__(self, varThis, id_: Id):
        super().__init__(id_)
        self._varThis = varThis

    def avaliar(self, ambiente=None):
        referencia = self._varThis.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        return objeto.getEstado().get(self.getId())

    def getExpressaoObjeto(self):
        return self._varThis

    def checaTipo(self, ambiente=None) -> bool:
        try:
            resposta = self._varThis.checaTipo(ambiente)
            if resposta:
                tipo = self._varThis.getTipo(ambiente)
                defClasse = ambiente.getDefClasse(tipo.getTipo())
                defClasse.getTipoAtributo(self.getId())
                resposta = True
        except (VariavelNaoDeclaradaException, ClasseNaoDeclaradaException):
            resposta = False
        return resposta

    def getTipo(self, ambiente=None):
        defClasse = ambiente.getDefClasse(self._varThis.getTipo(ambiente).getTipo())
        return defClasse.getTipoAtributo(self.getId())
