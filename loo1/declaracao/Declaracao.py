from abc import ABC, abstractmethod


class Declaracao(ABC):
    @abstractmethod
    def elabora(self, ambiente):
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente) -> bool:
        raise NotImplementedError
