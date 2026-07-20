from le1.expression.Valor import Valor
from le2.memory.AmbienteExecucao import AmbienteExecucao
from le2.memory.Contexto import Contexto


class ContextoExecucao(Contexto[Valor], AmbienteExecucao):
    def clone(self) -> "ContextoExecucao":
        retorno = ContextoExecucao()
        achatado = {}
        for escopo in self.getPilha():
            achatado.update(escopo)
        retorno.setPilha([achatado])
        return retorno
