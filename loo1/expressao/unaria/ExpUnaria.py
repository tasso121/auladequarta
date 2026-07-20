from abc import ABC

from loo1.expressao.Expressao import Expressao


class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self._exp

    def getOperador(self) -> str:
        return self._operador

    def checaTipo(self, ambiente=None) -> bool:
        return self.getExp().checaTipo(ambiente)
