from abc import abstractmethod

from le1.expression.Valor import Valor
from le2.memory.Ambiente import Ambiente


class AmbienteExecucao(Ambiente[Valor]):
    @abstractmethod
    def clone(self) -> "AmbienteExecucao":
        raise NotImplementedError
