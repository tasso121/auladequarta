from abc import abstractmethod

from li1.memory.AmbienteCompilacao import AmbienteCompilacao


class AmbienteCompilacaoImperativa(AmbienteCompilacao):
    @abstractmethod
    def getTipoEntrada(self):
        raise NotImplementedError
