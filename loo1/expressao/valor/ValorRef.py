from loo1.expressao.valor.Valor import Valor

VALOR_INICIAL = 0


class ValorRef(Valor):
    """Referencia a um objeto no heap. Deliberadamente NAO implementa
    ValorConcreto: em ExpEquals, comparar uma referencia de objeto com
    ValorNull cai no ramo de igualdade por identidade (sempre falso entre
    instancias distintas), que e exatamente o que 'this.prox == null' deve
    fazer depois que 'prox' passa a apontar para um objeto real -- replica
    fielmente o comportamento do ValorRef.java original (que so sobrescreve
    hashCode(), nunca equals(Object))."""

    VALOR_INICIAL = VALOR_INICIAL

    def __init__(self, valor: int):
        self._valor = valor if valor >= VALOR_INICIAL else VALOR_INICIAL

    def valor(self) -> int:
        return self._valor

    def avaliar(self, ambiente=None) -> "ValorRef":
        return self

    def getTipo(self, ambiente=None):
        from loo1.util.TipoPrimitivo import TipoPrimitivo

        return TipoPrimitivo.TIPO_INTEIRO

    def checaTipo(self, ambiente=None) -> bool:
        return True

    def equals(self, val) -> bool:
        return isinstance(val, ValorRef) and self._valor == val.valor()

    def incrementa(self) -> "ValorRef":
        self._valor += 1
        return self

    def __str__(self) -> str:
        return str(self._valor)
