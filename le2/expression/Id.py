from le1.expression.Expressao import Expressao
from le1.util.Tipo import Tipo


class Id(Expressao):
    """Referencia a um identificador declarado no ambiente."""

    def __init__(self, idName: str):
        self._idName = idName

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Id) and other._idName == self._idName

    def __hash__(self) -> int:
        return hash(self._idName)

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
