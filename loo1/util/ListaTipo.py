class ListaTipo:
    """Lista encadeada de Tipo (parametros reais/formais de um metodo)."""

    def __init__(self, tipo=None, listaTipo: "ListaTipo" = None):
        if tipo is None:
            self._tipo = None
            self._listaTipo = None
        elif listaTipo is None:
            self._tipo = tipo
            self._listaTipo = ListaTipo()
        else:
            self._tipo = tipo
            self._listaTipo = listaTipo

    def length(self) -> int:
        if self._listaTipo is None:
            return 0
        return 1 + self._listaTipo.length()

    def head(self):
        return self._tipo

    def tail(self) -> "ListaTipo":
        return self._listaTipo
