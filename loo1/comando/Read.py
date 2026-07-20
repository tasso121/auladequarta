from loo1.comando.IO import IO


class Read(IO):
    def __init__(self, id_):
        self._id = id_
        self._tipoId = None

    def executar(self, ambiente):
        ambiente.changeValor(self._id, ambiente.read(self._tipoId))
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        # Alteramos a implementacao, pois em tempo de compilacao nao se pode
        # saber o tipo da entrada que sera lida (comentario original do Java).
        self._tipoId = self._id.getTipo(ambiente)
        return self._id.checaTipo(ambiente)
