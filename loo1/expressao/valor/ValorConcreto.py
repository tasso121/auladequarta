from abc import abstractmethod

from loo1.expressao.valor.Valor import Valor


class ValorConcreto(Valor):
    """Valores cuja igualdade e definida pelo conteudo armazenado (em vez de
    identidade). ValorRef deliberadamente NAO implementa esta interface --
    ver ExpEquals."""

    @abstractmethod
    def equals(self, valor: "ValorConcreto") -> bool:
        raise NotImplementedError
