from le2.memory.Contexto import Contexto
from li1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.memory.ListaValor import ListaValor
from li2.memory.AmbienteExecucaoImperativa2 import AmbienteExecucaoImperativa2
from li2.memory.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from li2.memory.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class ContextoExecucaoImperativa2(ContextoExecucaoImperativa, AmbienteExecucaoImperativa2):
    """Alem da pilha de variaveis (herdada), mantem uma pilha paralela que
    guarda apenas procedimentos, sincronizada em incrementa/restaura."""

    def __init__(self, entrada: ListaValor):
        super().__init__(entrada)
        self._contextoProcedimentos: Contexto = Contexto()

    def incrementa(self) -> None:
        super().incrementa()
        self._contextoProcedimentos.incrementa()

    def restaura(self) -> None:
        super().restaura()
        self._contextoProcedimentos.restaura()

    def mapProcedimento(self, idArg, procedimentoId) -> None:
        try:
            self._contextoProcedimentos.map(idArg, procedimentoId)
        except Exception:
            raise ProcedimentoJaDeclaradoException(idArg)

    def getProcedimento(self, idArg):
        try:
            return self._contextoProcedimentos.get(idArg)
        except Exception:
            raise ProcedimentoNaoDeclaradoException(idArg)
