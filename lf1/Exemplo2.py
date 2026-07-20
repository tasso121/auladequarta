from le1.expression.ExpSoma import ExpSoma
from le1.expression.ValorInteiro import ValorInteiro
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

    # var x = 3
    decX1 = DecVariavel(Id("x"), ValorInteiro(3))
    ambiente.map(decX1.getID(), decX1.getExpressao().avaliar(ambiente))

    # fun f(y) = y + x   -- x livre, resolvido dinamicamente no ambiente corrente
    corpo = ExpSoma(Id("y"), Id("x"))
    valorFuncao = ValorFuncao([Id("y")], corpo)
    funcao = DecFuncao(Id("f"), valorFuncao)
    ambiente.mapFuncao(funcao.getID(), funcao.getFuncao())

    ambiente.incrementa()

    # var x = 5  -- sombreia o x anterior; f nao usa closures lexicos
    decX2 = DecVariavel(Id("x"), ValorInteiro(5))
    ambiente.map(decX2.getID(), decX2.getExpressao().avaliar(ambiente))

    # f(1)
    app = Aplicacao(Id("f"), [ValorInteiro(1)])
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
