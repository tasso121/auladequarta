from enum import Enum, auto
from typing import FrozenSet, Iterable, Optional


class Tipos(Enum):
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()


class Tipo:
    """Representa o(s) possiveis tipo(s) de uma expressao. Objetos sao imutaveis
    (exceto pelo encadeamento 'prox', usado para representar tipos de funcao)."""

    def __init__(self, tipo: Optional[Iterable[Tipos]] = None, prox: Optional["Tipo"] = None):
        self._tipo: FrozenSet[Tipos] = frozenset(tipo) if tipo is not None else frozenset(Tipos)
        self._prox = prox

    def get(self) -> FrozenSet[Tipos]:
        return self._tipo

    def eInteiro(self) -> bool:
        return Tipos.INTEIRO in self._tipo

    def eBooleano(self) -> bool:
        return Tipos.BOOLEANO in self._tipo

    def eString(self) -> bool:
        return Tipos.STRING in self._tipo

    def ePid(self) -> bool:
        return Tipos.PID in self._tipo

    def eTupla(self) -> bool:
        return Tipos.TUPLA in self._tipo

    def eVoid(self) -> bool:
        return len(self._tipo) == 0

    def eValido(self) -> bool:
        return len(self._tipo) == 1

    def intersecao(self, outroTipo: "Tipo") -> "Tipo":
        if self._tipo == outroTipo._tipo:
            return self
        return Tipo(self._tipo & outroTipo._tipo)

    def getProx(self) -> Optional["Tipo"]:
        return self._prox

    def setProx(self, novoProx: Optional["Tipo"]) -> None:
        self._prox = novoProx

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Tipo) and other._tipo == self._tipo

    def __hash__(self) -> int:
        return hash(self._tipo)

    def __repr__(self) -> str:
        return f"Tipo({sorted(t.name for t in self._tipo)})"


Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_PID = Tipo({Tipos.PID})
Tipo.TIPO_TUPLA = Tipo({Tipos.TUPLA})
Tipo.TIPO_INDEFINIDO = Tipo(frozenset())
