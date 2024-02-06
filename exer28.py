"""LUCAS DAVI"""
valores = [0, 0, 0, 0, 0]

for i in range(5):
    valores[i] = float(input(f"Insira o valor {i+1}: "))

print("\nValores inseridos:")
for i in range(5):
    print(f"Valor {i+1}: {valores[i]}")

for i in range(5):
    for j in range(0, 4 - i):
        if valores[j] > valores[j+1]:
            valores[j], valores[j+1] = valores[j+1], valores[j]


print("\nValores ordenados em ordem crescente:")
for i in range(5):
    print(f"Valor {i+1}: {valores[i]}")


for i in range(5):
    for j in range(0, 4 - i):
        if valores[j] < valores[j+1]:

            valores[j], valores[j+1] = valores[j+1], valores[j]


print("\nValores ordenados em ordem decrescente:")
for i in range(5):
    print(f"Valor {i+1}: {valores[i]}")
