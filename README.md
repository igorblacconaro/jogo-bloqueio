# 🎮 Jogo do Bloqueio

Um jogo de estratégia em Python desenvolvido com base no conceito de movimentação em tabuleiro e bloqueio de caminhos.

O projeto foi desenvolvido originalmente como parte de uma **entrega acadêmica da disciplina de "Computation Thinking Using Python"**, com o objetivo de aplicar conceitos fundamentais da linguagem na construção de uma aplicação interativa.

Além do contexto acadêmico, o projeto foi estruturado de forma a demonstrar conceitos que podem ser aplicados em projetos reais, como organização em funções, validação de entradas, manipulação de matrizes, estruturas de dados e implementação de regras de negócio.

---

## 🧩 Sobre o jogo

O **Jogo do Bloqueio** é uma disputa entre dois jogadores em um tabuleiro de **7 × 7 posições**.

Cada jogador começa em um lado oposto do tabuleiro e possui um objetivo:

* 🔵 **Jogador A:** chegar à última coluna do lado direito.
* 🔴 **Jogador B:** chegar à primeira coluna do lado esquerdo.

Durante sua vez, o jogador pode:

1. Mover seu peão uma casa;
2. Colocar uma barreira;
3. Encerrar o jogo.

O diferencial está na utilização das barreiras. Elas podem dificultar o caminho do adversário, porém **não podem bloquear completamente o caminho de nenhum dos jogadores**.

Cada jogador possui **5 barreiras disponíveis** durante a partida.

### 🏆 Condição de vitória

O jogador vence quando seu peão alcança o lado oposto do tabuleiro.

```text
Jogador A → → → → → → 🏆
Jogador B ← ← ← ← ← ← 🏆
```

---

# ⚙️ Funcionalidades

O código foi dividido em funções, mantendo cada responsabilidade separada para facilitar a leitura, manutenção e evolução do projeto.

### 🗺️ Criação do tabuleiro

A função `criarMatriz()` cria o tabuleiro utilizando uma **matriz bidimensional**, preenchendo inicialmente todas as posições com `.`.

```python
tabuleiro = criarMatriz(tamanho)
```

O tamanho utilizado atualmente é:

```text
7 × 7
```

---

### 👥 Posicionamento dos jogadores

A função `posicionarJogadores()` posiciona automaticamente os jogadores no centro das extremidades do tabuleiro.

Além da posição, o dicionário de jogadores armazena informações como:

* linha;
* coluna;
* quantidade de barreiras disponíveis.

Exemplo:

```python
"A": {
    "linha": linha,
    "coluna": 0,
    "barreiras": 5
}
```

---

### 🚶 Movimentação

O jogador pode movimentar seu peão em quatro direções:

* ⬆️ Cima
* ⬇️ Baixo
* ⬅️ Esquerda
* ➡️ Direita

A função `obterNovaPosicao()` calcula a nova posição, enquanto `validarMovimento()` verifica se ela está dentro dos limites do tabuleiro e disponível para movimentação.

---

### 🧱 Sistema de barreiras

As barreiras ocupam duas posições consecutivas do tabuleiro.

Elas podem ser colocadas em duas orientações:

* Horizontal;
* Vertical.

Antes de uma barreira ser confirmada, o código verifica:

* se as posições escolhidas estão dentro do tabuleiro;
* se as posições estão livres;
* se a orientação escolhida é válida;
* se o jogador ainda possui barreiras disponíveis;
* se a barreira não elimina o caminho possível de nenhum jogador.

---

### 🧠 Validação de caminhos

Uma das principais regras do jogo é impedir que um jogador fique completamente bloqueado.

Para isso, a função `existeCaminho()` percorre as posições disponíveis do tabuleiro e verifica se existe alguma rota entre a posição atual do jogador e seu objetivo.

Quando uma barreira é criada, o sistema realiza a seguinte verificação:

```text
             Nova barreira
                   ↓
          ┌────────────────┐
          │ Verifica A     │
          │ Verifica B     │
          └───────┬────────┘
                  ↓
       Ambos possuem caminho?
            ↙             ↘
          SIM             NÃO
           ↓               ↓
     Mantém barreira    Remove barreira
```

Dessa forma, uma barreira considerada inválida é automaticamente removida.

---

### 🏁 Verificação de vitória

A função `verificarVitoria()` verifica se o jogador alcançou a extremidade correspondente ao seu objetivo.

Quando isso acontece, o jogo é encerrado e o vencedor é apresentado no terminal.

---

### 🛡️ Validação de entradas

O projeto utiliza `try/except` para tratar entradas inválidas do usuário.

