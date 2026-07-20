class VariavelJaDeclaradaException(Exception):
    """Nao usada em tempo de execucao -- o mapeamento id->valor/tipo real
    (Contexto.map, reaproveitado de le2) lanca le2.memory.VariavelJaDeclaradaException.
    Mantida apenas porque existe na classe Java original (nunca instanciada la)."""

    def __init__(self, id_):
        super().__init__(f"Variavel {id_} ja declarada.")
