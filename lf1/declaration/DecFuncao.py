from le1.expression.Expressao import Expressao
from le1.util.Tipo import Tipo
from le2.expression.Id import Id
from lf1.declaration.DeclaracaoFuncional import DeclaracaoFuncional
from lf1.util.ValorFuncao import ValorFuncao


class DecFuncao(DeclaracaoFuncional):
    def __init__(self, idFun: Id, valorFuncao: ValorFuncao):
        self._id = idFun
        self._valorFuncao = valorFuncao

    def __str__(self) -> str:
        params = ", ".join(str(i) for i in self._valorFuncao.getListaId())
        return f"fun {self._id} ({params}) = {self._valorFuncao.getExp()}"

    def getID(self) -> Id:
        return self._id

    def getExpressao(self) -> Expressao:
        return self._valorFuncao.getExp()

    def getFuncao(self) -> ValorFuncao:
        return self._valorFuncao

    def getAridade(self) -> int:
        return self._valorFuncao.getAridade()

    def _tipoDaFuncao(self) -> Tipo:
        tipo = Tipo()
        for _ in range(self.getAridade()):
            tipo = Tipo(prox=tipo)
        return tipo

    def checaTipo(self, ambiente=None) -> bool:
        ambiente.incrementa()
        ambiente.map(self._id, self._tipoDaFuncao())
        resultado = self._valorFuncao.checaTipo(ambiente)
        ambiente.restaura()
        return resultado

    def getTipo(self, ambiente=None) -> Tipo:
        ambiente.incrementa()
        ambiente.map(self._id, self._tipoDaFuncao())
        resultado = self._valorFuncao.getTipo(ambiente)
        ambiente.restaura()
        return resultado
