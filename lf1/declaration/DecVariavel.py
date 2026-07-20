from le1.expression.Expressao import Expressao
from le1.util.Tipo import Tipo
from le2.expression.Id import Id
from lf1.declaration.DeclaracaoFuncional import DeclaracaoFuncional


class DecVariavel(DeclaracaoFuncional):
    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def __str__(self) -> str:
        return f"var {self._id} = {self._expressao}"

    def getAridade(self) -> int:
        return 0

    def getExpressao(self) -> Expressao:
        return self._expressao

    def getID(self) -> Id:
        return self._id

    def getTipo(self, ambiente=None) -> Tipo:
        return self._expressao.getTipo(ambiente)

    def checaTipo(self, ambiente=None) -> bool:
        return self._expressao.checaTipo(ambiente)
