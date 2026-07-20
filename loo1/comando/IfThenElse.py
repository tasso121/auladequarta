from loo1.comando.Comando import Comando


class IfThenElse(Comando):
    def __init__(self, expressao, comandoThen: Comando, comandoElse: Comando):
        self._expressao = expressao
        self._comandoThen = comandoThen
        self._comandoElse = comandoElse

    def executar(self, ambiente):
        if self._expressao.avaliar(ambiente).valor():
            return self._comandoThen.executar(ambiente)
        return self._comandoElse.executar(ambiente)

    def checaTipo(self, ambiente) -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comandoThen.checaTipo(ambiente)
            and self._comandoElse.checaTipo(ambiente)
        )
