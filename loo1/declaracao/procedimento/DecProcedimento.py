from abc import ABC, abstractmethod


class DecProcedimento(ABC):
    """Nao estende Declaracao -- metodos nao sao "elaborados" no ambiente de
    execucao (nao ha mapProcedimento); DefClasse apenas guarda a AST e
    getMetodo/getProcedimento faz um lookup direto por nome quando chamado."""

    @abstractmethod
    def getProcedimento(self, nomeProcedimento):
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente) -> bool:
        raise NotImplementedError
