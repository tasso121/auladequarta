from li1.command.IO import IO
from li1.expression.Expressao import Expressao


class SWrite(IO):
    def __init__(self, expressao: Expressao):
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.write(self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self._expressao.checaTipo(ambiente)
