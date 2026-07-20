from loo1.comando.ChamadaProcedimento import ChamadaProcedimento
from loo1.comando.Comando import Comando
from loo1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException
from loo1.expressao.leftExpression.Id import Id
from loo1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1

_THIS = Id("this")


class ChamadaMetodo(Comando):
    """ChamadaMetodo ::= Expressao "." Id "(" ListaExpressao ")".

    O corpo do metodo executa num ContextoExecucaoOO1 novo e auxiliar (nao
    no do objeto nem no de quem chama) que so tem 'this' mapeado -- os
    atributos so sao alcancados indiretamente, atraves de AcessoAtributoThis
    indo direto no Objeto.getEstado() via o mapObjetos compartilhado."""

    def __init__(self, expressao, nomeMetodo: Id, parametrosReais):
        self._expressao = expressao
        self._nomeMetodo = nomeMetodo
        self._parametrosReais = parametrosReais

    def executar(self, ambiente):
        vr = self._expressao.avaliar(ambiente)
        objeto = ambiente.getObjeto(vr)
        idClasse = objeto.getClasse()
        defClasse = ambiente.getDefClasse(idClasse)
        metodo = defClasse.getMetodo(self._nomeMetodo)

        aux = ContextoExecucaoOO1(ambiente)
        aux.changeValor(_THIS, vr)

        valoresDosParametros = self._parametrosReais.avaliar(ambiente)
        ChamadaProcedimento(metodo, self._parametrosReais, valoresDosParametros).executar(aux)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        tipoClasse = self._expressao.getTipo(ambiente)
        defClasse = ambiente.getDefClasse(tipoClasse.getTipo())
        try:
            metodo = defClasse.getMetodo(self._nomeMetodo)
        except ProcedimentoNaoDeclaradoException:
            return False
        ambiente.incrementa()
        ambiente.map(_THIS, tipoClasse)
        resposta = ChamadaProcedimento(metodo, self._parametrosReais).checaTipo(ambiente)
        ambiente.restaura()
        return resposta
