from li1.declaration.Declaracao import Declaracao


class DeclaracaoComposta(Declaracao):
    def __init__(self, declaracao1: Declaracao, declaracao2: Declaracao):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def elabora(self, ambiente):
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente) -> bool:
        return self._declaracao1.checaTipo(ambiente) and self._declaracao2.checaTipo(ambiente)
