Lista = [["Jonas", 1, 1, 1, 1 ], ["Ana", 2, 2, 2], ["Mario", 3, 3]]
if len(Lista[0][1:]) > len(Lista[1][1:]):
    print(f"{Lista[0][0]} é o(a) vencedor(a)")
    print(f"Venceu com {len(Lista[0][1:])} votos")
else:
    print(f"{Lista[1][0]} é o(a) vencedor(a)")