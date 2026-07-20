class ContextoObjeto:
    """Estado (atributos) de um objeto: um mapeamento Id -> Valor plano,
    copiado uma vez a partir do escopo elaborado por New (nao compartilha
    dict com a pilha de execucao que o originou)."""

    def __init__(self, hash_: dict):
        self._estado = dict(hash_)

    def remove(self, id_) -> None:
        self._estado.pop(id_, None)

    def put(self, id_, valor) -> None:
        self._estado[id_] = valor

    def containsKey(self, idVariavel) -> bool:
        return idVariavel in self._estado

    def get(self, id_):
        return self._estado.get(id_)
