from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException
from li1.command.Atribuicao import Atribuicao
from li1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.command.SequenciaComando import SequenciaComando
from li1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.expression.ExpSoma import ExpSoma
from li1.expression.Id import Id
from li1.expression.ValorInteiro import ValorInteiro
from li1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.memory.EntradaVaziaException import EntradaVaziaException
from li1.memory.ErroTipoEntradaException import ErroTipoEntradaException
from li1.memory.ListaValor import ListaValor
from li1.util.TipoPrimitivo import TipoPrimitivo
from li2.command.ChamadaProcedimento import ChamadaProcedimento
from li2.command.ListaExpressao import ListaExpressao
from li2.command.Write import Write
from li2.declaration.DeclaracaoParametro import DeclaracaoParametro
from li2.declaration.DeclaracaoProcedimento import DeclaracaoProcedimento
from li2.declaration.DefProcedimento import DefProcedimento
from li2.declaration.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from li2.memory.ContextoExecucaoImperativa2 import ContextoExecucaoImperativa2
from li2.memory.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from li2.memory.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException
from li2.Programa import Programa

if __name__ == "__main__":
    x = Id("x")
    y = Id("y")
    p = Id("p")

    params = ListaDeclaracaoParametro(DeclaracaoParametro(y, TipoPrimitivo.INTEIRO))

    defP = DefProcedimento(params, Atribuicao(x, ExpSoma(x, y)))

    blocoInterno = ComandoDeclaracao(
        DeclaracaoVariavel(x, ValorInteiro(1)),
        SequenciaComando(
            ChamadaProcedimento(p, ListaExpressao(ValorInteiro(3))),
            Write(x),
        ),
    )

    declaracoes = DeclaracaoComposta(
        DeclaracaoVariavel(x, ValorInteiro(0)),
        DeclaracaoProcedimento(p, defP),
    )

    programa = Programa(
        ComandoDeclaracao(
            declaracoes,
            SequenciaComando(
                blocoInterno,
                SequenciaComando(
                    ChamadaProcedimento(p, ListaExpressao(ValorInteiro(4))),
                    Write(x),
                ),
            ),
        )
    )

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        ambExec = ContextoExecucaoImperativa2(ListaValor())

        if programa.checaTipo(ambComp):
            saida = programa.executar(ambExec)
            print(f"Saida: {saida}")
        else:
            print("Erro de tipo.")
    except ProcedimentoJaDeclaradoException as e:
        print(f"Erro de procedimento: {e}")
    except IdentificadorJaDeclaradoException as e:
        print(f"Identificador ja declarado: {e}")
    except ProcedimentoNaoDeclaradoException as e:
        print(f"Erro de procedimento nao declarado: {e}")
    except IdentificadorNaoDeclaradoException as e:
        print(f"Identificador nao declarado: {e}")
    except EntradaVaziaException as e:
        print(f"Entrada vazia: {e}")
    except ErroTipoEntradaException as e:
        print(f"Erro de tipo na entrada: {e}")
