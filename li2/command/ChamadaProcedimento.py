from li1.command.Comando import Comando
from li1.expression.Id import Id
from li2.command.ListaExpressao import ListaExpressao
from li2.util.TipoProcedimento import TipoProcedimento


class ChamadaProcedimento(Comando):
    def __init__(self, nomeProcedimento: Id, parametrosReais: ListaExpressao):
        self._nomeProcedimento = nomeProcedimento
        self._parametrosReais = parametrosReais

    def executar(self, ambiente):
        procedimento = ambiente.getProcedimento(self._nomeProcedimento)

        # o incrementa e o restaura neste ponto servem para criar as
        # variaveis que serao utilizadas pela execucao do procedimento
        ambiente.incrementa()
        parametrosFormais = procedimento.getParametrosFormais()
        aux = self._bindParameters(ambiente, parametrosFormais)
        aux = procedimento.getComando().executar(aux)
        aux.restaura()
        return aux

    def _bindParameters(self, ambiente, parametrosFormais):
        """Insere no contexto o resultado da associacao entre cada
        parametro formal e seu correspondente parametro atual."""
        listaValor = self._parametrosReais.avaliar(ambiente)
        while listaValor.length() > 0:
            ambiente.map(parametrosFormais.getHead().getId(), listaValor.getHead())
            parametrosFormais = parametrosFormais.getTail()
            listaValor = listaValor.getTail()
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        tipoProcedimento = ambiente.get(self._nomeProcedimento)
        tipoParametrosReais = TipoProcedimento(self._parametrosReais.getTipos(ambiente))
        return tipoProcedimento.eIgual(tipoParametrosReais)
