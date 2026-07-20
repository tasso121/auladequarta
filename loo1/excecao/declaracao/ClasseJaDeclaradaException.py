class ClasseJaDeclaradaException(Exception):
    def __init__(self, id_):
        super().__init__(f"Classe {id_} ja declarada.")
