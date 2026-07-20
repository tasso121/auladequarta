from typing import List

from li1.util.Tipo import Tipo


class TipoProcedimento(Tipo):
    """Tipo de um procedimento: a lista (ordenada) dos tipos de seus
    parametros formais. Dois TipoProcedimento sao iguais se as listas de
    tipos dos parametros forem iguais, na ordem."""

    def __init__(self, tiposParametrosFormais: List[Tipo]):
        self.tiposParametrosFormais: List[Tipo] = list(tiposParametrosFormais)

    def eBooleano(self) -> bool:
        return False

    def eInteiro(self) -> bool:
        return False

    def eString(self) -> bool:
        return False

    def eValido(self) -> bool:
        resultado = True
        for tipo in self.tiposParametrosFormais:
            resultado = resultado and tipo.eValido()
        return resultado

    def eIgual(self, tipo: Tipo) -> bool:
        if isinstance(tipo, TipoProcedimento):
            return tipo.tiposParametrosFormais == self.tiposParametrosFormais
        return tipo.eIgual(self)

    def getNome(self) -> str:
        partes = ", ".join(str(t) for t in self.tiposParametrosFormais)
        return "{" + partes + "}"

    def intersecao(self, outroTipo: Tipo):
        if outroTipo.eIgual(self):
            return self
        return None

    def __str__(self) -> str:
        return self.getNome()
