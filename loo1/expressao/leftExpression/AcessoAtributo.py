from abc import abstractmethod

from loo1.expressao.leftExpression.LeftExpression import LeftExpression


class AcessoAtributo(LeftExpression):
    def __init__(self, id_):
        self._id = id_

    def getId(self):
        return self._id

    @abstractmethod
    def getExpressaoObjeto(self):
        raise NotImplementedError
