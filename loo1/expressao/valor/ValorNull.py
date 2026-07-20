from loo1.expressao.valor.ValorConcreto import ValorConcreto


class ValorNull(ValorConcreto):
    def __str__(self) -> str:
        return "null"

    def equals(self, obj) -> bool:
        return isinstance(obj, ValorNull)

    def avaliar(self, ambiente=None) -> "ValorNull":
        return self

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def getTipo(self, ambiente=None):
        from loo1.util.TipoClasse import TipoClasse

        return TipoClasse.TIPO_NULL
