class ErroTipoEntradaException(Exception):
    def __init__(self, msg: str = "Tipo do valor de entrada lido incompativel"):
        super().__init__(msg)
