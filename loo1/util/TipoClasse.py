from loo1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.expressao.leftExpression.Id import Id
from loo1.util.Tipo import Tipo


class TipoClasse(Tipo):
    NULL = Id("NULL")

    def __init__(self, tipoClasse: Id):
        self._tipoClasse = tipoClasse

    def getTipo(self) -> Id:
        return self._tipoClasse

    def eValido(self, ambiente=None) -> bool:
        if self._tipoClasse is TipoClasse.NULL:
            return True
        try:
            return ambiente.getDefClasse(self._tipoClasse) is not None
        except ClasseNaoDeclaradaException:
            return False

    def equals(self, obj) -> bool:
        return isinstance(obj, TipoClasse) and obj._tipoClasse == self._tipoClasse

    def __eq__(self, other) -> bool:
        return self.equals(other)

    def __hash__(self) -> int:
        return hash(("TipoClasse", self._tipoClasse))

    def __str__(self) -> str:
        return str(self._tipoClasse)


TipoClasse.TIPO_NULL = TipoClasse(TipoClasse.NULL)
