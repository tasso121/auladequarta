class DefClasse:
    """Definicao de uma classe: declaracao de atributos e de metodos (ambas
    podem ser simples ou compostas, encadeadas pela mesma logica recursiva).

    Sem memoizacao: uma chamada (ChamadaMetodo/ChamadaProcedimento.checaTipo)
    so compara a assinatura (aridade e tipos dos parametros reais x formais),
    nunca reverifica o corpo do metodo -- o corpo e checado uma unica vez,
    diretamente por DecProcedimentoSimples.checaTipo quando a classe e
    declarada. E por isso que metodos recursivos (this.prox.insere(v)) nao
    causam recursao infinita em tempo de compilacao."""

    def __init__(self, idClasse, decVariavel, decProcedimento):
        self._idClasse = idClasse
        self._decVariavel = decVariavel
        self._decProcedimento = decProcedimento

    def getDecVariavel(self):
        return self._decVariavel

    def getMetodo(self, idMetodo):
        return self._decProcedimento.getProcedimento(idMetodo)

    def getTipoAtributo(self, idAtributo):
        return self._decVariavel.getTipo(idAtributo)

    def getIdClasse(self):
        return self._idClasse
