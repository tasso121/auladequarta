class ProcedimentoJaDeclaradoException(Exception):
    def __init__(self, id_):
        super().__init__(f"Procedimento {id_} ja declarado.")
