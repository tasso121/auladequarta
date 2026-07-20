# Relatório do Projeto — Conversão Java → Python dos interpretadores le1..loo1

**Disciplina:** Paradigmas de Linguagem de Programação (PLP) — UFS
**Repositório:** `git@github.com:tasso121/auladequarta.git`

## 1. Objetivo

Este projeto consistiu em converter, de Java para Python, a hierarquia de
interpretadores construída ao longo dos laboratórios da disciplina:

| Estágio | Paradigma | Acrescenta em relação ao anterior |
|---|---|---|
| `le1` | expressões constantes | literais, operadores unários/binários |
| `le2` | expressões com escopo | `let`, variáveis, escopo léxico com shadowing |
| `lf1` | funcional | funções de primeira ordem, recursão, `if/then/else` como expressão |
| `li1` | imperativo | variáveis mutáveis, `:=`, sequência, blocos, `while`, `write` |
| `li2` | imperativo | procedimentos parametrizados/recursivos (sem retorno) |
| `loo1` | orientado a objetos | classes, objetos (`new`), `this`, atributos e métodos |

Cada estágio implementa um interpretador completo (avaliador de expressões,
checador de tipos estático e executor de comandos) para uma pequena
linguagem didática, seguindo o padrão *Interpreter* clássico: toda
`Expressao` tem `avaliar`/`checaTipo`/`getTipo`, todo `Comando` tem
`executar`/`checaTipo`, toda `Declaracao` tem `elabora`/`checaTipo`.

## 2. Metodologia

O material de origem (fornecido pelo professor) consistia em seis zips
Java, um por estágio, cada um com um pacote completo de fontes e classes
`Exemplo*.java` demonstrando a linguagem em uso — sem gramática formal
executável (BNF é usada como especificação, não como parser: os programas
de exemplo são montados manualmente como árvores de sintaxe, tanto no
Java original quanto no porte Python).

O trabalho seguiu, para cada estágio, o mesmo processo:

1. Extrair e ler o pacote Java integralmente (não apenas as assinaturas).
2. Portar cada classe pública Java para um módulo Python correspondente,
   preservando a divisão de pacotes e a semântica exata de cada método.
3. Portar os `Exemplo*.java` como scripts Python equivalentes.
4. Executar cada exemplo e conferir a saída contra um rastreio manual da
   semântica esperada (nunca aceitar saída sem essa verificação).
5. Reaproveitar código do estágio anterior sempre que o Java de origem
   comprovadamente não mudasse entre estágios (confirmado por `diff`
   ignorando apenas a declaração de pacote).

Ao todo, o projeto final tem 241 arquivos `.py` e aproximadamente 3300
linhas de código Python, organizados em seis pacotes importáveis
(`python3 -m <estagio>.Exemplo<N>` a partir da raiz do repositório).

## 3. Decisão central de design: reúso real entre estágios

A diferença mais importante em relação ao material original é que o Java
**duplica o pacote inteiro a cada estágio** — mesmo quando um pacote não
muda uma linha entre um estágio e o seguinte (confirmado por `diff -rq`
para vários pares de estágios), ele é copiado por completo para o novo
projeto Java, só trocando o nome do pacote raiz.

O porte em Python evita essa duplicação: sempre que um `diff` (ignorando
a linha de `package`) mostrou dois arquivos Java idênticos entre
estágios, o módulo Python já escrito para o estágio anterior é
**reaproveitado via import direto**, em vez de reescrito. Isso só é
possível porque:

- `le1.expression.Expressao` já nasce com um parâmetro opcional
  `ambiente=None` em `avaliar/checaTipo/getTipo`, que `le1` nunca usa —
  isso é o que permite `le2`/`lf1` reaproveitarem as classes de expressão
  de `le1` sem modificá-las.
- `le2.memory.{Ambiente,Contexto}` (pilha de escopos genérica,
  `Generic[T]`) é totalmente agnóstica ao tipo armazenado — por isso é
  reaproveitada também por `li1`/`li2`/`loo1`, mesmo eles tendo sistemas
  de `Tipo` completamente diferentes de `le1`/`le2`.

Nos pontos em que o Java de fato diverge (`li1` reformula todo o sistema
de tipos e adiciona `clone()`/`reduzir()` às expressões; `loo1` reformula
tudo de novo com tipos de classe e ambientes de execução orientados a
objetos), o porte Python também bifurca — sem tentar forçar reúso onde o
próprio Java não reaproveita.

## 4. Notas por estágio

### le1 — expressões constantes
Base da hierarquia: literais inteiro/booleano/string, operadores
aritméticos/lógicos/de concatenação, unários (`not`, `-`, `length`).
Checagem de tipo estática via `util.Tipo` (conjunto de tipos válidos).

### le2 — variáveis e escopo léxico
Acrescenta `Id`, `ExpDeclaracao` (`let x = e1 in e2`), `DecVariavel` e o
pacote `memory` (pilha de escopos genérica). `ExpEquals` é sobrescrita
com checagem de tipo mais permissiva (via interseção de tipos possíveis).
Escopo é léxico, com shadowing correto testado nos exemplos.

### lf1 — funções de primeira ordem
Reaproveita praticamente 100% do pacote de expressões/memória de `le2`.
Acrescenta `DecFuncao`, `Aplicacao`, `IfThenElse` (como expressão),
`ValorFuncao` e um `RestrictTypesVisitor` para inferir o tipo de
identificadores livres no corpo de uma função. A semântica de escopo de
função é **dinâmica**, não léxica (sem closures) — confirmado testando
os exemplos originais.

