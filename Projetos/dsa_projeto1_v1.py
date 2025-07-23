# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

import random  # Biblioteca usada para fazer sorteios aleatórios
from os import system, name  # Usada para identificar o sistema operacional e limpar a tela

# Função para limpar a tela a cada rodada (Windows ou Linux/Mac)
def limpa_tela():
    if name == 'nt':  # Se o sistema for Windows
        _ = system('cls')
    else:  # Se for Linux ou Mac
        _ = system('clear')

# Função principal do jogo
def game():
    
    limpa_tela()  # Limpa a tela antes de começar o jogo
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de possíveis palavras que podem ser sorteadas
    palavras = ['banana', 'abacaxi', 'uva', 'morango', 'laranja']
    
    # Sorteia uma palavra aleatoriamente da lista
    palavra = random.choice(palavras)
    
    # Cria uma lista com "_" para representar as letras ainda não descobertas
    letras_descobertas = ['_' for letra in palavra]
    
    chances = 6  # Número de tentativas permitidas
    letras_erradas = []  # Lista para guardar letras que o jogador errou
    
    # Loop que continua enquanto o jogador ainda tiver chances
    while chances > 0:
        
        # Mostra as letras já descobertas separadas por espaço
        print(" ".join(letras_descobertas))
        
        # Mostra quantas chances ainda restam
        print("\nChances restantes:", chances)
        
        # Mostra as letras que o jogador já tentou e errou
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Solicita uma letra ao jogador
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Verifica se a letra está na palavra
        if tentativa in palavra:
            # Substitui o "_" pela letra correta nos lugares certos
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            # Se a letra não estiver na palavra, perde uma chance
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Verifica se o jogador acertou todas as letras
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break  # Sai do loop, jogo encerrado
    
    # Se ainda sobrar "_" significa que o jogador perdeu
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco principal - garante que o jogo rode apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em python com a DSA.")