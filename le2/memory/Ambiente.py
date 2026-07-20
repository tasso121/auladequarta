from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Ambiente(Generic[T], ABC):
    """Mapeia identificadores (Id) para valores de tipo T, com escopo em pilha."""

    @abstractmethod
    def incrementa(self) -> None:
        """Abre um novo escopo (bloco)."""
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        """Fecha o escopo mais recente."""
        raise NotImplementedError

    @abstractmethod
    def map(self, idArg, tipoId: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, idArg) -> T:
        raise NotImplementedError
