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

O zip original de `loo1` **nao foi fornecido** neste projeto -- o pacote
foi implementado do zero a partir do PDF `PP_Lab06-_linguagem_loo1.pdf`
(BNF da Figura 28, interface `AmbienteExecucaoOO1` da Figura 30 e o
pseudocodigo do comando `New` da Figura 31), seguindo o mesmo estilo de
porte fiel usado nos demais estagios.

Decisoes principais:

- **Heap compartilhado via delegacao em cadeia.** Cada objeto tem seu
  proprio `ContextoExecucaoOO1` (pilha de variaveis/atributos e pilha de
  metodos PROPRIAS, para encapsulamento), mas classes, objetos, o contador
  de referencias e a saida do programa sao um unico heap compartilhado:
  todo `ContextoExecucaoOO1` criado para um objeto guarda uma referencia
  para o ambiente que o criou e **delega** `getDefClasse/getObjeto/
  mapObjeto/getProxRef/read/write/getSaida` a ele, subindo a cadeia ate o
  ambiente raiz do programa (o unico que de fato guarda esses dados).
- **Metodo executa no ambiente do objeto, nao no do chamador.** Diferente
  de `li2.ChamadaProcedimento` (escopo dinamico: o procedimento roda na
  pilha de quem chama), `loo1.ChamadaMetodo` busca o `Objeto` pela
  referencia e executa o corpo do metodo na pilha **do proprio objeto**
  (`objeto.getAmbiente()`), o que da a ele acesso a `this` e aos atributos
  sem precisa-los como parametro -- e o que torna isso genuinamente POO e
  nao apenas "procedimentos com um primeiro parametro implicito".
- **Verificacao de tipos de metodos e memoizada por classe.** Uma
  chamada `obj.metodo(...)` precisa que `this` esteja mapeado para
  checar o corpo do metodo (`this.atributo`, chamadas recursivas como
  `this.prox.insere(v)`). Uma tabela por classe (`DefClasse.
  getTabelaMetodos`) e construida e cacheada uma unica vez, atribuindo a
  tabela a si mesma **antes** de checar os corpos -- assim, chamadas
  recursivas/mutuas encontram a mesma tabela em construcao (com `this` e
  os metodos ja declarados ate ali) em vez de reverificar tudo de novo
  (o que causaria recursao infinita em tempo de compilacao).
- **`ValorRef`/`ValorNull` reaproveitam `ValorConcreto`.** Em vez de criar
  um caminho de igualdade especial, `ValorRef` e `ValorNull` sao
  subclasses de `li1.expression.ValorConcreto` (guardando `int`/`None`
  como valor), o que faz `ExpEquals`/`ExpNot` funcionarem sem nenhuma
  alteracao -- inclusive para comparacoes tipo `this.prox == null`.
- **`Exemplo3` reproduz fielmente uma peculiaridade do material da
  disciplina**: o metodo `insere` sempre aloca um novo no-sentinela vazio
  apos gravar um valor, e `print` percorre ate esse sentinela e o imprime
  tambem -- por isso a saida de `Exemplo3`/`Exemplo4` inclui um `-100`
  residual ao final de cada `print()`. Esse comportamento e reproduzido
  tal como descrito nos slides, no mesmo espirito de preservar
  comportamentos (mesmo que "estranhos") ja adotado em `li1/Exemplo1.py`.

## Testando tudo

```bash
cd /home/tassopc/Downloads/projeto
for pkg in le1 le2 lf1; do python3 -m $pkg.Exemplo1; done
for pkg in li1 li2 loo1; do
  for i in 1 2 3 4; do python3 -m $pkg.Exemplo$i; done
done
```
