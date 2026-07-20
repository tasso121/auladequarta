from li1.command.Comando import Comando
from li1.declaration.Declaracao import Declaracao


class ComandoDeclaracao(Comando):
    def __init__(self, declaracao: Declaracao, comando: Comando):
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente):
        ambiente.incrementa()
        ambiente = self._comando.executar(self._declaracao.elabora(ambiente))
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        ambiente.incrementa()
        resultado = self._declaracao.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
        ambiente.restaura()
        return resultado
