from typing import Dict, List

from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.util.Tipo import Tipo
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    """let var d1, d2, ... in expressao — abre um novo escopo com os
    vinculos de d1..dn (avaliados no escopo externo) e avalia a expressao
    resultante nesse novo escopo."""

    def __init__(self, declaracoes: List["DecVariavel"], expressao: Expressao):
        self._seqDecVariavel = declaracoes
        self._expressao = expressao

    def avaliar(self, ambiente=None) -> Valor:
        ambiente.incrementa()
        resolvidos = self._resolveValueBindings(ambiente)
        self._includeValueBindings(ambiente, resolvidos)
        resultado = self._expressao.avaliar(ambiente)
        ambiente.restaura()
        return resultado

    def _includeValueBindings(self, ambiente, resolvidos: Dict[Id, Valor]) -> None:
        for id_, valor in resolvidos.items():
            ambiente.map(id_, valor)

    def _resolveValueBindings(self, ambiente) -> Dict[Id, Valor]:
        return {d.getID(): d.getExpressao().avaliar(ambiente) for d in self._seqDecVariavel}

    def checaTipo(self, ambiente=None) -> bool:
        ambiente.incrementa()
        try:
            if not self._checkTypeBindings(ambiente):
                return False
            resolvidos = self._resolveTypeBindings(ambiente)
            self._includeTypeBindings(ambiente, resolvidos)
            return self._expressao.checaTipo(ambiente)
        finally:
            ambiente.restaura()

    def _includeTypeBindings(self, ambiente, resolvidos: Dict[Id, Tipo]) -> None:
        for id_, tipo in resolvidos.items():
            ambiente.map(id_, tipo)

    def _resolveTypeBindings(self, ambiente) -> Dict[Id, Tipo]:
        resolvidos: Dict[Id, Tipo] = {}
        for d in self._seqDecVariavel:
            if d.getID() in resolvidos:
                raise VariavelJaDeclaradaException(d.getID())
            resolvidos[d.getID()] = d.getExpressao().getTipo(ambiente)
        return resolvidos

    def _checkTypeBindings(self, ambiente) -> bool:
        for d in self._seqDecVariavel:
            if not d.getExpressao().checaTipo(ambiente):
                return False
        return True

    def getTipo(self, ambiente=None) -> Tipo:
        ambiente.incrementa()
        resolvidos = self._resolveTypeBindings(ambiente)
        self._includeTypeBindings(ambiente, resolvidos)
        resultado = self._expressao.getTipo(ambiente)
        ambiente.restaura()
        return resultado
