from abc import ABC, abstractmethod

from li1.expression.Expressao import Expressao


class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str):
        self.exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self.exp

    def getOperador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._operador} {self.exp}"

    def checaTipo(self, ambiente=None) -> bool:
        return self.getExp().checaTipo(ambiente) and self.checaTipoElementoTerminal(ambiente)

    @abstractmethod
    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        raise NotImplementedError

    def reduzir(self, ambiente=None) -> Expressao:
        self.exp = self.exp.reduzir(ambiente)
        return self

    def clone(self) -> "ExpUnaria":
        """Reconstroi a mesma subclasse concreta clonando a subexpressao."""
        return type(self)(self.exp.clone())
