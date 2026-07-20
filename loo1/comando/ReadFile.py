# pickle.load aqui e o analogo direto do ObjectInputStream.readObject() do
# Java original -- mesmo risco de execucao de codigo arbitrario se o arquivo
# vier de fonte nao confiavel. Aceitavel neste projeto academico: o arquivo
# lido e sempre gerado pelo proprio programa (equivalente ao WriteFile), nunca
# uma entrada externa/nao confiavel, e este comando nao e exercitado pelos
# Exemplo*.py (nenhum deles grava/le arquivos).
import pickle

from loo1.comando.IO import IO
from loo1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException


class ReadFile(IO):
    """Le uma lista de Objeto previamente serializada (pickle, equivalente
    ao ObjectInputStream do Java) e mapeia o objeto na posicao 'index' do
    arquivo 'dir' ao identificador 'id'. Nao exercitado pelos Exemplo*.py."""

    def __init__(self, id_, dir_, index):
        self._id = id_
        self._dir = dir_
        self._index = index
        self._tipoId = None

    def executar(self, ambiente):
        try:
            path = str(self._dir.avaliar(ambiente))
            objetos = []
            with open(path, "rb") as arquivo:
                while True:
                    try:
                        objetos.append(pickle.load(arquivo))
                    except EOFError:
                        break

            proxRef = ambiente.getProxRef()
            pos = int(str(self._index.avaliar(ambiente)))
            ambiente.mapObjeto(proxRef, objetos[pos])
            ambiente.changeValor(self._id, proxRef)
        except (ObjetoNaoDeclaradoException, ClasseNaoDeclaradaException, ObjetoJaDeclaradoException, OSError) as exc:
            print(exc)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        self._tipoId = self._id.getTipo(ambiente)
        return self._id.checaTipo(ambiente)
