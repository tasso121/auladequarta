# Relatório do Projeto: Conversão Java to Python dos interpretadores le1 a loo1

Disciplina: Paradigmas de Linguagem de Programação (PLP), UFS
Repositório: git@github.com:tasso121/auladequarta.git

## 1. Objetivo

Neste projeto eu converti para Python a sequência de interpretadores que construímos ao longo dos laboratórios da disciplina, originalmente em Java:

| Estágio | Paradigma | Acrescenta em relação ao anterior |
|---|---|---|
| `le1` | expressões constantes | literais, operadores unários/binários |
| `le2` | expressões com escopo | `let`, variáveis, escopo léxico com shadowing |
| `lf1` | funcional | funções de primeira ordem, recursão, `if/then/else` como expressão |
| `li1` | imperativo | variáveis mutáveis, `:=`, sequência, blocos, `while`, `write` |
| `li2` | imperativo | procedimentos parametrizados/recursivos (sem retorno) |
| `loo1` | orientado a objetos | classes, objetos (`new`), `this`, atributos e métodos |

Cada estágio é um interpretador completo (avaliador de expressões, checador de tipos estático e executor de comandos) pra uma linguagem didática pequena, seguindo o padrão Interpreter clássico: toda `Expressao` tem `avaliar`/`checaTipo`/`getTipo`, todo `Comando` tem `executar`/`checaTipo`, toda `Declaracao` tem `elabora`/`checaTipo`.

## 2. Metodologia

Cada laboratório tem seu próprio pacote Java, com classes `Exemplo*.java` mostrando a linguagem em uso. Não tem gramática executável de verdade: a BNF é usada como especificação, e os programas de exemplo são montados na mão como árvore de sintaxe, tanto no Java quanto no meu porte em Python.

Pra cada estágio segui o mesmo processo:

1. Ler o pacote Java inteiro, não só as assinaturas dos métodos.
2. Portar cada classe pra um módulo Python correspondente, mantendo a mesma divisão de pacotes e a mesma semântica de cada método.
3. Portar os `Exemplo*.java` como scripts Python equivalentes.
4. Rodar cada exemplo e conferir a saída contra a semântica esperada, sem aceitar nada sem checar de verdade.
5. Reaproveitar código do estágio anterior sempre que o Java não mudava nada entre estágios (confirmando com `diff`, ignorando só a linha de declaração do pacote).

No final o projeto ficou com 241 arquivos `.py` e cerca de 3300 linhas de código, organizados em seis pacotes que rodam direto com `python3 -m <estagio>.Exemplo<N>` a partir da raiz do repositório.

## 3. Decisão central: reúso entre estágios

A principal diferença do meu porte em relação ao Java original é que lá cada estágio duplica o pacote inteiro, mesmo quando o pacote não muda uma linha de um estágio pro outro (confirmei isso com `diff -rq` em vários pares de estágios). No meu porte em Python eu evitei essa duplicação: sempre que o `diff` (ignorando a linha de `package`) mostrava dois arquivos Java idênticos entre estágios, eu importava direto o módulo Python já escrito, em vez de reescrever.

Isso só foi possível porque:

- `le1.expression.Expressao` já nasce com um parâmetro opcional `ambiente=None` em `avaliar/checaTipo/getTipo`, que o `le1` nunca usa. É esse parâmetro que permite `le2`/`lf1` reaproveitarem as classes de expressão do `le1` sem precisar mexer nelas.
- `le2.memory.Ambiente` e `Contexto` (pilha de escopos genérica, `Generic[T]`) são totalmente agnósticos ao tipo armazenado, então dá pra reaproveitar também em `li1`/`li2`/`loo1`, mesmo eles tendo sistemas de `Tipo` completamente diferentes de `le1`/`le2`.

Nos pontos em que o Java realmente muda tudo (`li1` troca o sistema de tipos inteiro e acrescenta `clone()`/`reduzir()` nas expressões, `loo1` troca tudo de novo com tipos de classe e ambientes de execução orientados a objetos), o meu porte também bifurca, sem forçar reúso onde nem o próprio Java reaproveita.

## 4. Notas por estágio

### le1, expressões constantes
A base de tudo: literais inteiro/booleano/string, operadores aritméticos/lógicos/de concatenação, unários (`not`, `-`, `length`). Checagem de tipo estática via `util.Tipo` (conjunto de tipos válidos).

### le2, variáveis e escopo léxico
Acrescenta `Id`, `ExpDeclaracao` (`let x = e1 in e2`), `DecVariavel` e o pacote `memory` (pilha de escopos genérica). `ExpEquals` é sobrescrita com checagem de tipo mais permissiva (via interseção de tipos possíveis). Escopo é léxico, com shadowing correto testado nos exemplos.

### lf1, funções de primeira ordem
Reaproveita praticamente 100% do pacote de expressões/memória do `le2`. Acrescenta `DecFuncao`, `Aplicacao`, `IfThenElse` (como expressão), `ValorFuncao` e um `RestrictTypesVisitor` pra inferir o tipo de identificadores livres no corpo de uma função. A semântica de escopo de função é dinâmica, não léxica (sem closures), confirmei isso testando os exemplos.

Nesse estágio encontrei um problema no Java original: `ContextoExecucaoFuncional` não implementava `clone()` apesar da interface exigir (do jeito que estava, o Java não compilaria nesse ponto). No meu porte em Python implementei o `clone()` corretamente.

