from le1.expression.Expressao import Expressao
from le1.expression.Valor import Valor
from le2.memory.ContextoCompilacao import ContextoCompilacao
from le2.memory.ContextoExecucao import ContextoExecucao


class Programa:
    def __init__(self, exp: Expressao):
        self._exp = exp

    def executar(self) -> Valor:
        ambExec = ContextoExecucao()
        return self._exp.avaliar(ambExec)

    def checaTipo(self) -> bool:
        ambComp = ContextoCompilacao()
        return self._exp.checaTipo(ambComp)

    def getExpressao(self) -> Expressao:
        return self._exp
