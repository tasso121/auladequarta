from li1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.command.SequenciaComando import SequenciaComando
from li1.command.SWrite import SWrite
from li1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.expression.ExpSoma import ExpSoma
from li1.expression.Id import Id
from li1.expression.ValorInteiro import ValorInteiro
from li1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.memory.EntradaVaziaException import EntradaVaziaException
from li1.memory.ErroTipoEntradaException import ErroTipoEntradaException
from li1.memory.ListaValor import ListaValor
from li1.Programa import Programa
from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


def main():
    a_externo = Id("a")
    a_interno = Id("a")
    b = Id("b")

    bloco_interno = ComandoDeclaracao(
        DeclaracaoComposta(
            DeclaracaoVariavel(a_interno, ValorInteiro(2)),
            DeclaracaoVariavel(b, ValorInteiro(5)),
        ),
        SequenciaComando(
            SWrite(a_interno),
            SWrite(ExpSoma(b, a_interno)),
        ),
    )

    programa = Programa(
        ComandoDeclaracao(
            DeclaracaoVariavel(a_externo, ValorInteiro(3)),
            SequenciaComando(
                SWrite(a_externo),
                SequenciaComando(
                    bloco_interno,
                    SWrite(a_externo),
                ),
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
