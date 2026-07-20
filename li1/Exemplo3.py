from li1.command.Atribuicao import Atribuicao
from li1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.command.SequenciaComando import SequenciaComando
from li1.command.SWrite import SWrite
from li1.command.While import While
from li1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.expression.ExpEquals import ExpEquals
from li1.expression.ExpNot import ExpNot
from li1.expression.ExpSoma import ExpSoma
from li1.expression.Id import Id
from li1.expression.ValorInteiro import ValorInteiro
from li1.expression.ValorString import ValorString
from li1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.memory.EntradaVaziaException import EntradaVaziaException
from li1.memory.ErroTipoEntradaException import ErroTipoEntradaException
from li1.memory.ListaValor import ListaValor
from li1.Programa import Programa
from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


def main():
    i = Id("i")

    programa = Programa(
        ComandoDeclaracao(
            DeclaracaoVariavel(i, ValorInteiro(0)),
            SequenciaComando(
                While(
                    ExpNot(ExpEquals(i, ValorInteiro(3))),
                    Atribuicao(i, ExpSoma(i, ValorInteiro(1))),
                ),
                SWrite(ValorString("Hello World")),
            ),
        )
    )

    ambComp = ContextoCompilacaoImperativa(ListaValor())
    ambExec = ContextoExecucaoImperativa(ListaValor())

    try:
        if programa.checaTipo(ambComp):
            saida = programa.executar(ambExec)
            print(f"Saida: {saida}")
        else:
            print("Erro de tipo.")
    except IdentificadorNaoDeclaradoException as e:
        print(f"Erro: {e}")
    except IdentificadorJaDeclaradoException as e:
        print(f"Erro: {e}")
    except ErroTipoEntradaException as e:
        print(f"Erro: {e}")
    except EntradaVaziaException as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