Isso evita que valores como textos sejam capazes de interromper a execução do programa quando uma entrada numérica é esperada.

O sistema também valida opções fora dos intervalos permitidos.

---

# 🎮 Como jogar

## 1. Inicie o programa

Execute o arquivo Python pelo terminal:

```bash
python nome_do_arquivo.py
```

O tabuleiro será apresentado no terminal.

---

## 2. Identifique os jogadores

No início da partida:

* `A` representa o Jogador A;
* `B` representa o Jogador B;
* `.` representa uma posição livre;
* `🧱` representa uma barreira.

Exemplo:

```text
    1 2 3 4 5 6 7
1 | . . . . . . .
2 | . . . . . . .
3 | . . . . . . .
4 | A . . . . . B
5 | . . . . . . .
6 | . . . . . . .
7 | . . . . . . .
```

---

## 3. Escolha uma ação

A cada turno, o menu apresenta:

```text
1 - Mover peão
2 - Colocar barreira
3 - Sair
```

### Mover peão

Escolha `1` e depois informe uma direção:

```text
1 - Cima
2 - Baixo
3 - Esquerda
4 - Direita
```

O movimento só será realizado se a posição escolhida for válida.

---

### Colocar barreira

Escolha `2`.

Depois informe:

1. A linha;
2. A coluna;
3. A orientação da barreira.

Orientações disponíveis:

```text
1 - Horizontal
2 - Vertical
```

A barreira só será colocada se:

* as posições estiverem disponíveis;
* estiver dentro dos limites do tabuleiro;
* o jogador ainda possuir barreiras;
* a colocação não bloquear completamente o caminho de nenhum jogador.

Cada jogador começa com **5 barreiras**.

---

## 4. Alcance o objetivo

O objetivo é atravessar o tabuleiro e chegar à extremidade oposta.

### Jogador A

Começa no lado esquerdo e precisa alcançar a **coluna 7**.

### Jogador B

Começa no lado direito e precisa alcançar a **coluna 1**.

O primeiro jogador a alcançar seu objetivo vence a partida. 🏆

---

# 🧱 Regras resumidas

| Regra                    | Descrição                         |
| ------------------------ | --------------------------------- |
| 📐 Tabuleiro             | 7 × 7                             |
| 👥 Jogadores             | 2                                 |
| 🚶 Movimento             | Uma casa por turno                |
| 🧭 Direções              | Cima, baixo, esquerda e direita   |
| 🧱 Barreiras             | Horizontal ou vertical            |
| 🔢 Barreiras por jogador | 5                                 |
| 🚫 Bloqueio total        | Não permitido                     |
| 🏆 Vitória               | Alcançar o lado oposto            |
| 🚪 Saída                 | O jogador pode encerrar a partida |

---

# 🛠️ Conceitos utilizados

O desenvolvimento do projeto envolveu diferentes conceitos fundamentais de Python:

* Variáveis e constantes;
* Estruturas condicionais;
* Laços `for` e `while`;
* Funções com parâmetros e retornos;
* Listas;
* Listas de listas;
* Dicionários;
* Tuplas;
* Manipulação de matrizes;
* Entrada de dados com `input()`;
* Tratamento de exceções com `try/except`;
* Validação de dados;
* Regras de negócio;
* Algoritmo de busca de caminhos.

A organização em funções também permite que diferentes partes do jogo sejam desenvolvidas e testadas de maneira independente.

---

# 📁 Organização da lógica

De forma simplificada, o fluxo principal do projeto pode ser representado assim:

```text
                 ┌──────────────┐
                 │    main()    │
                 └──────┬───────┘
                        │
               ┌────────▼────────┐
               │ Criar tabuleiro │
               └────────┬────────┘
                        │
               ┌────────▼─────────┐
               │ Posicionar       │
               │ jogadores        │
               └────────┬─────────┘
                        │
                 ┌──────▼──────┐
                 │ Loop do jogo│
                 └──────┬──────┘
                        │
             ┌──────────┴──────────┐
             │                     │
       ┌─────▼─────┐         ┌─────▼──────┐
       │ Movimentar│         │  Barreira  │
       │ jogador   │         │            │
       └─────┬─────┘         └─────┬──────┘
             │                     │
             │              ┌──────▼──────┐
             │              │existeCaminho│
             │              └──────┬──────┘
             │                     │
             └──────────┬──────────┘
                        │
                 ┌──────▼──────┐
                 │ Verifica    │
                 │ vitória     │
                 └─────────────┘
```

---

⭐ **Projeto desenvolvido em Python como parte de uma experiência acadêmica e prática de desenvolvimento de software.**
