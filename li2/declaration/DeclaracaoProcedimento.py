from li1.declaration.Declaracao import Declaracao
from li1.expression.Id import Id
from li2.declaration.DefProcedimento import DefProcedimento


class DeclaracaoProcedimento(Declaracao):
    def __init__(self, id_: Id, defProcedimento: DefProcedimento):
        self._id = id_
        self._defProcedimento = defProcedimento

    def elabora(self, ambiente):
        ambiente.mapProcedimento(self._id, self._defProcedimento)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        ambiente.map(self._id, self._defProcedimento.getTipo())

        parametrosFormais = self._defProcedimento.getParametrosFormais()
        if parametrosFormais.checaTipo(ambiente):
            ambiente.incrementa()
            ambiente = parametrosFormais.elabora(ambiente)
            resposta = self._defProcedimento.getComando().checaTipo(ambiente)
            ambiente.restaura()
        else:
            resposta = False
        return resposta
