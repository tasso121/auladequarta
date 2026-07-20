from loo1.comando.Comando import Comando


class While(Comando):
    def __init__(self, expressao, comando: Comando):
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente):
        while self._expressao.avaliar(ambiente).valor():
            ambiente = self._comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando.checaTipo(ambiente)
        )
