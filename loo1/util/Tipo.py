from abc import ABC, abstractmethod


class Tipo(ABC):
    """Interface representando um tipo (TipoPrimitivo ou TipoClasse)."""

    @abstractmethod
    def getTipo(self):
        raise NotImplementedError

    @abstractmethod
    def equals(self, obj) -> bool:
        raise NotImplementedError

    @abstractmethod
    def eValido(self, ambiente) -> bool:
        raise NotImplementedError
