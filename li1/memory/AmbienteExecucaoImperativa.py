from abc import abstractmethod

from li1.memory.AmbienteExecucao import AmbienteExecucao


class AmbienteExecucaoImperativa(AmbienteExecucao):
    @abstractmethod
    def changeValor(self, idArg, valorId) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, v) -> None:
        raise NotImplementedError

    @abstractmethod
    def getSaida(self):
        raise NotImplementedError
