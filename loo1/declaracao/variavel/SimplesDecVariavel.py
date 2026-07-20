from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.util.TipoClasse import TipoClasse


class SimplesDecVariavel(DecVariavel):
    def __init__(self, tipo, id_, expressao):
        self._tipo = tipo
        self._id = id_
        self._expressao = expressao

    def getTipo(self, id_):
        if self._id == id_:
            return self._tipo
        raise VariavelNaoDeclaradaException(id_)

    def elabora(self, ambiente):
        ambiente.map(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        resposta = False
        if self._expressao.checaTipo(ambiente):
            if isinstance(self._tipo, TipoClasse):
                resposta = self._expressao.getTipo(ambiente).equals(
                    TipoClasse.TIPO_NULL
                ) or self._expressao.getTipo(ambiente).equals(self._tipo)
            else:
                resposta = self._expressao.getTipo(ambiente).equals(self._tipo)
        if resposta:
            ambiente.map(self._id, self._tipo)
        return resposta
