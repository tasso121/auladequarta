from li1.command.Comando import Comando
from li1.expression.Expressao import Expressao
from li1.expression.ValorBooleano import ValorBooleano


class While(Comando):
    def __init__(self, expressao: Expressao, comando: Comando):
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente):
        while True:
            condicao: ValorBooleano = self._expressao.avaliar(ambiente)
            if not condicao.valor():
                break
            ambiente = self._comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando.checaTipo(ambiente)
        )
