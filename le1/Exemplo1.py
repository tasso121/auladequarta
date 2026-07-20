from le1.expression.ExpAnd import ExpAnd
from le1.expression.ExpConcat import ExpConcat
from le1.expression.ExpEquals import ExpEquals
from le1.expression.ExpLength import ExpLength
from le1.expression.ExpMenos import ExpMenos
from le1.expression.ExpNot import ExpNot
from le1.expression.ExpOr import ExpOr
from le1.expression.ExpSoma import ExpSoma
from le1.expression.ExpSub import ExpSub
from le1.expression.ValorBooleano import ValorBooleano
from le1.expression.ValorInteiro import ValorInteiro
from le1.expression.ValorString import ValorString
from le1.Programa import Programa


def main():
    # (3 + 4) - 2 == 5
    exp1 = ExpEquals(
        ExpSub(ExpSoma(ValorInteiro(3), ValorInteiro(4)), ValorInteiro(2)),
        ValorInteiro(5),
    )
    p1 = Programa(exp1)
    print("checaTipo:", p1.checaTipo())
    p1.executar()

    # -5
    Programa(ExpMenos(ValorInteiro(5))).executar()

    # "PLP" ++ " UFS"
    Programa(ExpConcat(ValorString("PLP"), ValorString(" UFS"))).executar()

    # length("interpretador")
    Programa(ExpLength(ValorString("interpretador"))).executar()

    # (true and not false) or false
    exp5 = ExpOr(
        ExpAnd(ValorBooleano(True), ExpNot(ValorBooleano(False))),
        ValorBooleano(False),
    )
    Programa(exp5).executar()


if __name__ == "__main__":
    main()
