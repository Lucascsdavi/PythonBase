"""LUCAS DAVI"""
p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o segundo valor: "))
p3 = int(input("Digite o terceir valor: "))

if p1 > p2 and p1 > p3:
    print(f"o valor {p1} é o maior valor")
elif p2 > p1 and p2 > p3:
    print(f"o valor {p2} é o maior valor")
elif p3 > p1 and p3 > p2:
    print(f"o valor {p3} é o maior valor")
else:
    print("todos o valores sao iguais")

if p1 < p2 and p1 < p3:
    print(f"o valor {p1} é o menor valor")
elif p2 < p1 and p2 < p3:
    print(f"o valor {p2} é o menor valor")
elif p3 < p1 and p3 < p2:
    print(f"O valor {p3} é o menor valor")

