from abc import abstractmethod

from li1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa


class AmbienteExecucaoImperativa2(AmbienteExecucaoImperativa):
    @abstractmethod
    def mapProcedimento(self, idArg, procedimentoId) -> None:
        raise NotImplementedError

    @abstractmethod
    def getProcedimento(self, idArg):
        raise NotImplementedError
