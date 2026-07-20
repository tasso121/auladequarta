from abc import ABC
from typing import Generic, TypeVar

from le1.expression.Valor import Valor

T = TypeVar("T")


class ValorConcreto(Valor, ABC, Generic[T]):
    """Agrupa os diferentes tipos de valores concretos (Inteiro, Booleano, String)."""

    def __init__(self, valor: T):
        self._valor = valor

    def valor(self) -> T:
        """Retorna o valor encapsulado pelo objeto desta classe."""
        return self._valor

    def isEquals(self, obj: "ValorConcreto[T]") -> bool:
        """Determina igualdade entre objetos desta classe."""
        return self.valor() == obj.valor()

    def avaliar(self, ambiente=None) -> "Valor":
        """Retorna o valor deste valor primitivo, i.e., ele mesmo."""
        return self

    def checaTipo(self, ambiente=None) -> bool:
        """Sempre valido para um valor concreto."""
        return True

    def __str__(self) -> str:
        return str(self._valor)
