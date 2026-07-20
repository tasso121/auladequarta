from li1.command.Comando import Comando
from li1.expression.Expressao import Expressao
from li1.expression.ValorBooleano import ValorBooleano


class IfThenElse(Comando):
    def __init__(self, expressao: Expressao, comandoThen: Comando, comandoElse: Comando):
        self._expressao = expressao
        self._comandoThen = comandoThen
        self._comandoElse = comandoElse

    def executar(self, ambiente):
        condicao: ValorBooleano = self._expressao.avaliar(ambiente)
        if condicao.valor():
            return self._comandoThen.executar(ambiente)
        return self._comandoElse.executar(ambiente)

    def checaTipo(self, ambiente) -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comandoThen.checaTipo(ambiente)
            and self._comandoElse.checaTipo(ambiente)
        )
