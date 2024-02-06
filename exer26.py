"""LUCAS DAVI"""
nomes = ["", "", "", "", ""]
notas = [0, 0, 0, 0, 0]
positivos = 0
negativos = 0

for i in range(5):
    nomes[i] = input(f"Insira o nome {i+1}: ")
    notas[i] = float(input(f"Insira a nota para {nomes[i]}: "))

print("\nElementos inseridos:")
for i in range(5):
    print(f"Nome {i+1}: {nomes[i]}, Nota: {notas[i]}")
    if notas[i] > 0:
        print("Nota positiva\n")
    else:
        print("Nota negativa\n")

for nota in notas:
    if nota > 0:
        positivos += 1
    elif nota < 0:
        negativos += 1

print(f"\nForam {positivos} notas positivas.")
print(f"Foram {negativos} notas negativas.")
