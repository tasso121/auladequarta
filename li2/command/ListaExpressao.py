from typing import List, Optional

from li1.expression.Expressao import Expressao
from li1.memory.ListaValor import ListaValor
from li1.util.Lista import Lista
from li1.util.Tipo import Tipo


class ListaExpressao(Lista[Expressao]):
    def __init__(
        self,
        expressao: Optional[Expressao] = None,
        listaExpressao: Optional["ListaExpressao"] = None,
    ):
        if expressao is None:
            super().__init__()
        else:
            super().__init__(expressao, listaExpressao if listaExpressao is not None else ListaExpressao())

    def avaliar(self, ambiente) -> ListaValor:
        if self.length() >= 2:
            return ListaValor(self.getHead().avaliar(ambiente), self.getTail().avaliar(ambiente))
        elif self.length() == 1:
            return ListaValor(self.getHead().avaliar(ambiente))
        return ListaValor()

    def getTipos(self, ambiente) -> List[Tipo]:
        result: List[Tipo] = []
        if self.length() >= 2:
            result.append(self.getHead().getTipo(ambiente))
            result.extend(self.getTail().getTipos(ambiente))
        elif self.length() == 1:
            result.append(self.getHead().getTipo(ambiente))
        return result
