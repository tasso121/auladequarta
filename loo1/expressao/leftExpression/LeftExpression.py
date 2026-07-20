from abc import abstractmethod

from loo1.expressao.Expressao import Expressao


class LeftExpression(Expressao):
    """Expressao que pode ficar do lado esquerdo de uma atribuicao ou antes
    de uma chamada de metodo (Id ou AcessoAtributo)."""

    @abstractmethod
    def getId(self):
        raise NotImplementedError
