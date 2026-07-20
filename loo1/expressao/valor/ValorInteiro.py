from loo1.expressao.valor.ValorConcreto import ValorConcreto


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int):
        self._valor = valor

    def valor(self) -> int:
        return self._valor

    def avaliar(self, ambiente=None) -> "ValorInteiro":
        return self

    def equals(self, obj) -> bool:
        return isinstance(obj, ValorInteiro) and self._valor == obj.valor()

    def __str__(self) -> str:
        return str(self._valor)

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_INTEIRO
