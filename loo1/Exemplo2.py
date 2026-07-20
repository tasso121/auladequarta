from loo1.comando.Atribuicao import Atribuicao
from loo1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.comando.ComDeclaracao import ComDeclaracao
from loo1.comando.Sequencial import Sequencial
from loo1.comando.Write import Write
from loo1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.declaracao.variavel.CompostaDecVariavel import CompostaDecVariavel
from loo1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.expressao.binaria.ExpSoma import ExpSoma
from loo1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.expressao.leftExpression.Id import Id
from loo1.expressao.ListaExpressao import ListaExpressao
from loo1.expressao.This import This
from loo1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.memoria.colecao.ListaValor import ListaValor
from loo1.Programa import Programa
from loo1.util.TipoClasse import TipoClasse
from loo1.util.TipoPrimitivo import TipoPrimitivo


def main():
    classeContador = DecClasseSimples(
        Id("Contador"),
        SimplesDecVariavel(TipoPrimitivo.TIPO_INTEIRO, Id("valor"), ValorInteiro(1)),
        DecProcedimentoComposta(
            DecProcedimentoSimples(
                Id("print"),
                ListaDeclaracaoParametro(),
                Write(AcessoAtributoThis(This(), Id("valor"))),
            ),
            DecProcedimentoSimples(
                Id("inc"),
                ListaDeclaracaoParametro(),
                Atribuicao(
                    AcessoAtributoThis(This(), Id("valor")),
                    ExpSoma(AcessoAtributoThis(This(), Id("valor")), ValorInteiro(1)),
                ),
            ),
        ),
    )

    corpoComando = ComDeclaracao(
        CompostaDecVariavel(
            DecVariavelObjeto(TipoClasse(Id("Contador")), Id("c"), Id("Contador")),
            DecVariavelObjeto(TipoClasse(Id("Contador")), Id("c2"), Id("Contador")),
        ),
        Sequencial(
            ChamadaMetodo(Id("c"), Id("inc"), ListaExpressao()),
            Sequencial(
                ChamadaMetodo(Id("c2"), Id("inc"), ListaExpressao()),
                Sequencial(
                    ChamadaMetodo(Id("c2"), Id("inc"), ListaExpressao()),
                    Sequencial(
                        ChamadaMetodo(Id("c"), Id("print"), ListaExpressao()),
                        ChamadaMetodo(Id("c2"), Id("print"), ListaExpressao()),
                    ),
                ),
            ),
        ),
    )

    programa = Programa(classeContador, corpoComando)

    try:
        ambienteCompilacao = ContextoCompilacaoOO1(ListaValor())
        tipoValido = programa.checaTipo(ambienteCompilacao)

        if tipoValido:
            ambienteExecucao = ContextoExecucaoOO1(ListaValor())
            programa.executar(ambienteExecucao)
        else:
            print("Erro")
    except Exception as e:
        print(f"Exception: {e}")
        raise


if __name__ == "__main__":
    main()
