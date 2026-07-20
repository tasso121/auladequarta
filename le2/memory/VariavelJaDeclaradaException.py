from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id_):
        super().__init__(f"Variavel {id_} ja declarada.")