### li1, imperativo
Ponto de bifurcação real: o Java troca todo o sistema de tipos (de um conjunto de tipos possíveis pra uma interface `Tipo` + enum `TipoPrimitivo`) e acrescenta `clone()`/`reduzir()` em toda expressão, então não dá pra reaproveitar a árvore de expressões do `le1`/`le2`. O pacote `memory`, por ser genérico, continua sendo reaproveitado do `le2` sem alteração. Acrescenta variáveis mutáveis (`:=`), sequência de comandos, blocos com declaração (`ComandoDeclaracao`), `while` e `write`.

Uma simplificação que fiz: implementei o `clone()` de `ExpBinaria`/`ExpUnaria` uma única vez de forma genérica via `type(self)(...)`, em vez de cada operador concreto reimplementar `clone()` individualmente como faz o Java original.

### li2, procedimentos
Confirmei com `diff -rq` que os pacotes Java `expressions1`, `expressions2` e `imperative1` do `li2` são idênticos aos do `li1` (só o nome do pacote muda), então reaproveitei quase tudo via import direto. O que é novo de verdade: procedimentos parametrizados e recursivos (`DefProcedimento`, `DeclaracaoProcedimento`, `ChamadaProcedimento`, `TipoProcedimento`) e um `ContextoExecucaoImperativa2` com pilha paralela de procedimentos. O escopo de procedimento é dinâmico, igual no `lf1`: o corpo executa na pilha de quem chama.

### loo1, orientação a objetos
Esse foi o estágio mais trabalhoso. O pacote `orientadaObjetos1` tem cerca de 6700 linhas e usa nomes de pacote em português (`comando`, `expressao`, `declaracao`, `memoria`, `util`, `excecao`), diferente do `li1`/`li2` que usam inglês (`command`, `expression`, `declaration`, `memory`). Mantive essa nomenclatura em português no porte pra ficar fiel ao original.

Assim como o `li1` bifurcou do `le2`, o `loo1` bifurca de novo: tem seu próprio sistema de tipos (`util.Tipo`/`TipoPrimitivo`/`TipoClasse`/`ListaTipo`) e sua própria árvore de expressões e comandos. Ainda assim reaproveita, via import direto (confirmado por diff ignorando só o nome do pacote raiz), peças de baixo nível já portadas: `le2.memory.Ambiente`/`Contexto`, `li1.util.Lista`, `li1.memory.ListaValor` e as exceções de identificador do `le2.memory`.

Alguns pontos do design que valem destacar:

- O heap é só um compartilhamento por referência dos mesmos dicionários de objetos e classes (`mapObjetos`, `mapDefClasse`) entre todo `ContextoExecucaoOO1` criado a partir de outro, sem nenhuma cadeia de delegação.
- Uma chamada de método não executa na pilha persistente do objeto, mas num contexto de execução novo e descartável a cada chamada. Os atributos persistem porque leitura e escrita passam direto pelo estado do objeto (um dicionário plano), nunca pela pilha de execução do método.
- Não precisa memoizar uma tabela de tipos por classe pra evitar recursão infinita em tempo de compilação: checar uma chamada de método só confere a assinatura (número e tipo dos parâmetros), nunca reverifica o corpo do método já verificado quando a classe foi declarada.
- `ValorRef` (referência a objeto) não estende `ValorConcreto`. Essa distinção é o que garante que a comparação `this.prox == null` funcione certo por comparação de identidade.
- Tem uma hierarquia `LeftExpression` própria (`Id`, `AcessoAtributoId`, `AcessoAtributoThis`) e uma expressão `This`.
- I/O completo: `Read`, `ReadFile`, `WriteFile` e `IO`, além do `Write`.

Os exemplos 3 e 4 reproduzem uma peculiaridade da linguagem: o método `insere` sempre aloca um nó sentinela vazio extra depois de gravar um valor, e o método de impressão percorre até esse sentinela e imprime ele também. Por isso a saída inclui um `-100` residual no final, do mesmo jeito que acontece no Java.

## 5. Testes e verificação

Não fiz uma suíte automatizada de testes unitários. A verificação foi rodar cada `Exemplo*.py` de cada estágio e conferir a saída contra o comportamento esperado da classe `Exemplo*.java` correspondente, incluindo casos de erro proposital (como uma variável usada fora de escopo). Os 21 exemplos, nos seis estágios, dão a saída esperada:

```
le1:  PLP UFS / 13 / True
le2:  Resultado = 2 / 3 / 6 / 4 / 8
lf1:  3 / 6 / 6 / 12
li1:  erro esperado / 3 2 7 3 / "Hello World" / "valores de entrada diferentes"
li2:  2 / 4 4 / "Ola" "Ola" "Ola" / erro esperado
loo1: 2 / 2 3 / 3 4 -100 / 2 3 4 -100 2 4 -100
```

## 6. Conclusão

Esse projeto mostrou na prática um dos pontos centrais da disciplina: o quanto a escolha de abstrações (parâmetros opcionais, genéricos, interfaces mínimas) afeta o quanto dá pra reaproveitar código entre variantes de uma linguagem. Enquanto o Java resolve isso duplicando pacotes inteiros, no meu porte em Python eu resolvi reaproveitando módulo direto, reduzindo a diferença entre estágios ao que realmente muda semanticamente (tipos, escopo de execução, modelo de memória), e não ao que só muda de nome de pacote.
