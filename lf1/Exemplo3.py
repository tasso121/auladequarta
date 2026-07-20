from le1.expression.ExpSoma import ExpSoma
from le1.expression.ValorInteiro import ValorInteiro
from le1.expression.ValorString import ValorString
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from lf1.declaration.DecFuncao import DecFuncao
from lf1.declaration.DecVariavel import DecVariavel
from lf1.expression.Aplicacao import Aplicacao
from lf1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.memory.ContextoExecucaoFuncional import ContextoExecucaoFuncional
from lf1.Programa import Programa
from lf1.util.ValorFuncao import ValorFuncao


def main():
    ambiente = ContextoExecucaoFuncional()
    ambiente.incrementa()

    # var y = 3
    decY = DecVariavel(Id("y"), ValorInteiro(3))
    ambiente.map(decY.getID(), decY.getExpressao().avaliar(ambiente))

    # fun f(x) = x + y
    corpo = ExpSoma(Id("x"), Id("y"))
    valorFuncao = ValorFuncao([Id("x")], corpo)
    funcao = DecFuncao(Id("f"), valorFuncao)
    ambiente.mapFuncao(funcao.getID(), funcao.getFuncao())

    ambiente.incrementa()

    # var z = "abc"  -- nao usada por f, so testa que outro escopo nao interfere
    decZ = DecVariavel(Id("z"), ValorString("abc"))
    ambiente.map(decZ.getID(), decZ.getExpressao().avaliar(ambiente))

    # f(3)
    app = Aplicacao(Id("f"), [ValorInteiro(3)])
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
