from loo1.expressao.leftExpression.Id import Id
from loo1.util.Tipo import Tipo


class TipoPrimitivo(Tipo):
    INTEIRO = 1
    BOOLEANO = 2
    STRING = 4

    TIPO_ID_int = Id("int")
    TIPO_ID_string = Id("string")
    TIPO_ID_boolean = Id("boolean")

    def __init__(self, tipo: int):
        self._tipo = tipo

    def getTipo(self) -> Id:
        if self._tipo == TipoPrimitivo.INTEIRO:
            return TipoPrimitivo.TIPO_ID_int
        if self._tipo == TipoPrimitivo.BOOLEANO:
            return TipoPrimitivo.TIPO_ID_boolean
        if self._tipo == TipoPrimitivo.STRING:
            return TipoPrimitivo.TIPO_ID_string
        return Id("undefined")

    def eInteiro(self) -> bool:
        return self._tipo == TipoPrimitivo.INTEIRO

    def eBooleano(self) -> bool:
        return self._tipo == TipoPrimitivo.BOOLEANO

    def eString(self) -> bool:
        return self._tipo == TipoPrimitivo.STRING

    def eValido(self, ambiente=None) -> bool:
        return self._tipo in (TipoPrimitivo.INTEIRO, TipoPrimitivo.BOOLEANO, TipoPrimitivo.STRING)

    def equals(self, obj) -> bool:
        return isinstance(obj, TipoPrimitivo) and obj._tipo == self._tipo

    def __eq__(self, other) -> bool:
        return self.equals(other)

    def __hash__(self) -> int:
        return hash(("TipoPrimitivo", self._tipo))

    def __str__(self) -> str:
        return {
            TipoPrimitivo.INTEIRO: "int",
            TipoPrimitivo.BOOLEANO: "boolean",
            TipoPrimitivo.STRING: "string",
        }.get(self._tipo, "undefined")


TipoPrimitivo.TIPO_INTEIRO = TipoPrimitivo(TipoPrimitivo.INTEIRO)
TipoPrimitivo.TIPO_BOOLEANO = TipoPrimitivo(TipoPrimitivo.BOOLEANO)
TipoPrimitivo.TIPO_STRING = TipoPrimitivo(TipoPrimitivo.STRING)
