from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id_):
        super().__init__(f"Variavel {id_} nao declarada.")
