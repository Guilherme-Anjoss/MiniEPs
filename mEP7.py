def Candidatos(numCandidatos, C = [["Brancos"]], i = 0):

    if i < numCandidatos:
       NomeCandidato = input()
       C = C[:]
       return Candidatos(numCandidatos, C + [[NomeCandidato]], i + 1)
       
    return C

def Votos(numVotos, Candidatos, i = 0, contNulo = 0):
    
    if i < numVotos:
        voto = int(input())
        if voto > len(Candidatos[1:]):
            return Votos(numVotos, Candidatos, i + 1, contNulo + 1)
        Candidatos = Candidatos[:]
        Candidatos[voto] = Candidatos[voto] + [voto]
        return Votos(numVotos, Candidatos, i + 1, contNulo)

    return Candidatos, contNulo

def resultado(Votaçao, VotoNulo, numCandidatos, maior = [], i = 1):

    if i == 1:
        print(f"{Votaçao[i][0]}: {len(Votaçao[i][1:])}")
        maior = maior[:]
        maior = Votaçao[i]
        return resultado(Votaçao, VotoNulo, numCandidatos, maior, i + 1)
    else:
        if i <= numCandidatos:
            print(f"{Votaçao[i][0]}: {len(Votaçao[i][1:])}")
            if len(Votaçao[i][1:]) > len(maior[1:]):
                maior = maior[:]
                maior = Votaçao[i]
                return resultado(Votaçao, VotoNulo, numCandidatos, maior, i + 1)
            else:
                return resultado(Votaçao, VotoNulo, numCandidatos, maior, i + 1)

    print(f"{Votaçao[0][0]}: {len(Votaçao[0][1:])}")
    print(f"Nulos: {VotoNulo}")
    print(f"Vencedor(a): {maior[0]}")    


def main():
    numCanditados = int(input())
    ListaCandidatos = Candidatos(numCanditados)
    numVotos = int(input())
    Votaçao, VotoNulo = Votos(numVotos, ListaCandidatos)
    resultado(Votaçao, VotoNulo, numCanditados)

main()