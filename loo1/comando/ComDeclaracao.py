from loo1.comando.Comando import Comando


class ComDeclaracao(Comando):
    def __init__(self, declaracao, comando: Comando):
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self._comando.executar(self._declaracao.elabora(ambiente))
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        ambiente.incrementa()
        resposta = self._declaracao.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
        ambiente.restaura()
        return resposta
