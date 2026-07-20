from li1.util.Lista import Lista


class ListaExpressao(Lista):
    def __init__(self, expressao=None, listaExpressao: "ListaExpressao" = None):
        if expressao is None:
            super().__init__()
        elif listaExpressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, listaExpressao)

    def avaliar(self, ambiente=None):
        from loo1.memoria.colecao.ListaValor import ListaValor

        if self.length() >= 2:
            return ListaValor(self.getHead().avaliar(ambiente), self.getTail().avaliar(ambiente))
        if self.length() == 1:
            return ListaValor(self.getHead().avaliar(ambiente))
        return ListaValor()

    def getTipos(self, ambiente=None):
        from loo1.util.ListaTipo import ListaTipo

        if self.length() >= 2:
            return ListaTipo(self.getHead().getTipo(ambiente), self.getTail().getTipos(ambiente))
        if self.length() == 1:
            return ListaTipo(self.getHead().getTipo(ambiente))
        return ListaTipo()
