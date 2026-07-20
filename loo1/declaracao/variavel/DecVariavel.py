from abc import abstractmethod

from loo1.declaracao.Declaracao import Declaracao


class DecVariavel(Declaracao):
    @abstractmethod
    def getTipo(self, id_):
        raise NotImplementedError
