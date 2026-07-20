# Projeto PLP -- interpretadores le1 a loo1 (Java -> Python)

Port em Python da hierarquia de interpretadores da disciplina Paradigmas de
Linguagens de Programacao (UFS), originalmente em Java. Cada estagio
acrescenta uma construcao de linguagem ao anterior, e o codigo e
**reaproveitado entre os estagios** sempre que os pacotes Java de origem
eram identicos ou genericos o suficiente (ao contrario do Java original,
que duplica pacotes inteiros a cada estagio).

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
  `ambiente=None` em `avaliar/checaTipo/getTipo` -- le1 nunca usa esse
  parametro, mas e o que permite le2/lf1 reaproveitarem as classes de
  expressao de le1 **sem modifica-las**.
- `le2.memory.{Ambiente,Contexto}` (pilha de escopos generica,
  `Generic[T]`) e totalmente agnostica ao tipo armazenado -- por isso e
  reaproveitada tambem por li1/li2/loo1, mesmo eles tendo um sistema de
  `Tipo` completamente diferente de le1/le2.
- `li1` reaproveita `le2.memory` diretamente, mas tem seu proprio pacote
  `util.Tipo`/`TipoPrimitivo` (uma interface + `Enum`, em vez do
  `EnumSet` usado em le1/le2/lf1).
- `li2` reaproveita quase todo o `li1` (expressoes, comandos, ambiente de
  execucao/compilacao) e acrescenta apenas o necessario para
  procedimentos: `TipoProcedimento`, `DefProcedimento`,
  `DeclaracaoProcedimento`, `ChamadaProcedimento`, `ListaExpressao` e um
  `ContextoExecucaoImperativa2` com uma pilha paralela de procedimentos.
- `loo1` reaproveita `li1` (comandos `IfThenElse/While/SequenciaComando/
  Skip/ComandoDeclaracao/Write`, expressoes `Exp*`, `Id`) e o padrao de
  procedimentos de `li2` (um metodo e, na pratica, um procedimento
  associado a uma classe) -- ver secao especifica abaixo.

## loo1: notas de projeto

O zip original de `loo1` chegou depois dos demais estagios. Uma primeira
versao deste pacote foi implementada do zero a partir do PDF
`PP_Lab06-_linguagem_loo1.pdf` (BNF, interface `AmbienteExecucaoOO1` e o
pseudocodigo do comando `New`); quando o Java real (`orientadaObjetos1`,
~6700 linhas) ficou disponivel, o pacote foi **reportado por completo**
a partir dele, corrigindo varias suposicoes da versao especulativa.
Diferente de li1/li2 (pacotes Java em ingles: `command`/`expression`/
`declaration`/`memory`), o Java de loo1 usa nomes em portugues
(`comando`/`expressao`/`declaracao`/`memoria`/`util`/`excecao`) -- o
porte Python mantem essa mesma nomenclatura por fidelidade ao original.

`orientadaObjetos1` bifurca (fork) toda a arvore de `comando`/
`declaracao`/`expressao`/`util.Tipo*`, do mesmo jeito que li1 bifurcou de
le2 -- tem seu proprio sistema de tipos (`util.Tipo`/`TipoPrimitivo`/
`TipoClasse`/`ListaTipo`) e sua propria hierarquia de expressoes/
comandos, tipada para `AmbienteExecucaoOO1`/`AmbienteCompilacaoOO1`.
Ainda assim reaproveita, via import direto (confirmado por diff
ignorando so o nome do pacote raiz), pecas de baixo nivel ja portadas:
`le2.memory.{Ambiente,Contexto}` (pilha de escopos generica),
`li1.util.Lista`, `li1.memory.ListaValor` e as excecoes de
identificador de `le2.memory`.

Decisoes principais (a versao final, apos o porte fiel do Java real):

