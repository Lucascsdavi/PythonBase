"""LUCAS DAVI"""
p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o segundo valor: "))
p3 = int(input("Digite o terceiro valor: "))
p4 = int(input("Digite o quarto valor: "))

maior1 = 0
maior2 = 0
maior3 = 0
"""......................................................."""
if p1 > maior1:
    maior3 = maior2
    maior2 = maior1
    maior1 = p1
elif p1 > maior2:
    maior3 = maior2
    maior2 = p1
elif p1 > maior3:
    maior3 = p1
"""......................................................."""
if p2 > maior1:
    maior3 = maior2
    maior2 = maior1
    maior1 = p2
elif p2 > maior2:
    maior3 = maior2
    maior2 = p2
elif p2 > maior3:
    maior3 = p2
"""......................................................."""
if p3 > maior1:
    maior3 = maior2
    maior2 = maior1
    maior1 = p3
elif p3 > maior2:
    maior3 = maior2
    maior2 = p3
elif p3 > maior3:
    maior3 = p3
"""......................................................."""
if p4 > maior1:
    maior3 = maior2
    maior2 = maior1
    maior1 = p4
elif p4 > maior2:
    maior3 = maior2
    maior2 = p4
elif p4 > maior3:
    maior3 = p4
"""......................................................."""

if maior1 == maior2 == maior3:
    print("todos os numeros sao iguais")
else:
    print(f"Os três maiores valores são: {maior1}, {maior2} e {maior3}")


