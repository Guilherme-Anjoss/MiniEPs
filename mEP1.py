x = float(input())
y = float(input())
if x > 0 and y > 0:
    quadrante = "I"
elif x > 0 and y < 0:
    quadrante = "IV"
elif x < 0 and y > 0:
    quadrante = "II"
elif x < 0 and y < 0:
    quadrante = "III"
else:
    quadrante = "EIXOS"
print(quadrante)