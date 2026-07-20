from abc import ABC, abstractmethod


class Expressao(ABC):
    """Uma expressao e a unidade basica na Linguagem de Expressoes.

    O parametro opcional `ambiente` nao e usado por le1 (que nao tem
    variaveis), mas existe para que le2 em diante reaproveitem estas
    mesmas classes threading o ambiente de execucao/compilacao pela
    arvore de expressoes, em vez de duplica-las.
    """

    @abstractmethod
    def avaliar(self, ambiente=None) -> "Valor":
        """Avalia a expressao retornando seu Valor."""
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente=None) -> bool:
        """Realiza a verificacao de tipos desta expressao."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, ambiente=None) -> "Tipo":
        """Retorna os tipos possiveis desta expressao."""
        raise NotImplementedError
