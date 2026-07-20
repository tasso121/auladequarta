class Procedimento:
    def __init__(self, parametrosFormais, comando):
        self._parametrosFormais = parametrosFormais
        self._comando = comando

    def getParametrosFormais(self):
        return self._parametrosFormais

    def getComando(self):
        return self._comando
