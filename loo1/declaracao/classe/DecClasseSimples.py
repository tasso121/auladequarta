from loo1.declaracao.classe.DecClasse import DecClasse
from loo1.expressao.leftExpression.Id import Id
from loo1.memoria.DefClasse import DefClasse
from loo1.util.TipoClasse import TipoClasse

_THIS = Id("this")


class DecClasseSimples(DecClasse):
    def __init__(self, nomeClasse: Id, atributos, metodos):
        self._nomeClasse = nomeClasse
        self._atributos = atributos
        self._metodos = metodos

    def checaTipo(self, ambiente) -> bool:
        ambiente.mapDefClasse(self._nomeClasse, DefClasse(self._nomeClasse, self._atributos, self._metodos))
        resposta = False
        ambiente.incrementa()
        if self._atributos.checaTipo(ambiente):
            ambiente.map(_THIS, TipoClasse(self._nomeClasse))
            resposta = self._metodos.checaTipo(ambiente)
        ambiente.restaura()
        return resposta

    def elabora(self, ambiente):
        ambiente.mapDefClasse(self._nomeClasse, DefClasse(self._nomeClasse, self._atributos, self._metodos))
        return ambiente
