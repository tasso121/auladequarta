class ObjetoJaDeclaradoException(Exception):
    def __init__(self, id_):
        super().__init__(f"Objeto {id_} ja declarado.")
