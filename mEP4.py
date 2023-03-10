def ConversTempo(tempo):
    hora = tempo // 60
    minuto = tempo % 60
    return hora, minuto

def TempoCorredor(tempo, sexo):
    hora, minuto = ConversTempo(tempo)
    if sexo == 'm' or sexo == 'M':
        return f'Tempo do corredor: {hora:02d}h {minuto:02d}min'
    else:
        return f'Tempo da corredora: {hora:02d}h {minuto:02d}min'    

def Indice(tempo, idade, sexo):
    if 18 <= idade <= 34:
            indiceMin = 180
    elif 35 <= idade <= 39:
            indiceMin = 185
    elif 40 <= idade <= 44:
            indiceMin = 190
    elif 45 <= idade <= 49:
            indiceMin = 200
    elif 50 <= idade <= 54:
            indiceMin = 205
    elif 55 <= idade <= 59:
            indiceMin = 215
    elif 60 <= idade <= 64:
            indiceMin = 230
    elif 65 <= idade <= 69:
            indiceMin = 245
    elif 70 <= idade <= 74:
            indiceMin = 260
    elif 75 <= idade <= 79:
            indiceMin = 275
    elif idade >= 80:
            indiceMin = 290  

    if sexo == "f" or sexo == "F":
        indiceMin += 30

    tempoHora, tempoMin = ConversTempo(indiceMin)
    print(f'Tempo necessario: {tempoHora:02d}h {tempoMin:02d}min')

    DiferencaTempo = indiceMin - tempo
    DiferencaTempo_pos = abs(DiferencaTempo)
    if DiferencaTempo >= 0:
        print("Conseguiu indice? SIM")
        hora, minuto = ConversTempo(DiferencaTempo)
        if sexo == "f" or sexo == "F":
            print(f"A corredora correu {hora:02d}h {minuto:02d}min abaixo do indice")
        else:
            print(f"O corredor correu {hora:02d}h {minuto:02d}min abaixo do indice")
    else:
        print("Conseguiu indice? NAO")
        hora, minuto = ConversTempo(DiferencaTempo_pos)
        if sexo == "f" or sexo == "F":
             print(f"A corredora correu {hora:02d}h {minuto:02d}min acima do indice")
        else:
             print(f"O corredor correu {hora:02d}h {minuto:02d}min acima do indice")

def main():
    tempo = int(input())
    idade = int(input())
    sexo = input()
    print(TempoCorredor(tempo, sexo))
    Indice(tempo, idade, sexo)

main()

 
   
 
     


