from loo1.comando.IO import IO


class Write(IO):
    def __init__(self, expressao):
        self._expressao = expressao

    def executar(self, ambiente):
        valor = self._expressao.avaliar(ambiente)
        print(valor)
        return ambiente.write(valor)

    def checaTipo(self, ambiente) -> bool:
        return self._expressao.checaTipo(ambiente)
