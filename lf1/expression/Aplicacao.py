from typing import Dict, List

from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.util.Tipo import Tipo
from le2.expression.Id import Id
from lf1.util.ValorFuncao import ValorFuncao


class Aplicacao(Expressao):
    """Aplicacao de uma funcao (por identificador) a uma lista de argumentos."""

    def __init__(self, func: Id, expressoes: List[Expressao]):
        self._func = func
        self._argsExpressao = expressoes

    def __str__(self) -> str:
        return f"{self._func} ({self._argsExpressao})"

    def avaliar(self, ambiente=None) -> Valor:
        funcao: ValorFuncao = ambiente.getFuncao(self._func)
        mapIdValor = self._resolveParametersBindings(ambiente, funcao)
        ambiente.incrementa()
        self._includeValueBindings(ambiente, mapIdValor)
        resultado = funcao.getExp().avaliar(ambiente)
        ambiente.restaura()
        return resultado

    def _includeValueBindings(self, ambiente, mapIdValor: Dict[Id, Valor]) -> None:
        for id_, valor in mapIdValor.items():
            ambiente.map(id_, valor)

    def _resolveParametersBindings(self, ambiente, funcao: ValorFuncao) -> Dict[Id, Valor]:
        mapIdValor: Dict[Id, Valor] = {}
        for id_, exp in zip(funcao.getListaId(), self._argsExpressao):
            mapIdValor[id_] = exp.avaliar(ambiente)
        return mapIdValor

    def checaTipo(self, ambiente=None) -> bool:
        tipoFuncao = ambiente.get(self._func)
        return self._checkArgumentListSize(tipoFuncao) and self._checkArgumentTypes(ambiente, tipoFuncao)

    def _checkArgumentTypes(self, ambiente, tipoFuncao: Tipo) -> bool:
        result = True
        for valorReal in self._argsExpressao:
            if not valorReal.checaTipo(ambiente):
                result = False
            tipoArg = valorReal.getTipo(ambiente)
            if tipoArg.intersecao(tipoFuncao).eVoid():
                result = False
            tipoFuncao = tipoFuncao.getProx()
        return result

    def _checkArgumentListSize(self, tipoFuncao: Tipo) -> bool:
        tamanhoTipo = 0
        aux = tipoFuncao
        while aux is not None:
            tamanhoTipo += 1
            aux = aux.getProx()
        return (tamanhoTipo - 1) == len(self._argsExpressao)

    def getTipo(self, ambiente=None) -> Tipo:
        t = ambiente.get(self._func)
        while t.getProx() is not None:
            t = t.getProx()
        return t

    def getFunc(self) -> Id:
        return self._func

    def getArgsExpressao(self) -> List[Expressao]:
        return self._argsExpressao
