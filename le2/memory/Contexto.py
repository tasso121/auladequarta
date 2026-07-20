from typing import Dict, Generic, List, TypeVar

from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException

T = TypeVar("T")


class Contexto(Generic[T]):
    """Pilha de blocos de escopo mapeando Id -> T. O topo da pilha e o escopo
    mais interno; a busca por um identificador percorre do mais interno ao
    mais externo, implementando shadowing."""

    def __init__(self):
        self._pilha: List[Dict] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        self._pilha.pop()

    def map(self, idArg, valorId: T) -> None:
        topo = self._pilha[-1]
        if idArg in topo:
            raise VariavelJaDeclaradaException(idArg)
        topo[idArg] = valorId

    def get(self, idArg) -> T:
        for escopo in reversed(self._pilha):
            if idArg in escopo:
                return escopo[idArg]
        raise VariavelNaoDeclaradaException(idArg)

    def getPilha(self) -> List[Dict]:
        return self._pilha

    def setPilha(self, pilha: List[Dict]) -> None:
        self._pilha = pilha
