from abc import abstractmethod

from le2.memory.AmbienteExecucao import AmbienteExecucao


class AmbienteExecucaoFuncional(AmbienteExecucao):
    """Ambiente de execucao que, alem de variaveis, mapeia identificadores
    para funcoes (ValorFuncao) em uma pilha de escopo propria."""

    @abstractmethod
    def mapFuncao(self, idArg, funcao) -> None:
        raise NotImplementedError

    @abstractmethod
    def getFuncao(self, idArg):
        raise NotImplementedError
