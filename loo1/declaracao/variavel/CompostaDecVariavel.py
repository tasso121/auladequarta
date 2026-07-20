from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.declaracao.variavel.DecVariavel import DecVariavel


class CompostaDecVariavel(DecVariavel):
    def __init__(self, declaracao1: DecVariavel, declaracao2: DecVariavel):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def getTipo(self, id_):
        try:
            return self._declaracao1.getTipo(id_)
        except VariavelNaoDeclaradaException:
            return self._declaracao2.getTipo(id_)

    def elabora(self, ambiente):
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente) -> bool:
        return self._declaracao1.checaTipo(ambiente) and self._declaracao2.checaTipo(ambiente)
