from abc import ABC, abstractmethod

from li1.expression.Expressao import Expressao


class ExpBinaria(Expressao, ABC):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self.esq = esq
        self.dir = dir
        self._operador = operador

    def getEsq(self) -> Expressao:
        return self.esq

    def getDir(self) -> Expressao:
        return self.dir

    def getOperador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self.esq} {self._operador} {self.dir}"

    def checaTipo(self, ambiente=None) -> bool:
        if not self.getEsq().checaTipo(ambiente) or not self.getDir().checaTipo(ambiente):
            return False
        return self.checaTipoElementoTerminal(ambiente)

    @abstractmethod
    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        raise NotImplementedError

    def reduzir(self, ambiente=None) -> Expressao:
        self.esq = self.esq.reduzir(ambiente)
        self.dir = self.dir.reduzir(ambiente)
        return self

    def clone(self) -> "ExpBinaria":
        """Reconstroi a mesma subclasse concreta clonando as subexpressoes.
        Funciona genericamente pois todo operador binario tem construtor
        (esq, dir) -- evita reescrever clone() em cada subclasse."""
        return type(self)(self.esq.clone(), self.dir.clone())
