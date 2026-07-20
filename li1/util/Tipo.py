class Tipo:
    """Interface (informal) para os tipos primitivos da linguagem imperativa.
    Nao usa ABC porque a implementacao concreta (TipoPrimitivo) precisa ser
    tambem um Enum, e Enum + ABCMeta colidem em metaclasse."""

    def getNome(self) -> str:
        raise NotImplementedError

    def eInteiro(self) -> bool:
        raise NotImplementedError

    def eBooleano(self) -> bool:
        raise NotImplementedError

    def eString(self) -> bool:
        raise NotImplementedError

    def eIgual(self, tipo: "Tipo") -> bool:
        raise NotImplementedError

    def eValido(self) -> bool:
        raise NotImplementedError

    def intersecao(self, outroTipo: "Tipo"):
        raise NotImplementedError
