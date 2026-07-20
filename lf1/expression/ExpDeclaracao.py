from typing import Dict, List

from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.util.Tipo import Tipo
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from lf1.declaration.DeclaracaoFuncional import DeclaracaoFuncional


class ExpDeclaracao(Expressao):
    """let (var|fun) d1, d2, ... in expressao -- versao funcional, aceita
    tanto variaveis quanto funcoes na lista de declaracoes."""

    def __init__(self, declaracoesFuncionais: List[DeclaracaoFuncional], expressao: Expressao):
        self._seqDecFuncional = declaracoesFuncionais
        self._expressao = expressao

    def __str__(self) -> str:
        return f"let {self._seqDecFuncional}\nin\n{self._expressao}"

    def avaliar(self, ambiente=None) -> Valor:
        ambiente.incrementa()
        auxIdValor: Dict[Id, Valor] = {}
        auxIdValorFuncao: Dict = {}
        self._resolveBindings(ambiente, auxIdValor, auxIdValorFuncao)
        self._includeBindings(ambiente, auxIdValor, auxIdValorFuncao)
        resultado = self._expressao.avaliar(ambiente)
        ambiente.restaura()
        return resultado

    def _includeBindings(self, ambiente, auxIdValor, auxIdValorFuncao) -> None:
        for id_, valor in auxIdValor.items():
            ambiente.map(id_, valor)
        for id_, valorFuncao in auxIdValorFuncao.items():
            ambiente.mapFuncao(id_, valorFuncao)

    def _resolveBindings(self, ambiente, auxIdValor, auxIdValorFuncao) -> None:
        for decFuncional in self._seqDecFuncional:
            if decFuncional.getAridade() == 0:
                auxIdValor[decFuncional.getID()] = decFuncional.getExpressao().avaliar(ambiente)
            else:
                auxIdValorFuncao[decFuncional.getID()] = decFuncional.getFuncao()

    def checaTipo(self, ambiente=None) -> bool:
        ambiente.incrementa()
        try:
            result = self._checkTypeBindings(ambiente)
            if result:
                resolvidos = self._resolveTypeBindings(ambiente)
                self._includeTypeBindings(ambiente, resolvidos)
                result = self._expressao.checaTipo(ambiente)
            return result
        finally:
            ambiente.restaura()

    def _resolveTypeBindings(self, ambiente) -> Dict[Id, Tipo]:
        resolvidos: Dict[Id, Tipo] = {}
        for decFuncional in self._seqDecFuncional:
            if decFuncional.getID() in resolvidos:
                raise VariavelJaDeclaradaException(decFuncional.getID())
            resolvidos[decFuncional.getID()] = decFuncional.getTipo(ambiente)
        return resolvidos

    def _checkTypeBindings(self, ambiente) -> bool:
        result = True
        for decFuncional in self._seqDecFuncional:
            if not decFuncional.checaTipo(ambiente):
                result = False
        return result

    def _includeTypeBindings(self, ambiente, resolvidos: Dict[Id, Tipo]) -> None:
        for id_, tipo in resolvidos.items():
            ambiente.map(id_, tipo)

    def getTipo(self, ambiente=None) -> Tipo:
        ambiente.incrementa()
        for decFuncional in self._seqDecFuncional:
            if decFuncional.getAridade() == 0:
                ambiente.map(decFuncional.getID(), decFuncional.getExpressao().getTipo(ambiente))
            else:
                tipo = decFuncional.getFuncao().getTipo(ambiente)
                if tipo is not Tipo.TIPO_INDEFINIDO:
                    ambiente.map(decFuncional.getID(), tipo)
        resultado = self._expressao.getTipo(ambiente)
        ambiente.restaura()
        return resultado

    def getSeqdecFuncional(self) -> List[DeclaracaoFuncional]:
        return self._seqDecFuncional

    def getExpressao(self) -> Expressao:
        return self._expressao
