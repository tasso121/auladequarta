from loo1.comando.Comando import Comando
from loo1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.util.TipoClasse import TipoClasse


class Atribuicao(Comando):
    def __init__(self, av, expressao):
        self._av = av
        self._expressao = expressao

    def executar(self, ambiente):
        idVariavel = self._av.getId()
        if isinstance(self._av, AcessoAtributo):
            expAV = self._av.getExpressaoObjeto()
            referencia = expAV.avaliar(ambiente)
            obj = ambiente.getObjeto(referencia)
            obj.changeAtributo(idVariavel, self._expressao.avaliar(ambiente))
        else:
            ambiente.changeValor(idVariavel, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self._expressao.checaTipo(ambiente) and (
            self._av.getTipo(ambiente).equals(self._expressao.getTipo(ambiente))
            or self._expressao.getTipo(ambiente).equals(TipoClasse.TIPO_NULL)
        )
