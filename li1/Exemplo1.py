from li1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.command.SWrite import SWrite
from li1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
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
    a = Id("a")
    b = Id("b")

    # var a = 3; write(b)  -- 'b' nunca foi declarado: demonstra o erro de tipo
    programa = Programa(
        ComandoDeclaracao(
            DeclaracaoVariavel(a, ValorInteiro(3)),
            SWrite(b),
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
