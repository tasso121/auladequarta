from loo1.expressao.valor.ValorConcreto import ValorConcreto


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool):
        self._valor = valor

    def valor(self) -> bool:
        return self._valor

    def avaliar(self, ambiente=None) -> "ValorBooleano":
        return self

    def equals(self, obj) -> bool:
        return isinstance(obj, ValorBooleano) and self._valor == obj.valor()

    def __str__(self) -> str:
        return "true" if self._valor else "false"

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_BOOLEANO
