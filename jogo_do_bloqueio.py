'''

== Integrantes ==
    Igor Blacconaro Santos - RM572033
    Andrew Rodrigues Lima da Silva - RM573777
    Bryan Costa Silva - RM569439
    Luis Henrique Rondão Mendonça - RM569797

== Proposta do jogo ==
    O Projeto foi baseado em um jogo de tabuleiro chamado "bloqueio", a ideia do jogo consiste em que cada jogador chegue ao lado do inimigo. Contudo cada jogador possuira 5 barreiras e o usuário deve escolher entre se mover ou atrapalhar a locomoção do rival de forma estratégica!

'''

def criarMatriz(tamanho: int):
    '''
    Cria o tabuleiro do jogo com base em um tamnho que é passado por parãmetro, utilizando "." para sinalizar as posições que estarão disponíveis.
    '''
    tabuleiro = []

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(".")
        tabuleiro.append(linha)
    return tabuleiro

def posicionarJogadores(tabuleiro: list):
    '''
    Posiciona os jogadores "A" no meio e esquerda da matriz, e o jogador "B" no meio e direita da mesma.
    Salva as informações de posição dos jogadores dentro de um dicionário de jogadores, contendo as chaves, linha e coluna, dentro de cada jogador.
    '''
    tamanho = len(tabuleiro)

    linha = tamanho // 2

    tabuleiro[linha][0] = "A"
    tabuleiro[linha][tamanho - 1] = "B"

    jogadores = {
        "A": {
            "linha": linha,
            "coluna": 0,
            "barreiras": 5
        },
        "B": {
            "linha": linha,
            "coluna": tamanho - 1,
            "barreiras": 5
        }
    }
    return jogadores

def exibirTabuleiro(tabuleiro: list):
    '''
    Função que faz uma impressão personalizada da matriz do jogo, com posições de linha e coluna alinhadas a seus respectivos valores.
    '''
    tamanho = len(tabuleiro)

    print("\n    ", end="")

    for coluna in range(tamanho):
        print(coluna + 1, end=" ")

    print()

    for linha in range(tamanho):
        print(f"{linha + 1} |", end=" ")
        for coluna in range(tamanho):
            print(tabuleiro[linha][coluna], end=" ")
        print()

def validarMovimento(tabuleiro: list, nova_linha: int, nova_coluna: int):
    '''
    Faz a validação se uma linha/coluna pode ser ocupada na hora de uma jogada do usuário.
    '''
    tamanho = len(tabuleiro)

    if nova_linha < 0 or nova_linha >= tamanho:
        return False

    if nova_coluna < 0 or nova_coluna >= tamanho:
        return False

    if tabuleiro[nova_linha][nova_coluna] != ".":
        return False

    return True

def obterNovaPosicao(linha: int, coluna: int, direcao: int):
    '''Função responsável por definir aonde será a nova jogada do usuário.
    1- Cima
    2- Baixo
    3- Esquerda
    4- Direita
    '''
    nova_linha = linha
    nova_coluna = coluna

    if direcao == 1:
        nova_linha -= 1

    elif direcao == 2:
        nova_linha += 1

    elif direcao == 3:
        nova_coluna -= 1

    elif direcao == 4:
        nova_coluna += 1

    return nova_linha, nova_coluna

def movimentarJogador(tabuleiro: list, jogadores: dict, jogador: str, direcao: int):
    '''
    Realiza a movimentação do jogador com base na direção recebida.
        - obtem a posição nova da jogada utilizando a função "obterNovaPosicao".
        - valida a posição disponível com função "validarMovimento".
        - atualiza o tabuleiro, com a nova posição e transformando a anitga em uma posição vazia.
    '''

    linha = jogadores[jogador]["linha"]
    coluna = jogadores[jogador]["coluna"]

    nova_linha, nova_coluna = obterNovaPosicao(
        linha,
        coluna,
        direcao
    )

    if not validarMovimento(tabuleiro, nova_linha, nova_coluna):
        print("Movimento inválido!")
        return False

    tabuleiro[linha][coluna] = "."
    tabuleiro[nova_linha][nova_coluna] = jogador

    jogadores[jogador]["linha"] = nova_linha
    jogadores[jogador]["coluna"] = nova_coluna

    return True

def escolherDirecao():
    '''
    Realiza a entrada da direção desejada do usuário.
        - valida erros de digitação.
    '''
    while True:
        print("\n1- Cima")
        print("2- Baixo")
        print("3- Esquerda")
        print("4- Direita")

        try:
            direcao = int(input("\nEscolha uma opção: "))
            if direcao < 1 or direcao > 4:
                raise Exception("\nEscolha uma opção entre 1 e 4.")
        except ValueError:
            print("\nDigite penas números.")
        except Exception as erro:
            print(erro)
        else:
            break
    return direcao

def verificarVitoria(jogadores: dict, jogador: str, tamanho: int):
    '''
    Verifica se um jogador venceu a partida e retorna um True para finalizar o jogo.
    '''

    coluna = jogadores[jogador]["coluna"]

    if jogador == "A" and coluna == tamanho - 1:
        return True
    if jogador == "B" and coluna == 0:
        return True

    return False

