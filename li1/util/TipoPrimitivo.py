from enum import Enum

from li1.util.Tipo import Tipo


class TipoPrimitivo(Tipo, Enum):
    INTEIRO = "INTEIRO"
    BOOLEANO = "BOOLEANO"
    STRING = "STRING"

    def getNome(self) -> str:
        return self.value

    def eInteiro(self) -> bool:
        return self.eIgual(TipoPrimitivo.INTEIRO)

    def eBooleano(self) -> bool:
        return self.eIgual(TipoPrimitivo.BOOLEANO)

    def eString(self) -> bool:
        return self.eIgual(TipoPrimitivo.STRING)

    def eIgual(self, tipo: Tipo) -> bool:
        if not self.eValido():
            return False
        if tipo.eValido():
            return self.getNome() == tipo.getNome()
        return tipo.eIgual(self)

    def eValido(self) -> bool:
        return bool(self.getNome())

    def intersecao(self, outroTipo: Tipo):
        if outroTipo.eIgual(self):
            return self
        return None

    def __str__(self) -> str:
        return self.getNome()
