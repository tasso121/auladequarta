from abc import ABC, abstractmethod


class Expressao(ABC):
    @abstractmethod
    def avaliar(self, ambiente=None) -> "Valor":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente=None) -> bool:
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, ambiente=None) -> "Tipo":
        raise NotImplementedError

    @abstractmethod
    def reduzir(self, ambiente=None) -> "Expressao":
        """Retorna uma expressao reduzida, sem ocorrencia de ids conhecidos."""
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> "Expressao":
        raise NotImplementedError
