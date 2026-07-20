from le2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from le2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException
from li1.command.Atribuicao import Atribuicao
from li1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.command.IfThenElse import IfThenElse
from li1.command.SequenciaComando import SequenciaComando
from li1.command.Skip import Skip
from li1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.expression.ExpEquals import ExpEquals
from li1.expression.ExpNot import ExpNot
from li1.expression.ExpSub import ExpSub
from li1.expression.Id import Id
from li1.expression.ValorInteiro import ValorInteiro
from li1.expression.ValorString import ValorString
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
    b = Id("b")
    a = Id("a")
    aExterno = Id("a")
    x = Id("x")
    escreveRecursivo = Id("escreveRecursivo")

    corpoThen = ComandoDeclaracao(
        DeclaracaoVariavel(x, ValorInteiro(0)),
        SequenciaComando(
            Atribuicao(x, ExpSub(a, ValorInteiro(1))),
            SequenciaComando(
                Write(ValorString("Ola")),
                ChamadaProcedimento(escreveRecursivo, ListaExpressao(x)),
            ),
        ),
    )

    corpoProc = IfThenElse(
        ExpNot(ExpEquals(a, ValorInteiro(0))),
        corpoThen,
        Skip(),
    )

    params = ListaDeclaracaoParametro(DeclaracaoParametro(a, TipoPrimitivo.INTEIRO))

    defEscreve = DefProcedimento(params, corpoProc)

    declaracoes = DeclaracaoComposta(
        DeclaracaoVariavel(b, ValorInteiro(3)),
        DeclaracaoProcedimento(escreveRecursivo, defEscreve),
    )

    # aExterno e um Id("a") diferente do 'a' usado como parametro formal do
    # procedimento (mas com o mesmo nome, logo igual por __eq__/__hash__) --
    # o Exemplo4 java testa a chamada com um Id vindo de fora do escopo de
    # declaracao do procedimento.
    programa = Programa(
        ComandoDeclaracao(
            declaracoes,
            ChamadaProcedimento(escreveRecursivo, ListaExpressao(aExterno)),
        )
    )

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        ambExec = ContextoExecucaoImperativa2(ListaValor())

        if programa.checaTipo(ambComp):
            saida = programa.executar(ambExec)
            print(f"Saida: {saida}")
        else:
            print("Erro de tipo: variavel 'a' nao declarada no escopo externo.")
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
