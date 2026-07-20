from le1.expression.Expressao import Expressao
from le2.expression.Id import Id


class DecVariavel:
    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def getID(self) -> Id:
        return self._id

    def getExpressao(self) -> Expressao:
        return self._expressao
