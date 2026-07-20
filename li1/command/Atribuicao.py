from li1.command.Comando import Comando
from li1.expression.Expressao import Expressao
from li1.expression.Id import Id


class Atribuicao(Comando):
    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.changeValor(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return self._expressao.checaTipo(ambiente) and self._id.getTipo(ambiente).eIgual(
            self._expressao.getTipo(ambiente)
        )
