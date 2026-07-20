from li1.command.Comando import Comando


class Skip(Comando):
    def executar(self, ambiente):
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return True
