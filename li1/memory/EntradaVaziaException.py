class EntradaVaziaException(Exception):
    def __init__(self):
        super().__init__("Entrada vazia.")
