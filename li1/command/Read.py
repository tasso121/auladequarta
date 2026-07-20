from li1.command.IO import IO
from li1.expression.Id import Id
from li1.memory.ErroTipoEntradaException import ErroTipoEntradaException


class Read(IO):
    def __init__(self, id_: Id):
        self._id = id_

    def executar(self, ambiente):
        valorID = ambiente.get(self._id)
        valorRead = ambiente.read()
        if valorID.getTipo(None).eIgual(valorRead.getTipo(None)):
            ambiente.changeValor(self._id, valorRead)
        else:
            raise ErroTipoEntradaException(
                f"Tipo do valor de entrada lido incompativel com tipo da variavel ({self._id.getIdName()})"
            )
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        return True
