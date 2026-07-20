class VariavelNaoDeclaradaException(Exception):
    """Nao usada em tempo de execucao -- ver VariavelJaDeclaradaException."""

    def __init__(self, id_):
        super().__init__(f"Variavel {id_} nao declarada.")
