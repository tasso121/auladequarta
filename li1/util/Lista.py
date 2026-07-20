from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Lista(Generic[T]):
    """Lista encadeada simples."""

    def __init__(self, valor: Optional[T] = None, lista: Optional["Lista[T]"] = None):
        self.head = valor
        self.tail = lista

    def length(self) -> int:
        if self.head is None:
            return 0
        if self.tail is None:
            return 1
        return 1 + self.tail.length()

    def getHead(self) -> Optional[T]:
        return self.head

    def getTail(self) -> Optional["Lista[T]"]:
        return self.tail

    def __str__(self) -> str:
        partes = []
        no = self
        while no is not None and no.head is not None:
            partes.append(str(no.head))
            no = no.tail
        return " ".join(partes)
