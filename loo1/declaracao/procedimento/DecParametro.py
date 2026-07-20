class DecParametro:
    def __init__(self, id_, tipo):
        self._id = id_
        self._tipo = tipo

    def getId(self):
        return self._id

    def getTipo(self):
        return self._tipo

    def elabora(self, ambiente):
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self._tipo.eValido(ambiente)

    def declaraParametro(self, ambiente):
        ambiente.map(self._id, self._tipo)
        return ambiente
