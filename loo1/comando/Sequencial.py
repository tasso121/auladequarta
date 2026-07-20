from loo1.comando.Comando import Comando


class Sequencial(Comando):
    def __init__(self, comando1: Comando, comando2: Comando):
        self._comando1 = comando1
        self._comando2 = comando2

    def executar(self, ambiente):
        ambiente = self._comando1.executar(ambiente)
        ambiente = self._comando2.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self._comando1.checaTipo(ambiente) and self._comando2.checaTipo(ambiente)
