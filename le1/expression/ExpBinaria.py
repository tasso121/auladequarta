from abc import ABC, abstractmethod

from le1.expression.Expressao import Expressao


class ExpBinaria(Expressao, ABC):
    """Uma expressao binaria contem duas expressoes e um operador."""

    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self._esq = esq
        self._dir = dir
        self._operador = operador

    def getEsq(self) -> Expressao:
        return self._esq

    def getDir(self) -> Expressao:
        return self._dir

    def getOperador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._esq} {self._operador} {self._dir}"

    def checaTipo(self, ambiente=None) -> bool:
        if not self.getEsq().checaTipo(ambiente) or not self.getDir().checaTipo(ambiente):
            return False
        return self.checaTipoElementoTerminal(ambiente)

    @abstractmethod
    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do head terminal."""
        raise NotImplementedError
