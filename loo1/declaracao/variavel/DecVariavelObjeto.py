from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.comando.New import New
from loo1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.expressao.valor.ValorNull import ValorNull
from loo1.util.TipoClasse import TipoClasse


class DecVariavelObjeto(DecVariavel):
    """Tipo Id ':=' 'new' Id -- declara uma variavel do tipo de uma classe
    e ja cria uma instancia dela."""

    def __init__(self, tipo, objeto, classe):
        self._tipo = tipo
        self._objeto = objeto
        self._classe = classe

    def getTipo(self, id_=None):
        if id_ is None:
            return self._tipo
        if self._objeto == id_:
            return self._tipo
        raise VariavelNaoDeclaradaException(id_)

    def elabora(self, ambiente):
        aux = SimplesDecVariavel(self._tipo, self._objeto, ValorNull()).elabora(ambiente)
        aux = New(self._objeto, self._classe).executar(aux)
        return aux

    def checaTipo(self, ambiente) -> bool:
        resposta = False
        tpClasse = TipoClasse(self._classe)
        if tpClasse.eValido(ambiente) and self._tipo.eValido(ambiente):
            resposta = tpClasse.equals(self._tipo)
            ambiente.map(self._objeto, tpClasse)
        return resposta

    def getObjeto(self):
        return self._objeto

    def getClasse(self):
        return self._classe
