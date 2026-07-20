from li1.command.Comando import Comando
from li1.memory.AmbienteCompilacaoImperativa import AmbienteCompilacaoImperativa
from li1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa
from li1.memory.ListaValor import ListaValor


class Programa:
    def __init__(self, comando: Comando):
        self._comando = comando

    def executar(self, ambienteExecucao: AmbienteExecucaoImperativa) -> ListaValor:
        ambienteExecucao = self._comando.executar(ambienteExecucao)
        return ambienteExecucao.getSaida()

    def checaTipo(self, ambienteCompilacao: AmbienteCompilacaoImperativa) -> bool:
        return self._comando.checaTipo(ambienteCompilacao)
