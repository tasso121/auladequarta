from le2.memory.Contexto import Contexto
from li1.memory.AmbienteExecucao import AmbienteExecucao


class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self) -> "ContextoExecucao":
        retorno = ContextoExecucao()
        achatado = {}
        for escopo in self.getPilha():
            achatado.update(escopo)
        retorno.setPilha([achatado])
        return retorno
