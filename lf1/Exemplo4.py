from le1.expression.ExpSoma import ExpSoma
from le1.expression.ExpSub import ExpSub
from le1.expression.ValorInteiro import ValorInteiro
from le2.expression.ExpEquals import ExpEquals
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from lf1.declaration.DecFuncao import DecFuncao
from lf1.expression.Aplicacao import Aplicacao
from lf1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.expression.IfThenElse import IfThenElse
from lf1.memory.ContextoExecucaoFuncional import ContextoExecucaoFuncional
from lf1.Programa import Programa
from lf1.util.ValorFuncao import ValorFuncao


def main():
    # fun mult(x, y) = if (x == 0) then 0 else (y + mult(x - 1, y))
    condicao = ExpEquals(Id("x"), ValorInteiro(0))
    sub = ExpSub(Id("x"), ValorInteiro(1))
    recursao = Aplicacao(Id("mult"), [sub, Id("y")])
    soma = ExpSoma(Id("y"), recursao)
    ifExp = IfThenElse(condicao, ValorInteiro(0), soma)

    valorFuncao = ValorFuncao([Id("x"), Id("y")], ifExp)
    mult = DecFuncao(Id("mult"), valorFuncao)

    ambiente = ContextoExecucaoFuncional()
    ambiente.incrementa()
    ambiente.mapFuncao(mult.getID(), mult.getFuncao())

    # mult(3, 4)
    app = Aplicacao(Id("mult"), [ValorInteiro(3), ValorInteiro(4)])
    programa = Programa(ExpDeclaracao([mult], app))

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
