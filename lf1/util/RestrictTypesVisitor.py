from typing import Dict

from le1.expression.ExpAnd import ExpAnd
from le1.expression.ExpConcat import ExpConcat
from le1.expression.ExpLength import ExpLength
from le1.expression.ExpMenos import ExpMenos
from le1.expression.ExpNot import ExpNot
from le1.expression.ExpOr import ExpOr
from le1.expression.ExpSoma import ExpSoma
from le1.expression.ExpSub import ExpSub
from le1.expression.ValorBooleano import ValorBooleano
from le1.expression.ValorInteiro import ValorInteiro
from le1.expression.ValorString import ValorString
from le1.util.Tipo import Tipo
from le2.expression.ExpEquals import ExpEquals
from le2.expression.Id import Id
from le2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from le2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from lf1.expression.Aplicacao import Aplicacao
from lf1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.expression.IfThenElse import IfThenElse


class RestrictTypesVisitor:
    """Inferencia de tipos dos identificadores livres do corpo de uma funcao:
    percorre a arvore de expressao restringindo, para cada Id encontrado, o
    tipo esperado de acordo com o contexto sintatico em que ele aparece.

    Equivalente ao visitor Java que despachava via reflection sobre o nome
    da classe da expressao; aqui o despacho e feito por tipo concreto.
    """

    @staticmethod
    def visit(exp, ambiente, tipos: Dict[Id, Tipo], tipoEsperado: Tipo) -> Dict[Id, Tipo]:
        handler = _VISITORS.get(type(exp))
        if handler is None:
            return tipos
        return handler(exp, ambiente, tipos, tipoEsperado)


def _visit_aplicacao(aplicacao: Aplicacao, ambiente, tipos, tipoEsperado):
    try:
        t = ambiente.get(aplicacao.getFunc())
        mapIdTipo = tipos
        for exp in aplicacao.getArgsExpressao():
            tArg = Tipo(t.get())
            mapIdTipo = RestrictTypesVisitor.visit(exp, ambiente, mapIdTipo, tArg)
            t = t.getProx()
        return mapIdTipo
    except VariavelNaoDeclaradaException:
        # Funcao ainda nao declarada: restringe os argumentos sem tipo esperado.
        mapIdTipo = tipos
        tudo = Tipo()
        for exp in aplicacao.getArgsExpressao():
            mapIdTipo = RestrictTypesVisitor.visit(exp, ambiente, mapIdTipo, tudo)
        return mapIdTipo


def _visit_exp_and(expressao: ExpAnd, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
    return RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO)


def _visit_exp_or(expressao: ExpOr, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
    return RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO)


def _visit_exp_concat(expressao: ExpConcat, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_STRING)
    return RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_STRING)


def _visit_exp_soma(expressao: ExpSoma, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
    return RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO)


def _visit_exp_sub(expressao: ExpSub, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
    return RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO)


def _visit_exp_length(expressao: ExpLength, ambiente, tipos, tipoEsperado):
    return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_STRING)


def _visit_exp_menos(expressao: ExpMenos, ambiente, tipos, tipoEsperado):
    return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_INTEIRO)


def _visit_exp_not(expressao: ExpNot, ambiente, tipos, tipoEsperado):
    return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_BOOLEANO)


def _visit_exp_equals(expressao: ExpEquals, ambiente, tipos, tipoEsperado):
    return tipos


def _visit_exp_declaracao(expressao: ExpDeclaracao, ambiente, tipos, tipoEsperado):
    ambiente.incrementa()
    mapa = tipos
    for decFuncional in expressao.getSeqdecFuncional():
        tipoProcurado = None
        try:
            if decFuncional.getAridade() == 0:
                tipoProcurado = decFuncional.getExpressao().getTipo(ambiente)
                ambiente.map(decFuncional.getID(), tipoProcurado)
            else:
                tipo = decFuncional.getFuncao().getTipo(ambiente)
                tipoProcurado = tipo
                if tipo is not Tipo.TIPO_INDEFINIDO:
                    ambiente.map(decFuncional.getID(), tipo)
        except (VariavelJaDeclaradaException, VariavelNaoDeclaradaException):
            pass
        mapa = RestrictTypesVisitor.visit(decFuncional.getExpressao(), ambiente, mapa, tipoProcurado)
    mapa = RestrictTypesVisitor.visit(expressao.getExpressao(), ambiente, mapa, tipoEsperado)
    ambiente.restaura()
    return mapa


def _visit_if_then_else(expressao: IfThenElse, ambiente, tipos, tipoEsperado):
    aux = RestrictTypesVisitor.visit(expressao.getCondicao(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
    aux = RestrictTypesVisitor.visit(expressao.getThen(), ambiente, aux, tipoEsperado)
    return RestrictTypesVisitor.visit(expressao.getElseExpressao(), ambiente, aux, tipoEsperado)


def _visit_id(thisId: Id, ambiente, tipos, tipoEsperado):
    for id_, tipoAtual in list(tipos.items()):
        if id_ == thisId:
            tipos[id_] = tipoEsperado.intersecao(tipoAtual)
    return tipos


def _visit_valor(valor, ambiente, tipos, tipoEsperado):
    return tipos


_VISITORS = {
    Aplicacao: _visit_aplicacao,
    ExpAnd: _visit_exp_and,
    ExpOr: _visit_exp_or,
    ExpConcat: _visit_exp_concat,
    ExpSoma: _visit_exp_soma,
    ExpSub: _visit_exp_sub,
    ExpLength: _visit_exp_length,
    ExpMenos: _visit_exp_menos,
    ExpNot: _visit_exp_not,
    ExpEquals: _visit_exp_equals,
    ExpDeclaracao: _visit_exp_declaracao,
    IfThenElse: _visit_if_then_else,
    Id: _visit_id,
    ValorInteiro: _visit_valor,
    ValorString: _visit_valor,
    ValorBooleano: _visit_valor,
}
