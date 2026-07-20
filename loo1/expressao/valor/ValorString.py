from loo1.expressao.valor.ValorConcreto import ValorConcreto


class ValorString(ValorConcreto):
    def __init__(self, valor: str):
        self._valor = valor

    def valor(self) -> str:
        return self._valor

    def avaliar(self, ambiente=None) -> "ValorString":
        return self

    def equals(self, obj) -> bool:
        return isinstance(obj, ValorString) and self._valor == obj.valor()

    def __str__(self) -> str:
        return self._valor

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_STRING
