from loo1.comando.Procedimento import Procedimento
from loo1.declaracao.procedimento.DecProcedimento import DecProcedimento
from loo1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class DecProcedimentoSimples(DecProcedimento):
    def __init__(self, nome, parametrosFormais, comando):
        self._nome = nome
        self._parametrosFormais = parametrosFormais
        self._comando = comando

    def getProcedimento(self, nome) -> Procedimento:
        if self._nome == nome:
            return Procedimento(self._parametrosFormais, self._comando)
        raise ProcedimentoNaoDeclaradoException(nome)

    def checaTipo(self, ambiente) -> bool:
        if self._parametrosFormais.checaTipo(ambiente):
            ambiente.mapParametrosProcedimento(self._nome, self._parametrosFormais)
            ambiente.incrementa()
            ambiente = self._parametrosFormais.declaraParametro(ambiente)
            resposta = self._comando.checaTipo(ambiente)
            ambiente.restaura()
        else:
            resposta = False
        return resposta
