from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class Objeto:
    def __init__(self, classeObjeto, estadoObj):
        self._classeObjeto = classeObjeto
        self._estado = estadoObj

    def getClasse(self):
        return self._classeObjeto

    def getEstado(self):
        return self._estado

    def setEstado(self, novoEstado) -> None:
        self._estado = novoEstado

    def mapThis(self, vr) -> None:
        from loo1.expressao.leftExpression.Id import Id

        id_ = Id("this")
        self._estado.remove(id_)
        self._estado.put(id_, vr)

    def changeAtributo(self, idVariavel, valor) -> None:
        if self._estado.containsKey(idVariavel):
            self._estado.remove(idVariavel)
            self._estado.put(idVariavel, valor)
        else:
            raise VariavelNaoDeclaradaException(idVariavel)
