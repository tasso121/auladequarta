from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.excecao.declaracao.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from loo1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class ContextoCompilacaoOO1:
    def __init__(self, entrada=None):
        self._pilha = []
        self._pilhaProcedimento = []
        self._mapDefClasse = {}
        self._entrada = entrada

    def incrementa(self) -> None:
        self._pilha.append({})
        self._pilhaProcedimento.append({})

    def restaura(self) -> None:
        self._pilha.pop()
        self._pilhaProcedimento.pop()

    def map(self, idArg, tipoId) -> None:
        topo = self._pilha[-1]
        if idArg in topo:
            raise VariavelJaDeclaradaException(idArg)
        topo[idArg] = tipoId

    def mapParametrosProcedimento(self, idArg, parametrosId) -> None:
        topo = self._pilhaProcedimento[-1]
        if idArg in topo:
            raise ProcedimentoJaDeclaradoException(idArg)
        topo[idArg] = parametrosId

    def mapDefClasse(self, idArg, defClasse) -> None:
        if idArg in self._mapDefClasse:
            raise ClasseJaDeclaradaException(idArg)
        self._mapDefClasse[idArg] = defClasse

    def get(self, idArg):
        for escopo in reversed(self._pilha):
            if idArg in escopo:
                return escopo[idArg]
        raise VariavelNaoDeclaradaException(idArg)

    def getTipo(self, idArg):
        return self.get(idArg)

    def getParametrosProcedimento(self, idArg):
        for escopo in reversed(self._pilhaProcedimento):
            if idArg in escopo:
                return escopo[idArg]
        raise ProcedimentoNaoDeclaradoException(idArg)

    def getDefClasse(self, idArg):
        result = self._mapDefClasse.get(idArg)
        if result is None:
            raise ClasseNaoDeclaradaException(idArg)
        return result

    def getTipoEntrada(self):
        aux = self._entrada.getHead().getTipo(self)
        self._entrada = self._entrada.getTail()
        return aux
