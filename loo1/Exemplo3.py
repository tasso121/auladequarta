from loo1.comando.Atribuicao import Atribuicao
from loo1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.comando.ComDeclaracao import ComDeclaracao
from loo1.comando.IfThenElse import IfThenElse
from loo1.comando.New import New
from loo1.comando.Sequencial import Sequencial
from loo1.comando.Skip import Skip
from loo1.comando.Write import Write
from loo1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.declaracao.procedimento.DecParametro import DecParametro
from loo1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.declaracao.variavel.CompostaDecVariavel import CompostaDecVariavel
from loo1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.expressao.binaria.ExpEquals import ExpEquals
from loo1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.expressao.leftExpression.Id import Id
from loo1.expressao.ListaExpressao import ListaExpressao
from loo1.expressao.This import This
from loo1.expressao.unaria.ExpNot import ExpNot
from loo1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.expressao.valor.ValorNull import ValorNull
from loo1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.memoria.colecao.ListaValor import ListaValor
from loo1.Programa import Programa
from loo1.util.TipoClasse import TipoClasse
from loo1.util.TipoPrimitivo import TipoPrimitivo


def main():
    classeLValor = DecClasseSimples(
        Id("LValor"),
        CompostaDecVariavel(
            SimplesDecVariavel(TipoPrimitivo.TIPO_INTEIRO, Id("valor"), ValorInteiro(-100)),
            SimplesDecVariavel(TipoClasse(Id("LValor")), Id("prox"), ValorNull()),
        ),
        DecProcedimentoComposta(
            DecProcedimentoSimples(
                Id("insere"),
                ListaDeclaracaoParametro(DecParametro(Id("v"), TipoPrimitivo.TIPO_INTEIRO)),
                IfThenElse(
                    ExpEquals(AcessoAtributoThis(This(), Id("valor")), ValorInteiro(-100)),
                    Sequencial(
                        Atribuicao(AcessoAtributoThis(This(), Id("valor")), Id("v")),
                        New(AcessoAtributoThis(This(), Id("prox")), Id("LValor")),
                    ),
                    ChamadaMetodo(
                        AcessoAtributoThis(This(), Id("prox")),
                        Id("insere"),
                        ListaExpressao(Id("v")),
                    ),
                ),
            ),
            DecProcedimentoSimples(
                Id("print"),
                ListaDeclaracaoParametro(),
                Sequencial(
                    Write(AcessoAtributoThis(This(), Id("valor"))),
                    IfThenElse(
                        ExpNot(ExpEquals(AcessoAtributoThis(This(), Id("prox")), ValorNull())),
                        ChamadaMetodo(AcessoAtributoThis(This(), Id("prox")), Id("print"), ListaExpressao()),
                        Skip(),
                    ),
                ),
            ),
        ),
    )

    corpoComando = ComDeclaracao(
        DecVariavelObjeto(TipoClasse(Id("LValor")), Id("lv"), Id("LValor")),
        Sequencial(
            ChamadaMetodo(Id("lv"), Id("insere"), ListaExpressao(ValorInteiro(3))),
            Sequencial(
                ChamadaMetodo(Id("lv"), Id("insere"), ListaExpressao(ValorInteiro(4))),
                ChamadaMetodo(Id("lv"), Id("print"), ListaExpressao()),
            ),
        ),
    )

    programa = Programa(classeLValor, corpoComando)

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
