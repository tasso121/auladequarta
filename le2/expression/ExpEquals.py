from le1.expression.ExpEquals import ExpEquals as ExpEqualsLe1


class ExpEquals(ExpEqualsLe1):
    """Em le2 a checagem de igualdade e mais permissiva: basta que os tipos
    possiveis das subexpressoes tenham intersecao nao-vazia (relevante
    quando identificadores tem tipo ainda indefinido)."""

    def checaTipoElementoTerminal(self, ambiente=None) -> bool:
        return not self.getEsq().getTipo(ambiente).intersecao(self.getDir().getTipo(ambiente)).eVoid()
