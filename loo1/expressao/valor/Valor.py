from abc import abstractmethod

from loo1.expressao.Expressao import Expressao


class Valor(Expressao):
    @abstractmethod
    def getTipo(self, ambiente=None):
        raise NotImplementedError
