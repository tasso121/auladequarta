from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from li1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa
from li1.memory.ContextoExecucao import ContextoExecucao
from li1.memory.EntradaVaziaException import EntradaVaziaException
from li1.memory.ListaValor import ListaValor


class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):
    def __init__(self, entrada: ListaValor):
        super().__init__()
        self._entrada = entrada
        self._saida = ListaValor()

    def read(self):
        if self._entrada is None or self._entrada.getHead() is None:
            raise EntradaVaziaException()
        aux = self._entrada.getHead()
        self._entrada = self._entrada.getTail()
        return aux

    def getSaida(self) -> ListaValor:
        return self._saida

    def write(self, v) -> None:
        self._saida.write(v)

    def changeValor(self, idArg, valorId) -> None:
        for escopo in reversed(self.getPilha()):
            if idArg in escopo:
                escopo[idArg] = valorId
                return
        raise VariavelNaoDeclaradaException(idArg)
