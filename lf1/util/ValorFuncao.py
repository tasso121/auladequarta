from typing import Dict, List

from le1.expression.Expressao import Expressao
from le1.util.Tipo import Tipo
from le2.expression.Id import Id


class ValorFuncao:
    """Representa o corpo + parametros formais de uma funcao declarada."""

    def __init__(self, argsId: List[Id], exp: Expressao):
        self._argsId = argsId
        self._exp = exp

    def getListaId(self) -> List[Id]:
        return self._argsId

    def getExp(self) -> Expressao:
        return self._exp

    def getAridade(self) -> int:
        return len(self._argsId)

    def checaTipo(self, ambiente=None) -> bool:
        ambiente.incrementa()
        t = self.getTipo(ambiente)
        for id_ in self._argsId:
            ambiente.map(id_, Tipo(t.get()))
            t = t.getProx()
        ambiente.restaura()
        return True

    def getTipo(self, ambiente=None) -> Tipo:
        from lf1.util.RestrictTypesVisitor import RestrictTypesVisitor

        idsArg = list(self._argsId)
        mapIdTipo: Dict[Id, Tipo] = {id_: Tipo() for id_ in idsArg}

        mapIdTipo = RestrictTypesVisitor.visit(self._exp, ambiente, mapIdTipo, Tipo())

        ambiente.incrementa()
        for id_, tipo in mapIdTipo.items():
            ambiente.map(id_, tipo)

        resultado = self._exp.getTipo(ambiente)
        for id_ in reversed(idsArg):
            resultado = Tipo(mapIdTipo[id_].get(), resultado)
        ambiente.restaura()
        return resultado
