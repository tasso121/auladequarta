from le1.expression.ExpSoma import ExpSoma
from le1.expression.ValorInteiro import ValorInteiro
from le2.declaration.DecVariavel import DecVariavel
from le2.expression.ExpDeclaracao import ExpDeclaracao
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from le2.Programa import Programa


def main():
    x = Id("x")

    # let var x = 1 in x + 1
    programa = Programa(
        ExpDeclaracao(
            [DecVariavel(x, ValorInteiro(1))],
            ExpSoma(x, ValorInteiro(1)),
        )
    )

    try:
        if programa.checaTipo():
            resultado = programa.executar()
            print(f"Resultado = {resultado}")
        else:
            print("Erro de tipo.")
    except VariavelNaoDeclaradaException as e:
        print(f"Erro: variavel nao declarada - {e}")
    except VariavelJaDeclaradaException as e:
        print(f"Erro: variavel ja declarada - {e}")


if __name__ == "__main__":
    main()
