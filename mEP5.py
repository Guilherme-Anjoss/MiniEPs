######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP5 - Jogo da Velha
# Nome:Guilherme Lima dos Anjos
# Matrícula:2021201054
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################


def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} \n---+---+---\n {p4} | {p5} | {p6} \n---+---+---\n {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    cont = 0
    cont += 1 if p1 == " " or p1 == "x" or p1 == "o" else + 0
    cont += 1 if p2 == " " or p2 == "x" or p2 == "o" else + 0
    cont += 1 if p3 == " " or p3 == "x" or p3 == "o" else + 0
    cont += 1 if p4 == " " or p4 == "x" or p4 == "o" else + 0
    cont += 1 if p5 == " " or p5 == "x" or p5 == "o" else + 0
    cont += 1 if p6 == " " or p6 == "x" or p6 == "o" else + 0
    cont += 1 if p7 == " " or p7 == "x" or p7 == "o" else + 0
    cont += 1 if p8 == " " or p8 == "x" or p8 == "o" else + 0
    cont += 1 if p9 == " " or p9 == "x" or p9 == "o" else + 0
    if cont == 9:
        return True
    else:
        return False 

def contaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições e faz a contagem de jogadas do 'x'
    e do 'o' retornando o número de jogadas feitas.
    """
    contX = contO = 0
    contX += 1 if p1 == "x" else + 0
    contO += 1 if p1 == "o" else + 0
    contX += 1 if p2 == "x" else + 0
    contO += 1 if p2 == "o" else + 0
    contX += 1 if p3 == "x" else + 0
    contO += 1 if p3 == "o" else + 0
    contX += 1 if p4 == "x" else + 0
    contO += 1 if p4 == "o" else + 0
    contX += 1 if p5 == "x" else + 0
    contO += 1 if p5 == "o" else + 0
    contX += 1 if p6 == "x" else + 0
    contO += 1 if p6 == "o" else + 0
    contX += 1 if p7 == "x" else + 0
    contO += 1 if p7 == "o" else + 0
    contX += 1 if p8 == "x" else + 0
    contO += 1 if p8 == "o" else + 0
    contX += 1 if p9 == "x" else + 0
    contO += 1 if p9 == "o" else + 0   
    if contX == 0 and contO == 0:
        return 0, 0
    return contX, contO
    
def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    contX, contO = contaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if contX == 6 or contO == 6:
        return False
    elif (contX >= 5 and contO <= 3) or (contO == 5 and contX <= 3):
        return False
    elif (contX >= 4 and contO <= 2) or (contO >= 4 and contX <= 2):
        return False
    elif (contX >= 3 and contO <= 1) or (contO >= 3 and contX <= 1):
        return False
    elif (contX >= 2 and contO == 0) or (contO >= 2 and contX == 0):
        return False    
    else:
        return True

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    #Complete o código da função

    if (p1 == "x" and p2 == "x" and p3 == "x") or (p1 == "o" and p2 == "o" and p3 == "o"):
        if p1 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p4 == "x" and p5 == "x" and p6 == "x") or (p4 == "o" and p5 == "o" and p6 == "o"):
        if p4 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p7 == "x" and p8 == "x" and p9 == "x") or (p7 == "o" and p8 == "o" and p9 == "o"):
        if p7 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p1 == "x" and p4 == "x" and p7 == "x") or (p1 == "o" and p4 == "o" and p7 == "o"):
        if p1 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p2 == "x" and p5 == "x" and p8 == "x") or (p2 == "o" and p5 == "o" and p8 == "o"):
        if p2 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p3 == "x" and p6 == "x" and p9 == "x") or (p3 == "o" and p6 == "o" and p9 == "o"):
        if p3 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p1 == "x" and p5 == "x" and p9 == "x") or (p1 == "o" and p5 == "o" and p9 == "o"):
        if p1 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    elif (p3 == "x" and p5 == "x" and p7 == "x") or (p3 == "o" and p5 == "o" and p7 == "o"):
        if p3 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")   
    elif p1 == " " or p2 == " " or p3 == " " or p4 == " " or p5 == " " or p6 == " " or p7 == " " or p8 == " " or p9 == " ":
        print("O jogo nao terminou!")
    else:
        print("Empate!")

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
