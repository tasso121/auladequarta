from abc import abstractmethod

from le2.memory.Ambiente import Ambiente


class AmbienteExecucao(Ambiente):
    @abstractmethod
    def clone(self) -> "AmbienteExecucao":
        raise NotImplementedError
