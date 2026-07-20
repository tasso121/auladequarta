from loo1.expressao.Expressao import Expressao
from loo1.expressao.leftExpression.Id import Id

_THIS = Id("this")


class This(Expressao):
    """Expressao do token 'this' -- sempre bem tipada, ja que so existe
    dentro do corpo de um metodo, onde 'this' esta sempre mapeado."""

    def avaliar(self, ambiente=None):
        return ambiente.get(_THIS)

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def getTipo(self, ambiente=None):
        return ambiente.get(_THIS)
