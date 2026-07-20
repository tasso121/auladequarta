from le2.expression.Id import Id as _Id2Id
from loo1.expressao.leftExpression.LeftExpression import LeftExpression


class Id(_Id2Id, LeftExpression):
    """Reaproveita avaliar/checaTipo/getTipo de le2.expression.Id (todos
    delegam a ambiente.get(self), que funciona identicamente nos ambientes
    de execucao/compilacao de loo1)."""

    def getId(self) -> "Id":
        return self
