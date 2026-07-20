from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class ProcedimentoJaDeclaradoException(IdentificadorJaDeclaradoException):
    def __init__(self, id_):
        super().__init__(f"Procedimento {id_} ja declarado.")
