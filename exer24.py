"""LUCAS DAVI"""
notas = [0, 0, 0, 0, 0]
contador = 0
soma = 0

for i in range(5):
    notas[i] = float(input(f"Insira a nota {i+1}: "))
    contador += 1
    soma += notas[i]

print("\nNotas inseridas:")
for i in range(5):
    print(f"Nota {i+1}: {notas[i]}")

if contador > 0:
    media = soma / contador
    print(f"\nMédia das notas: {media:.2f}")
else:
    print("Não há notas para calcular a média.")
