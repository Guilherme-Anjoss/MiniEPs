impedimento = 0
peso = float(input())
idade = int(input())
if 16 <= idade < 18:
    autorizacao = str(input())    
boasaude = str(input())
usodedrogas = str(input())
primeiradoacao = str(input())
if primeiradoacao == "N":
    ultimadoacao = int(input())
    ultimos12meses = int(input())
sexo = str(input())
if sexo == "F":
    gravidez = str(input())
    amamentando = str(input())
    if amamentando == "S":
        idadedobebe = int(input())

print(f"Peso: {peso}")
print(f"Idade: {idade}")
if 16 <= idade < 18:
    print(f"Documento de autorizacao: {autorizacao}")
print(f"Boa saude: {boasaude}")
print(f"Uso drogas injetaveis: {usodedrogas}")
print(f"Primeira doacao: {primeiradoacao}")
if primeiradoacao == "N":
    print(f"Meses desde ultima doacao: {ultimadoacao}")
    print(f"Doacoes nos ultimos 12 meses: {ultimos12meses}")
print(f"Sexo biologico: {sexo}")
if sexo == "F":
    print(f"Gravidez: {gravidez}")
    print(f"Amamentando: {amamentando}")
    if amamentando == "S":
        print(f"Meses bebe: {idadedobebe}")

if peso < 50:
    impedimento += 1
    print("Impedimento: abaixo do peso minimo.")
if idade < 16:
    impedimento += 1
    print("Impedimento: menor de 16 anos.")
if 16 <= idade < 18:
    if autorizacao == "N":
        impedimento += 1
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if idade > 60:
    if primeiradoacao == "S":
        impedimento += 1
        print("Impedimento: maior de 60 anos, primeira doacao.")
if idade > 69:
    impedimento += 1
    print("Impedimento: maior de 69 anos.")
if boasaude == "N":
    impedimento += 1
    print("Impedimento: nao esta em boa saude.")
if usodedrogas == "S":
    impedimento += 1
    print("Impedimento: uso de drogas injetaveis.")
if sexo == "F":
    if primeiradoacao == "N":
        if ultimadoacao < 3:
            impedimento += 1
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        if ultimos12meses >= 3:
            impedimento += 1
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    if gravidez == "S":
        impedimento += 1
        print("Impedimento: gravidez.")
    if amamentando == "S":
        if idadedobebe < 12:
            impedimento += 1
            print("Impedimento: amamentacao.")
if sexo == "M":
    if primeiradoacao == "N":
        if ultimadoacao < 2:
            impedimento += 1
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        if ultimos12meses >= 4:
            impedimento += 1
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if impedimento == 0:
    print("Procure um hemocentro.")
