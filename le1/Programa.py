from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor


class Programa:
    def __init__(self, exp: Expressao):
        self._exp = exp

    def executar(self) -> Valor:
        resultado = self._exp.avaliar()
        print(resultado)
        return resultado

    def checaTipo(self) -> bool:
        return self._exp.checaTipo()

    def getExpressao(self) -> Expressao:
        return self._exp
