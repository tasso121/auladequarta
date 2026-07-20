from loo1.comando.Comando import Comando


class ChamadaProcedimento(Comando):
    def __init__(self, procedimento, parametrosReais, valoresParametros=None):
        self._procedimento = procedimento
        self._parametrosReais = parametrosReais
        self._valoresParametros = valoresParametros

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self._bindParameters(ambiente, self._procedimento.getParametrosFormais())
        ambiente = self._procedimento.getComando().executar(ambiente)
        ambiente.restaura()
        return ambiente

    def _bindParameters(self, ambiente, parametrosFormais):
        listaValor = self._valoresParametros
        if listaValor is None:
            listaValor = self._parametrosReais.avaliar(ambiente)
        while listaValor.length() > 0:
            ambiente.map(parametrosFormais.getHead().getId(), listaValor.getHead())
            parametrosFormais = parametrosFormais.getTail()
            listaValor = listaValor.getTail()
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        ambiente.incrementa()
        parametrosFormais = self._procedimento.getParametrosFormais()
        listaTipo = self._parametrosReais.getTipos(ambiente)
        if listaTipo.length() == parametrosFormais.length():
            if listaTipo.head() is None or parametrosFormais.getHead() is None:
                resposta = True
            else:
                resposta = True
                while listaTipo is not None and parametrosFormais is not None:
                    if not listaTipo.head().equals(parametrosFormais.getHead().getTipo()):
                        resposta = False
                        break
                    listaTipo = listaTipo.tail()
                    parametrosFormais = parametrosFormais.getTail()
        else:
            resposta = False
        ambiente.restaura()
        return resposta
