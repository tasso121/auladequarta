from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le1.expression.ValorBooleano import ValorBooleano
from le1.util.Tipo import Tipo


class IfThenElse(Expressao):
    """if (condicao) then (then) else (elseExpressao), como expressao."""

    def __init__(self, teste: Expressao, thenExpressao: Expressao, elseExpressao: Expressao):
        self._condicao = teste
        self._then = thenExpressao
        self._elseExpressao = elseExpressao

    def __str__(self) -> str:
        return f"if ({self._condicao}) then ({self._then}) else ({self._elseExpressao})"

    def avaliar(self, ambiente=None) -> Valor:
        condicao: ValorBooleano = self._condicao.avaliar(ambiente)
        if condicao.valor():
            return self._then.avaliar(ambiente)
        return self._elseExpressao.avaliar(ambiente)

    def checaTipo(self, ambiente=None) -> bool:
        if not self._condicao.getTipo(ambiente).eBooleano():
            return False
        if self._then.getTipo(ambiente).intersecao(self._elseExpressao.getTipo(ambiente)).eVoid():
            return False
        return True

    def getTipo(self, ambiente=None) -> Tipo:
        return self._then.getTipo(ambiente).intersecao(self._elseExpressao.getTipo(ambiente))

    def getCondicao(self) -> Expressao:
        return self._condicao

    def getThen(self) -> Expressao:
        return self._then

    def getElseExpressao(self) -> Expressao:
        return self._elseExpressao
