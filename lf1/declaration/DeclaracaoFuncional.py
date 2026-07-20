from abc import ABC, abstractmethod

from le1.expression.Expressao import Expressao
from le1.util.Tipo import Tipo
from le2.expression.Id import Id


class DeclaracaoFuncional(ABC):
    """Uma declaracao dentro de um 'let' funcional: uma variavel (aridade 0)
    ou uma funcao (aridade > 0)."""

    @abstractmethod
    def getID(self) -> Id:
        raise NotImplementedError

    @abstractmethod
    def getAridade(self) -> int:
        """Aridade da declaracao. Variaveis tem aridade 0."""
        raise NotImplementedError

    @abstractmethod
    def getExpressao(self) -> Expressao:
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente=None) -> bool:
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, ambiente=None) -> Tipo:
        raise NotImplementedError
