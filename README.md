# Projeto PLP, interpretadores le1 a loo1 (Java -> Python)

Port em Python da sequência de interpretadores da disciplina Paradigmas de
Linguagens de Programacao (UFS), que originalmente fizemos em Java. Cada
estagio acrescenta uma construcao de linguagem ao anterior, e eu reaproveito
codigo entre os estagios sempre que os pacotes Java de origem eram
identicos ou genericos o suficiente (o Java original duplica o pacote
inteiro a cada estagio, aqui eu evitei isso).

## Estagios

| Pacote | Paradigma | Acrescenta |
|---|---|---|
| `le1` | expressoes constantes | literais, operadores unarios/binarios |
| `le2` | expressoes | `let`, escopo lexico com shadowing |
| `lf1` | funcional | funcoes de primeira ordem, recursao, `if/then/else` como expressao |
| `li1` | imperativo | variaveis mutaveis, `:=`, sequencia, blocos, `while`, `write` |
| `li2` | imperativo | procedimentos parametrizados/recursivos (sem retorno) sobre li1 |
| `loo1` | orientado a objetos | classes, objetos (`new`), `this`, atributos e metodos, sobre li1 |

Cada pacote tem `Programa.py` (monta `Contexto*` e chama `checaTipo`/
`executar`) e um ou mais `Exemplo*.py` executaveis:

```bash
python3 -m le1.Exemplo1
python3 -m li2.Exemplo3
python3 -m loo1.Exemplo4
```

## Reaproveitamento entre estagios

- `le1.expression.Expressao` ja nasce com um parametro opcional
  `ambiente=None` em `avaliar/checaTipo/getTipo`. O le1 nunca usa esse
  parametro, mas e o que permite le2/lf1 reaproveitarem as classes de
  expressao de le1 sem precisar mexer nelas.
- `le2.memory.Ambiente` e `Contexto` (pilha de escopos generica,
  `Generic[T]`) sao totalmente agnosticos ao tipo armazenado, por isso
  reaproveito tambem em li1/li2/loo1, mesmo eles tendo um sistema de
  `Tipo` completamente diferente de le1/le2.
- `li1` reaproveita `le2.memory` direto, mas tem seu proprio pacote
  `util.Tipo`/`TipoPrimitivo` (uma interface + `Enum`, em vez do
  `EnumSet` usado em le1/le2/lf1).
- `li2` reaproveita quase todo o `li1` (expressoes, comandos, ambiente de
  execucao/compilacao) e acrescenta so o necessario pra procedimentos:
  `TipoProcedimento`, `DefProcedimento`, `DeclaracaoProcedimento`,
  `ChamadaProcedimento`, `ListaExpressao` e um `ContextoExecucaoImperativa2`
  com uma pilha paralela de procedimentos.
- `loo1` reaproveita `li1` (comandos `IfThenElse/While/SequenciaComando/
  Skip/ComandoDeclaracao/Write`, expressoes `Exp*`, `Id`) e o padrao de
  procedimentos do `li2` (um metodo e, na pratica, um procedimento
  associado a uma classe). Ver secao especifica abaixo.

## loo1: notas de projeto

Esse pacote (`orientadaObjetos1` no Java, cerca de 6700 linhas) usa nomes
de pacote em portugues (`comando`, `expressao`, `declaracao`, `memoria`,
`util`, `excecao`), diferente do li1/li2 que usam ingles (`command`,
`expression`, `declaration`, `memory`). Mantive essa nomenclatura em
portugues no porte pra ficar fiel ao original.

O loo1 bifurca toda a arvore de `comando`/`declaracao`/`expressao`/
`util.Tipo*`, do mesmo jeito que o li1 bifurcou do le2: tem seu proprio
sistema de tipos (`util.Tipo`/`TipoPrimitivo`/`TipoClasse`/`ListaTipo`) e
sua propria hierarquia de expressoes/comandos, tipada pra
`AmbienteExecucaoOO1`/`AmbienteCompilacaoOO1`. Mesmo assim reaproveita, via
import direto (confirmado com diff ignorando so o nome do pacote raiz),
pecas de baixo nivel ja portadas: `le2.memory.Ambiente`/`Contexto`,
`li1.util.Lista`, `li1.memory.ListaValor` e as excecoes de identificador
do `le2.memory`.

Pontos principais do design:

- Heap compartilhado por referencia, sem delegacao. `ContextoExecucaoOO1(
  ambiente)` nao faz nenhuma cadeia de delegacao, ele so reaproveita os
  mesmos dicionarios `mapObjetos`/`mapDefClasse` e o mesmo contador
  `proxRef` do ambiente que o criou (igual objetos em Java, que sao
  passados por referencia).
- Metodo executa numa pilha nova e descartavel, nao na do objeto.
  `ChamadaMetodo`/`ChamadaProcedimento` criam um `ContextoExecucaoOO1(
  ambiente)` novo a cada chamada (compartilhando os dicionarios do heap,
  como acima), mapeiam `this` e os parametros ali, executam o corpo e
  descartam o contexto no final. Atributo nunca passa por essa pilha:
  leitura e escrita de atributo vai direto no `Objeto.getEstado()` (um
  dicionario plano, `ContextoObjeto`), alcancado via o `mapObjetos`
  compartilhado. E por isso que atributos persistem entre chamadas de
  metodo mesmo com uma pilha nova toda vez.
- Sem tabela de tipos memoizada por classe. `ChamadaMetodo`/
  `ChamadaProcedimento.checaTipo` so compara a assinatura (aridade e
  tipos dos parametros formais vs reais, checagem O(1)) e nunca
  reverifica o corpo do metodo chamado. O corpo e checado uma unica vez,
  em `DecProcedimentoSimples.checaTipo`, no momento da declaracao da
  classe. Por isso chamadas recursivas nunca disparam nova checagem de
  corpo e nao tem recursao em tempo de compilacao.
- `ValorRef` nao reaproveita `ValorConcreto`. Em `ExpEquals`, comparar um
  `ValorConcreto` (`ValorNull`) com algo que nao e `ValorConcreto`
  (`ValorRef`) cai em comparacao de identidade, que e exatamente o que
  faz `this.prox == null` virar `False` quando `prox` aponta pra um
  objeto real, e `True` enquanto ainda for `ValorNull`.
- `LeftExpression` e uma hierarquia propria. `Id` e
  `AcessoAtributoId`/`AcessoAtributoThis` implementam `LeftExpression`
  (separada de `Expressao`): `AcessoAtributoId` acessa um atributo a
  partir de um identificador (`obj.attr`), enquanto `AcessoAtributoThis`
  acessa um atributo do proprio objeto corrente via `this`.
- I/O completo: alem do `Write`, tem `Read`/`ReadFile`/`WriteFile`/`IO`.
- `Exemplo3`/`Exemplo4` reproduzem uma peculiaridade da linguagem: o
  metodo `insere` sempre aloca um novo no sentinela vazio depois de
  gravar um valor, e o metodo de impressao percorre ate esse sentinela e
  imprime ele tambem. Por isso a saida inclui um `-100` residual no
  final, preservado igual no Java, no mesmo espirito de manter
  comportamentos "estranhos" que ja vem do `li1/Exemplo1.py`.

## Testando tudo

```bash
cd /home/tassopc/Downloads/projeto
for pkg in le1 le2 lf1; do python3 -m $pkg.Exemplo1; done
for pkg in li1 li2 loo1; do
  for i in 1 2 3 4; do python3 -m $pkg.Exemplo$i; done
done
```
