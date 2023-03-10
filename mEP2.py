#Guilherme Lima dos Anjos o miserê da Bahia
a = int(input())
b = int(input())
c = int(input())
l1 = l2 = l3 = 1
if a >= b and a >= c:
    l1 = a
    if b >= c:
        l2 = b
        l3 = c
    else:
        l2 = c
        l3 = b
elif b >= a and b >= c:
    l1 = b
    if a >= c:
        l2 = a
        l3 = c
    else:
        l2 = c
        l3 = a
elif c >= a and c >= b:
    l1 = c
    if a >= b:
        l2 = a
        l3 = b
    else:
        l2 = b
        l3 = a
elif a == b and b == c:
    l1 = a
    l2 = b
    l3 = c
a = l1
b = l2
c = l3

if a <= 0 or b <= 0 or c <= 0:
    print("Valores invalidos.")
elif a >= b + c or b >= a + c or c >= a + b:
    print("Valores nao podem formar um triangulo.")
elif a == b == c:
    print("Triangulo equilatero.")
    if l1**2 < l2**2 + l3**2:
        print("Triangulo acutangulo.")
    elif l1**2 == l2**2 + l3**2:
        print("Triangulo retangulo.")
    elif l1**2 > l2**2 + l3**2:
        print("Triangulo obtusangulo.")
elif a == b != c or a == c != b or b == c != a:
    print("Triangulo isosceles.")
    if l1**2 < l2**2 + l3**2:
        print("Triangulo acutangulo.")
    elif l1**2 == l2**2 + l3**2:
        print("Triangulo retangulo.")
    elif l1**2 > l2**2 + l3**2:
        print("Triangulo obtusangulo.")
elif a != b != c:
    print("Triangulo escaleno.")
    if l1**2 < l2**2 + l3**2:
        print("Triangulo acutangulo.")
    elif l1**2 == l2**2 + l3**2:
        print("Triangulo retangulo.")
    elif l1**2 > l2**2 + l3**2:
        print("Triangulo obtusangulo.")