from li1.util.Lista import Lista


class ListaValor(Lista):
    def __init__(self, valor=None, listaValor: "ListaValor" = None):
        if valor is None:
            super().__init__()
        elif listaValor is None:
            super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, listaValor)

    def write(self, valor) -> None:
        if self.getHead() is None:
            self.head = valor
            self.tail = ListaValor()
        else:
            self.getTail().write(valor)

    def __str__(self) -> str:
        partes = []
        no = self
        while no is not None and no.getHead() is not None:
            partes.append(str(no.getHead()))
            no = no.getTail()
        return " ".join(partes)
