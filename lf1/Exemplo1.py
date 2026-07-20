from le1.expression.ExpSoma import ExpSoma
from le1.expression.ValorInteiro import ValorInteiro
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from lf1.declaration.DecFuncao import DecFuncao
from lf1.expression.Aplicacao import Aplicacao
from lf1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.memory.ContextoExecucaoFuncional import ContextoExecucaoFuncional
from lf1.Programa import Programa
from lf1.util.ValorFuncao import ValorFuncao


def main():
    # fun f(x) = x + 1
    corpo = ExpSoma(Id("x"), ValorInteiro(1))
    valorFuncao = ValorFuncao([Id("x")], corpo)
    funcao = DecFuncao(Id("f"), valorFuncao)

    ambiente = ContextoExecucaoFuncional()
    ambiente.incrementa()
    ambiente.mapFuncao(funcao.getID(), funcao.getFuncao())

    # f(2)
    app = Aplicacao(Id("f"), [ValorInteiro(2)])
    programa = Programa(ExpDeclaracao([funcao], app))

    try:
        if programa.checaTipo():
            resultado = app.avaliar(ambiente)
            print(resultado)
        else:
            print("Erro de tipo")
    except VariavelJaDeclaradaException as e:
        print(f"Variavel ja declarada: {e}")
    except VariavelNaoDeclaradaException as e:
        print(f"Variavel nao declarada: {e}")


if __name__ == "__main__":
    main()
