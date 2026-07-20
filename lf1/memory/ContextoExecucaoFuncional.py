from le2.memory.Contexto import Contexto
from le2.memory.ContextoExecucao import ContextoExecucao
from lf1.memory.AmbienteExecucaoFuncional import AmbienteExecucaoFuncional


class ContextoExecucaoFuncional(AmbienteExecucaoFuncional):
    """Combina uma pilha de variaveis (reaproveitando ContextoExecucao de le2)
    com uma pilha paralela de funcoes, incrementadas/restauradas em conjunto."""

    def __init__(self):
        self._pilhaIdValor = ContextoExecucao()
        self._pilhaIdValorFunc = Contexto()

    def incrementa(self) -> None:
        self._pilhaIdValor.incrementa()
        self._pilhaIdValorFunc.incrementa()

    def restaura(self) -> None:
        self._pilhaIdValor.restaura()
        self._pilhaIdValorFunc.restaura()

    def mapFuncao(self, idArg, funcao) -> None:
        self._pilhaIdValorFunc.map(idArg, funcao)

    def getFuncao(self, idArg):
        return self._pilhaIdValorFunc.get(idArg)

    def get(self, idArg):
        return self._pilhaIdValor.get(idArg)

    def map(self, idArg, valor) -> None:
        self._pilhaIdValor.map(idArg, valor)

    def getPilhaIdValor(self) -> ContextoExecucao:
        return self._pilhaIdValor

    def getPilhaIdValorFunc(self) -> Contexto:
        return self._pilhaIdValorFunc

    def clone(self) -> "ContextoExecucaoFuncional":
        novo = ContextoExecucaoFuncional()
        novo._pilhaIdValor = self._pilhaIdValor.clone()
        pilhaFuncClonada = Contexto()
        pilhaFuncClonada.setPilha([dict(escopo) for escopo in self._pilhaIdValorFunc.getPilha()])
        novo._pilhaIdValorFunc = pilhaFuncClonada
        return novo
