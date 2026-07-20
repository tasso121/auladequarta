from abc import ABC, abstractmethod

from le1.expression.Expressao import Expressao


class ExpUnaria(Expressao, ABC):
    """Uma expressao unaria contem uma expressao e um operador sobre a mesma."""

    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self._exp

    def getOperador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._operador} {self._exp}"

    def checaTipo(self, ambiente=None) -> bool:
        return self.getExp().checaTipo(ambiente) and self.checaTipoElementoTerminal(ambiente)

    @abstractmethod
    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do head terminal."""
        raise NotImplementedError
