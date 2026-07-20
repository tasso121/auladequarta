from li1.util.Lista import Lista


class ListaDeclaracaoParametro(Lista):
    def __init__(self, declaracao=None, listaDeclaracao: "ListaDeclaracaoParametro" = None):
        if declaracao is None:
            super().__init__()
        elif listaDeclaracao is None:
            super().__init__(declaracao, None)
        else:
            super().__init__(declaracao, listaDeclaracao)

    def elabora(self, ambiente):
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().elabora(self.getHead().elabora(ambiente))
            return self.getHead().elabora(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getHead().checaTipo(ambiente) and self.getTail().checaTipo(ambiente)
            return self.getHead().checaTipo(ambiente)
        return True

    def declaraParametro(self, ambiente):
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().declaraParametro(self.getHead().declaraParametro(ambiente))
            return self.getHead().declaraParametro(ambiente)
        return ambiente
