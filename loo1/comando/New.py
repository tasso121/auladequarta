from loo1.comando.Atribuicao import Atribuicao
from loo1.comando.Comando import Comando
from loo1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.memoria.ContextoObjeto import ContextoObjeto
from loo1.memoria.Objeto import Objeto
from loo1.util.TipoClasse import TipoClasse


class New(Comando):
    """New ::= LeftExpression ":=" "new" Id.

    Cria um ContextoExecucaoOO1 auxiliar (compartilhando o heap com
    'ambiente'), elabora os atributos da classe nele -- todos caem no mesmo
    (unico) frame que o construtor ja abriu -- e usa esse frame, ja
    populado, como o estado (ContextoObjeto) do novo objeto."""

    def __init__(self, av, classe):
        self._av = av
        self._classe = classe

    def executar(self, ambiente):
        defClasse = ambiente.getDefClasse(self._classe)
        decVariavel = defClasse.getDecVariavel()

        aux = decVariavel.elabora(ContextoExecucaoOO1(ambiente))
        estadoObj = ContextoObjeto(aux.getPilha().pop())
        objeto = Objeto(self._classe, estadoObj)

        vr = ambiente.getProxRef()
        ambiente.mapObjeto(vr, objeto)
        ambiente = Atribuicao(self._av, vr).executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente) -> bool:
        tpClasse = TipoClasse(self._classe)
        return (
            self._av.checaTipo(ambiente)
            and tpClasse.eValido(ambiente)
            and tpClasse.equals(self._av.getTipo(ambiente))
        )

    def getClasse(self):
        return self._classe

    def getAv(self):
        return self._av
