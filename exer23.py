"""LUCAS DAVI"""
notas = [0, 0, 0, 0, 0]

for i in range(5):
    notas[i] = float(input(f"Insira a nota {i+1}: "))


print("\nNotas inseridas:")
for i in range(5):
    print(f"Nota {i+1}: {notas[i]}")

