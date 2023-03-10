######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP6 - Avatar: A Lenda de Aang
# Nome:Guilherme Lima dos Anjos
# Matrícula:2021201054
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional;
# - Você não pode usar variáveis globais;
# - Caso precise, você PODE criar outras funções;
# - Você PODE adicionar os parâmetros que achar 
#   necessários na função 'realizaTreinamentoAvatar'.
######################################################





def realizaTreinamentoAvatar(fogo = 0, agua = 0, ar = 0, terra = 0):
    """
    Função responsável pela leitura dos dados e cálculo da pontuação do treinamento do Avatar. 
    A função deve retornar True se o treinamento foi realizado com sucesso e False, caso contrário
    """
    e = input()
    if e != "FIM":
        p = int(input())
        if e == "FOGO":
            if agua >= p/2:
                agua -= p/2
            else:
                agua = 0
            return realizaTreinamentoAvatar(fogo + p, agua + 0, ar + 0, terra + 0)
        elif e == "AGUA":
            if fogo >= p/2:
                fogo -= p/2
            else:
                fogo = 0
            return realizaTreinamentoAvatar(fogo + 0, agua + p, ar + 0, terra + 0)
        elif e == "AR":
            if terra >= p/2:
                terra -= p/2
            else:
                terra = 0
            return realizaTreinamentoAvatar(fogo + 0, agua + 0, ar + p, terra + 0)
        elif e == "TERRA":
            if ar >= p/2:
                ar -= p/2
            else:
                ar = 0
            return realizaTreinamentoAvatar(fogo + 0, agua + 0, ar + 0, terra + p)
        else:
            return realizaTreinamentoAvatar(fogo + 0, agua + 0, ar + 0, terra + 0)
    else:
        if (agua > 0) and (terra > 0) and (fogo > 0) and (ar > 0):
            print(f"Pontuacao Final\nAgua: {agua:.1f}\nTerra: {terra:.1f}\nFogo: {fogo:.1f}\nAr: {ar:.1f}")
            return True
        else:
            print(f"Pontuacao Final\nAgua: {agua:.1f}\nTerra: {terra:.1f}\nFogo: {fogo:.1f}\nAr: {ar:.1f}")
            return False

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    treinamentoAvatar = realizaTreinamentoAvatar()
    if treinamentoAvatar == True:
        print("Treinamento realizado com sucesso.")
    elif treinamentoAvatar == False:
        print("Realize mais treinamentos.")
    else:
        print("ERRO: A implementação da função 'realizaTreinamentoAvatar' possui algum erro")

main()
