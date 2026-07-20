from typing import List, Optional

from li1.util.Lista import Lista
from li1.util.Tipo import Tipo
from li2.declaration.DeclaracaoParametro import DeclaracaoParametro


class ListaDeclaracaoParametro(Lista[DeclaracaoParametro]):
    def __init__(
        self,
        declaracao: Optional[DeclaracaoParametro] = None,
        listaDeclaracao: Optional["ListaDeclaracaoParametro"] = None,
    ):
        super().__init__(declaracao, listaDeclaracao)

    def checaTipo(self, ambiente) -> bool:
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getHead().checaTipo(ambiente) and self.getTail().checaTipo(ambiente)
            return self.getHead().checaTipo(ambiente)
        return True

    def elabora(self, ambiente):
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().elabora(self.getHead().elabora(ambiente))
            return self.getHead().elabora(ambiente)
        return ambiente

    def getTipos(self) -> List[Tipo]:
        retorno: List[Tipo] = []
        headTemp = self.head
        tailTemp = self.tail
        while headTemp is not None:
            retorno.append(headTemp.getTipo())
            if tailTemp is not None:
                headTemp = tailTemp.getHead()
                tailTemp = tailTemp.getTail()
            else:
                headTemp = None
        return retorno