Foi identificado e corrigido um gap do Java original:
`ContextoExecucaoFuncional` não implementava `clone()` apesar de a
interface exigir (o Java original, tal como fornecido, não compilaria
nesse ponto); o porte Python implementa `clone()` corretamente.

### li1 — imperativo
Ponto de bifurcação real da hierarquia: o Java troca todo o sistema de
tipos (de um conjunto de tipos possíveis para uma interface `Tipo` +
enum `TipoPrimitivo`) e acrescenta `clone()`/`reduzir()` a toda
expressão — por isso não reaproveita a árvore de expressões de
`le1`/`le2`. O pacote `memory` genérico, por ser agnóstico ao tipo
armazenado, continua sendo reaproveitado de `le2` sem alteração.
Acrescenta variáveis mutáveis (`:=`), sequência de comandos, blocos com
declaração (`ComandoDeclaracao`), `while` e `write`.

Uma simplificação deliberada: `clone()` de `ExpBinaria`/`ExpUnaria` foi
implementado uma única vez de forma genérica via `type(self)(...)`, em
vez de cada operador concreto reimplementar `clone()` individualmente
(como faz o Java original).

### li2 — procedimentos
Confirmado por `diff -rq` que os pacotes Java `expressions1`,
`expressions2` e `imperative1` de `li2` são idênticos aos de `li1` (só o
nome do pacote muda) — reaproveitados quase 100% via import direto.
Acrescenta procedimentos parametrizados e recursivos (`DefProcedimento`,
`DeclaracaoProcedimento`, `ChamadaProcedimento`, `TipoProcedimento`) e um
`ContextoExecucaoImperativa2` com pilha paralela de procedimentos.
Escopo de procedimento é dinâmico (como em `lf1`): o corpo executa na
pilha de quem chama.

### loo1 — orientação a objetos
O zip Java deste estágio chegou depois dos demais; uma primeira versão
do pacote foi projetada do zero a partir do material do laboratório
(BNF, descrição da interface de ambiente e os quatro programas de
exemplo dos slides), antes do Java real estar disponível. Quando o Java
real (~6700 linhas, pacote `orientadaObjetos1`) chegou, o pacote foi
**reportado por completo** a partir dele — o que permitiu corrigir
diversas suposições razoáveis, mas equivocadas, da versão especulativa:

- O modelo de heap **não** usa uma cadeia de delegação entre ambientes
  de execução (como a versão especulativa supunha); é simplesmente um
  compartilhamento por referência dos mesmos dicionários de objetos e
  classes entre todo `ContextoExecucaoOO1` criado a partir de outro.
- Uma chamada de método **não** executa na pilha persistente do objeto,
  mas num contexto de execução novo e descartável a cada chamada;
  atributos persistem porque leitura/escrita passa direto pelo estado do
  objeto (um dicionário plano), nunca pela pilha de execução do método.
- Não há necessidade de memoizar uma tabela de tipos por classe para
  evitar recursão infinita em tempo de compilação — o Java real evita o
  problema de forma estrutural: verificar uma chamada de método só
  confere a assinatura (número e tipo dos parâmetros), nunca reverifica
  o corpo do método já verificado na declaração da classe.
- `ValorRef` (referência a objeto) **não** compartilha implementação com
  `ValorConcreto`, ao contrário do que a versão especulativa fazia — essa
  distinção é o que garante que a comparação `this.prox == null` funcione
  corretamente por meio de comparação de identidade.

Notavelmente, diferente de `li1`/`li2` (pacotes Java em inglês), o Java
de `loo1` usa nomenclatura em português (`comando`, `expressao`,
`declaracao`, `memoria`, `excecao`) — mantida no porte Python por
fidelidade ao original, ainda que quebre a convenção em inglês dos
estágios anteriores.

Os exemplos 3 e 4 preservam deliberadamente uma peculiaridade do
material da disciplina: o método `insere` de uma lista ligada sempre
aloca um nó-sentinela vazio extra após gravar um valor, e o método de
impressão o percorre e imprime também — por isso a saída inclui um
`-100` residual ao final, reproduzido fielmente tal como no Java
original.

## 5. Testes e verificação

Não há suíte automatizada de testes unitários: a verificação foi feita
executando cada `Exemplo*.py` de cada estágio e conferindo manualmente a
saída contra o comportamento esperado da respectiva classe
`Exemplo*.java` (incluindo casos de erro propositais, como uma variável
usada fora de escopo). Todos os 21 exemplos, nos seis estágios, produzem
a saída esperada:

```
le1:  PLP UFS / 13 / True
le2:  Resultado = 2 / 3 / 6 / 4 / 8
lf1:  3 / 6 / 6 / 12
li1:  erro esperado / 3 2 7 3 / "Hello World" / "valores de entrada diferentes"
li2:  2 / 4 4 / "Ola" "Ola" "Ola" / erro esperado
loo1: 2 / 2 3 / 3 4 -100 / 2 3 4 -100 2 4 -100
```

## 6. Conclusão

A conversão evidencia, na prática, um dos temas centrais da disciplina:
o quanto a escolha de abstrações (parâmetros opcionais, genéricos,
interfaces mínimas) afeta a reutilização de código entre variantes de
uma linguagem. Onde o Java original resolve essa reutilização por
duplicação de pacotes, o porte Python resolve por composição e reúso
direto de módulo — reduzindo a distância entre estágios ao que
realmente muda semanticamente entre eles (tipos, escopo de execução,
modelo de memória), e não ao que muda apenas de nome de pacote.
