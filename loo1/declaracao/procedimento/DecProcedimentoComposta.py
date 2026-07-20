from loo1.declaracao.procedimento.DecProcedimento import DecProcedimento
from loo1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class DecProcedimentoComposta(DecProcedimento):
    def __init__(self, declaracao1: DecProcedimento, declaracao2: DecProcedimento):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def getProcedimento(self, id_):
        try:
            return self._declaracao1.getProcedimento(id_)
        except ProcedimentoNaoDeclaradoException:
            return self._declaracao2.getProcedimento(id_)

    def checaTipo(self, ambiente) -> bool:
        return self._declaracao1.checaTipo(ambiente) and self._declaracao2.checaTipo(ambiente)