- **Heap simplesmente compartilhado por referencia, sem delegacao.**
  `ContextoExecucaoOO1(ambiente)` nao implementa uma cadeia de delegacao
  (isso era um chute da versao especulativa) -- ele so **reaproveita os
  mesmos dicionarios** `mapObjetos`/`mapDefClasse` e o mesmo contador
  `proxRef` do ambiente que o criou (semelhante a como HashMap/objetos em
  Java sao passados por referencia). Nao ha metodo de delegacao nenhum;
  e so nao copiar essas estruturas ao construir um novo contexto.
- **Metodo executa numa pilha nova e descartavel, nao na do objeto.**
  Diferente do que a versao especulativa supunha (metodo rodando na
  pilha persistente do proprio objeto), `ChamadaMetodo`/
  `ChamadaProcedimento` criam um `ContextoExecucaoOO1(ambiente)`
  **novo e temporario** a cada chamada (compartilhando os dicionarios do
  heap, como acima), mapeiam `this` e os parametros ali, executam o
  corpo, e descartam esse contexto ao final. Atributos nunca passam por
  essa pilha: leitura/escrita de atributo vai direto ao `Objeto.
  getEstado()` (um dicionario piano, `ContextoObjeto`), alcancado via o
  `mapObjetos` compartilhado -- e por isso que atributos persistem entre
  chamadas de metodo mesmo com uma pilha nova a cada vez.
- **Sem tabela de tipos memoizada por classe.** A versao especulativa
  criava uma tabela per-classe para evitar recursao infinita ao checar
  `this.prox.insere(v)`. O Java real evita o problema de forma
  estrutural: `ChamadaMetodo`/`ChamadaProcedimento.checaTipo` so compara
  a assinatura (aridade/tipos dos parametros formais vs. reais, checagem
  O(1)) e **nunca reverifica o corpo do metodo chamado** -- o corpo e
  checado uma unica vez, em `DecProcedimentoSimples.checaTipo`, no
  momento da declaracao da classe. Chamadas recursivas nunca disparam
  nova checagem de corpo, entao nao ha recursao em tempo de compilacao.
- **`ValorRef` NAO reaproveita `ValorConcreto`.** Ao contrario do que a
  versao especulativa fazia, `ValorRef` nao estende `ValorConcreto` --
  isso e proposital: em `ExpEquals`, comparar um `ValorConcreto`
  (`ValorNull`) com algo que nao e `ValorConcreto` (`ValorRef`) cai em
  comparacao de identidade, que e exatamente o que faz `this.prox ==
  null` virar `False` quando `prox` aponta pra um objeto real, e `True`
  enquanto ainda for `ValorNull`.
- **`LeftExpression` e uma hierarquia propria.** `Id` e
  `AcessoAtributoId`/`AcessoAtributoThis` implementam `LeftExpression`
  (separada de `Expressao`), refletindo o Java: `AcessoAtributoId` acessa
  um atributo a partir de um identificador (`obj.attr`), enquanto
  `AcessoAtributoThis` acessa um atributo do proprio objeto corrente via
  `this` -- a versao especulativa nao tinha essa distincao nem a
  expressao `This`.
- **I/O completo**: alem de `Write`, o Java real tem `Read`/`ReadFile`/
  `WriteFile`/`IO`, todos portados (a versao especulativa so tinha
  `Write`).
- **`Exemplo3`/`Exemplo4` reproduzem fielmente uma peculiaridade do
  material da disciplina**: o metodo `insere` sempre aloca um novo
  no-sentinela vazio apos gravar um valor, e o metodo de impressao
  percorre ate esse sentinela e o imprime tambem -- por isso a saida
  inclui um `-100` residual ao final. Preservado tal como no Java
  original, no mesmo espirito de manter comportamentos "estranhos" ja
  adotado em `li1/Exemplo1.py`.

## Testando tudo

```bash
cd /home/tassopc/Downloads/projeto
for pkg in le1 le2 lf1; do python3 -m $pkg.Exemplo1; done
for pkg in li1 li2 loo1; do
  for i in 1 2 3 4; do python3 -m $pkg.Exemplo$i; done
done
```
