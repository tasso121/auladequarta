from li1.util.Lista import Lista


class ListaValor(Lista):
    """Lista encadeada de Valor -- usada para a fita de entrada e a saida do
    programa (o que foi lido/escrito por Read/SWrite)."""

    def __init__(self, valor=None, listaValor: "ListaValor" = None):
        if valor is None:
            super().__init__()
        else:
            super().__init__(valor, listaValor if listaValor is not None else ListaValor())

    def write(self, valor) -> None:
        if self.getHead() is None:
            self.head = valor
            self.tail = ListaValor()
        else:
            self.getTail().write(valor)