def colocarBarreira(tabuleiro: list, jogadores: dict, jogador: str):
    '''
    Responsável por fazer as validações da posição da barreira desejada pelo usuário.
    '''
    tamanho = len(tabuleiro)

    if jogadores[jogador]["barreiras"] == 0:
        print("\nVocê não possui mais barreiras!")
        return False
    #escolha da linha e coluna da barreira
    while True:
        try:
            linha = int(input("\nInforme o número da linha para adicionar a barreira: ")) - 1
            coluna = int(input("\nInforme o número da coluna para adicionar a barreira: ")) - 1
            if linha < 0 or linha >= tamanho:
                raise Exception("\nLinha inválida!")
            if coluna < 0 or coluna >= tamanho:
                raise Exception("\nColuna inválida!")
        except ValueError:
            print("\nDigite apenas números.")
        except Exception as erro:
            print(erro)
            return False
        else:
            break

    #escolha da orienação da barreira
    print("\n1- Horizontal")        
    print("2- Vertical")
    while True:
        try:
            orientacao = int(input("\nInforme a orientação da barreira: "))
            if orientacao < 1 or orientacao > 2:
                raise Exception("\nOrientação inválida!")
        except ValueError:
            print("\nDigite apenas números.")
            return False
        except Exception as erro:
            print(erro)
            return False
        else:
            break

    if orientacao == 1:
        #Horizontal
        segunda_linha = linha
        segunda_coluna = coluna + 1
    else:
        #Vertical
        segunda_linha = linha + 1
        segunda_coluna = coluna

    #verifica se a segunda posição esta dentro do tabuleiro 
    if segunda_linha >= tamanho or segunda_coluna >= tamanho:
        print("\nA barreira ultrapassa o limite do tabuleiro!")
        return False
    
    # Verifica se as duas posições estão livres
    if tabuleiro[linha][coluna] != ".":
        print("\nA primeira posição já está ocupada!")
        return False
    if tabuleiro[segunda_linha][segunda_coluna] != ".":
        print("\nA segunda posição já está ocupada!")
        return False

    #colocar a barreira
    tabuleiro[linha][coluna] = "#" 
    tabuleiro[segunda_linha][segunda_coluna] = "#"

    caminho_a = existeCaminho(
    tabuleiro,
    jogadores["A"]["linha"],
    jogadores["A"]["coluna"],
    "A"
    )

    caminho_b = existeCaminho(
    tabuleiro,
    jogadores["B"]["linha"],
    jogadores["B"]["coluna"],
    "B"
    )

    if not caminho_a or not caminho_b:
        # Remove a barreira
        tabuleiro[linha][coluna] = "."
        tabuleiro[segunda_linha][segunda_coluna] = "."

        print("\nBarreira inválida! Ela bloqueia o caminho de um jogador.")
        return False

    jogadores[jogador]["barreiras"] -= 1
    print("\nBarreira colocada com sucesso!")
    print(f"Barreiras restantes: {jogadores[jogador]["barreiras"]}")
    return True

def existeCaminho(tabuleiro: list, inicio_linha: int, inicio_coluna: int, jogador: str):
    '''
    Verifica se um caminho é válido ou inválido.
    '''
    tamanho = len(tabuleiro)

    # Lista de posições que ainda precisam ser verificadas
    fila = [(inicio_linha, inicio_coluna)]

    # Guarda as posições que já foram verificadas
    visitados = []

    while len(fila) > 0:

        linha, coluna = fila.pop(0)

        # Evita verificar a mesma posição novamente
        if (linha, coluna) in visitados:
            continue

        visitados.append((linha, coluna))

        # Verifica se o jogador chegou ao objetivo
        if jogador == "A" and coluna == tamanho - 1:
            return True

        if jogador == "B" and coluna == 0:
            return True

        # Possíveis movimentos: cima, baixo, esquerda e direita
        movimentos = [
            (-1, 0),  # cima
            (1, 0),   # baixo
            (0, -1),  # esquerda
            (0, 1)    # direita
        ]

        for movimento in movimentos:

            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]

            # Verifica se está dentro do tabuleiro
            if (nova_linha >= 0 and nova_linha < tamanho and
                    nova_coluna >= 0 and nova_coluna < tamanho):

                # Pode passar somente por casas vazias ou pela posição do jogador
                if (tabuleiro[nova_linha][nova_coluna] == "." or
                        tabuleiro[nova_linha][nova_coluna] == jogador):

                    if (nova_linha, nova_coluna) not in visitados:
                        fila.append((nova_linha, nova_coluna))

    # Se todas as possibilidades foram verificadas
    # e o objetivo não foi encontrado
    return False


def main():
    '''
    Função principal, onde ocorre a chamada de todas as outras funções.
    '''
    tamanho = 7

    tabuleiro = criarMatriz(tamanho)
    jogadores = posicionarJogadores(tabuleiro)

    jogador_atual = "A"
    jogo_ativo = True

    while jogo_ativo:
        exibirTabuleiro(tabuleiro)

        print(f"\nVez do jogador {jogador_atual}")
        print("1 - Mover peão")
        print("2 - Colocar barreira")
        print("3 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            direcao = escolherDirecao()

            movimentou = movimentarJogador(
                tabuleiro,
                jogadores,
                jogador_atual,
                direcao
            )

            if movimentou:
                if verificarVitoria(
                    jogadores,
                    jogador_atual,
                    tamanho
                ):
                    exibirTabuleiro(tabuleiro)
                    print(f"\nJogador {jogador_atual} venceu!")
                    jogo_ativo = False
                else:
                    if jogador_atual == "A":
                        jogador_atual = "B"
                    else:
                        jogador_atual = "A"

        elif opcao == 2:
            colocou_barreira = colocarBarreira(tabuleiro, jogadores, jogador_atual)
            if colocou_barreira:
                if jogador_atual == "A":
                    jogador_atual = "B"
                else:
                    jogador_atual = "A"

        elif opcao == 3:
            print("Jogo encerrado.")
            jogo_ativo = False

        else:
            print("Opção inválida!")

#chamada do main()
main()
