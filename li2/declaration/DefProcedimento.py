from li1.command.Comando import Comando
from li2.declaration.ListaDeclaracaoParametro import ListaDeclaracaoParametro


class DefProcedimento:
    """Uma definicao de procedimento associa uma lista de parametros formais
    a um comando (o corpo do procedimento)."""

    def __init__(self, parametrosFormais: ListaDeclaracaoParametro, comando: Comando):
        self._parametrosFormais = parametrosFormais
        self._comando = comando

    def getComando(self) -> Comando:
        return self._comando

    def getParametrosFormais(self) -> ListaDeclaracaoParametro:
        return self._parametrosFormais

    def getTipo(self):
        from li2.util.TipoProcedimento import TipoProcedimento

        return TipoProcedimento(self._parametrosFormais.getTipos())
