from li1.declaration.Declaracao import Declaracao
from li1.expression.Expressao import Expressao
from li1.expression.Id import Id


class DeclaracaoVariavel(Declaracao):
    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def elabora(self, ambiente):
        ambiente.map(self.getId(), self.getExpressao().avaliar(ambiente))
        return ambiente

    def getExpressao(self) -> Expressao:
        return self._expressao

    def getId(self) -> Id:
        return self._id

    def checaTipo(self, ambiente) -> bool:
        resultado = self.getExpressao().checaTipo(ambiente)
        if resultado:
            ambiente.map(self.getId(), self.getExpressao().getTipo(ambiente))
        return resultado
