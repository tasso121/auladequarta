from loo1.excecao.execucao.EntradaNaoFornecidaException import EntradaNaoFornecidaException


class Programa:
    def __init__(self, decClasse, comando):
        self._decClasse = decClasse
        self._comando = comando

    def executar(self, ambiente):
        if ambiente is None:
            raise EntradaNaoFornecidaException()
        ambiente = self._comando.executar(self._decClasse.elabora(ambiente))
        return ambiente.getSaida()

    def checaTipo(self, ambiente) -> bool:
        if ambiente is None:
            raise EntradaNaoFornecidaException()
        return self._decClasse.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
