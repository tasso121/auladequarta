class EntradaInvalidaException(Exception):
    def __init__(self, mensagem: str = "A entrada fornecida nao pode ser atribuida a um identificador desse tipo!"):
        super().__init__(mensagem)
