from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class ProcedimentoNaoDeclaradoException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_):
        super().__init__(f"Procedimento {id_} nao declarado.")
