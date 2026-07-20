from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from li1.expression.Expressao import Expressao
from li1.util.Tipo import Tipo


class Id(Expressao):
    def __init__(self, idName: str):
        self._idName = idName

    def __str__(self) -> str:
        return self._idName

    def avaliar(self, ambiente=None) -> "Valor":
        return ambiente.get(self)

    def checaTipo(self, ambiente=None) -> bool:
        ambiente.get(self)
        return True

    def getTipo(self, ambiente=None) -> Tipo:
        return ambiente.get(self)

    def getIdName(self) -> str:
        return self._idName

    def setIdName(self, idName: str) -> None:
        self._idName = idName

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Id) and other._idName == self._idName

    def __hash__(self) -> int:
        return hash(self._idName)

    def reduzir(self, ambiente=None) -> Expressao:
        try:
            valor = ambiente.get(self)
            return valor.clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> "Id":
        return self
