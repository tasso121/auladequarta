class EntradaNaoFornecidaException(Exception):
    def __init__(self):
        super().__init__("Forneca os valores de entrada do programa!")
