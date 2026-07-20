from li1.expression.Id import Id
from li1.util.Tipo import Tipo


class DeclaracaoParametro:
    def __init__(self, id_: Id, tipo: Tipo):
        self._id = id_
        self._tipo = tipo

    def getId(self) -> Id:
        return self._id

    def getTipo(self) -> Tipo:
        return self._tipo

    def checaTipo(self, ambiente) -> bool:
        return self._tipo.eValido()

    def elabora(self, ambiente):
        ambiente.map(self._id, self._tipo)
        return ambiente
