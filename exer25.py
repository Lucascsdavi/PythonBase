"""LUCAS DAVI"""
notas = [0, 0, 0, 0, 0]
soma = 0
positivos = 0
negativos = 0

for i in range(5):
    notas[i] = float(input(f"Insira a nota {i+1}: "))
    soma += notas[i]

print("\nNotas inseridas:")
for i in range(5):
    print(f"Nota {i+1}: {notas[i]}")
    if notas[i] > 0:
        print("positivo\n")
    else:
        print("negativo\n")

for nota in notas:
    if nota > 0:
        positivos += 1
    elif nota < 0:
        negativos += 1
print(f"Foram :{positivos} positivos \nForam :{negativos} Negativos")