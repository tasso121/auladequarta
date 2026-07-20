from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from li1.expression.Valor import Valor

T = TypeVar("T")


class ValorConcreto(Valor, ABC, Generic[T]):
    def __init__(self, valor: T):
        self._valor = valor

    def __str__(self) -> str:
        return str(self._valor)

    def valor(self) -> T:
        return self._valor

    def isEquals(self, obj: "ValorConcreto[T]") -> bool:
        return self.valor() == obj.valor()

    def avaliar(self, ambiente=None) -> "Valor":
        return self

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def reduzir(self, ambiente=None) -> "Expressao":
        return self

    def __eq__(self, other: object) -> bool:
        return type(other) is type(self) and self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

    @abstractmethod
    def clone(self) -> "ValorConcreto[T]":
        raise NotImplementedError
