from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException
from loo1.excecao.execucao.EntradaInvalidaException import EntradaInvalidaException
from loo1.expressao.leftExpression.Id import Id
from loo1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.expressao.valor.ValorNull import ValorNull
from loo1.expressao.valor.ValorRef import ValorRef, VALOR_INICIAL
from loo1.expressao.valor.ValorString import ValorString
from loo1.memoria.colecao.ListaValor import ListaValor
from loo1.util.TipoPrimitivo import TipoPrimitivo

_THIS = Id("this")


class ContextoExecucaoOO1:
    """Tres formas de construcao, espelhando as tres do Java:

    - ``ContextoExecucaoOO1()`` / ``ContextoExecucaoOO1(entrada)``: raiz do
      programa -- pilha, mapa de objetos, mapa de classes e proxRef todos
      novos.
    - ``ContextoExecucaoOO1(ambiente)``: ambiente auxiliar usado por New/
      ChamadaMetodo -- COMPARTILHA (mesma referencia de dict/objeto, nao
      copia) mapObjetos, mapDefClasse, entrada, saida e o contador proxRef
      com quem criou, mas comeca com uma pilha propria e vazia contendo
      apenas {"this": ValorNull()}. E essa referencia compartilhada de dict
      (equivalente ao HashMap do Java sendo passado por referencia) que
      unifica todos os objetos/classes num unico heap, sem precisar de
      nenhuma logica extra de delegacao.
    """

    def __init__(self, entrada_ou_ambiente=None):
        if entrada_ou_ambiente is None or isinstance(entrada_ou_ambiente, ListaValor):
            self._pilha = []
            self._mapObjetos = {}
            self._mapDefClasse = {}
            self._entrada = entrada_ou_ambiente
            self._saida = ListaValor()
            self._proxRef = None
        else:
            ambiente = entrada_ou_ambiente
            self._proxRef = ambiente.getRef()
            self._mapObjetos = ambiente.getMapObjetos()
            self._mapDefClasse = ambiente.getMapDefClasse()
            self._entrada = ambiente.getEntrada()
            self._saida = ambiente.getSaida()
            self._pilha = [{_THIS: ValorNull()}]

    def getPilha(self):
        return self._pilha

    def setPilha(self, pilha) -> None:
        self._pilha = pilha

    def setSaida(self, saida) -> None:
        self._saida = saida

    def getMapDefClasse(self) -> dict:
        return self._mapDefClasse

    def getMapObjetos(self) -> dict:
        return self._mapObjetos

    def read(self, tipoIdLido):
        valorLido = self._leEntrada()
        if valorLido is not None:
            valorLido = valorLido.strip()
            if isinstance(tipoIdLido, TipoPrimitivo):
                try:
                    if tipoIdLido.eBooleano():
                        return ValorBooleano(valorLido.strip().lower() == "true")
                    if tipoIdLido.eInteiro():
                        return ValorInteiro(int(valorLido))
                    if tipoIdLido.eString():
                        return ValorString(valorLido)
                except ValueError:
                    raise EntradaInvalidaException(
                        "O tipo da entrada e o da variavel a ser lida sao diferentes!"
                    )
        raise EntradaInvalidaException("O tipo da variavel a ser lida nao e um tipo Primitivo!")

    def _leEntrada(self):
        if self._entrada is None:
            return input()
        if self._entrada.length() == 0:
            raise EntradaInvalidaException("Numero de argumentos menor do que o numero de reads!")
        retorno = str(self._entrada.getHead())
        self._entrada = self._entrada.getTail()
        return retorno

    def getSaida(self) -> ListaValor:
        return self._saida

    def getEntrada(self):
        return self._entrada

    def write(self, v):
        self._saida.write(v)
        return self

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        self._pilha.pop()

    def map(self, idArg, valorId) -> None:
        topo = self._pilha[-1]
        if idArg in topo:
            raise VariavelJaDeclaradaException(idArg)
        topo[idArg] = valorId

    def mapDefClasse(self, idArg, defClasse) -> None:
        if idArg in self._mapDefClasse:
            raise ClasseJaDeclaradaException(idArg)
        self._mapDefClasse[idArg] = defClasse

    def mapObjeto(self, valorRef, objeto) -> None:
        if valorRef in self._mapObjetos:
            raise ObjetoJaDeclaradoException(objeto.getClasse())
        self._mapObjetos[valorRef] = objeto

    def changeValor(self, idArg, valorId) -> None:
        for escopo in reversed(self._pilha):
            if idArg in escopo:
                escopo[idArg] = valorId
                return
        raise VariavelNaoDeclaradaException(idArg)

    def get(self, idArg):
        for escopo in reversed(self._pilha):
            if idArg in escopo:
                return escopo[idArg]
        raise VariavelNaoDeclaradaException(idArg)

    def getValor(self, idArg):
        return self.get(idArg)

    def getDefClasse(self, idArg):
        return self._mapDefClasse.get(idArg)

    def getObjeto(self, valorRef):
        result = self._mapObjetos.get(valorRef)
        if result is None:
            raise ObjetoNaoDeclaradoException(Id(str(valorRef)))
        return result

    def getProxRef(self) -> ValorRef:
        aux = ValorRef(self._proxRef.valor())
        self._proxRef = self._proxRef.incrementa()
        return aux

    def getRef(self) -> ValorRef:
        if self._proxRef is None:
            self._proxRef = ValorRef(VALOR_INICIAL)
        return self._proxRef

    def getContextoIdValor(self) -> "ContextoExecucaoOO1":
        ambiente = ContextoExecucaoOO1(self.getEntrada())
        ambiente._pilha = self._pilha
        ambiente._saida = self._saida
        return ambiente
