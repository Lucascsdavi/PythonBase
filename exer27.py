"""LUCAS DAVI"""
valores = [0, 0, 0, 0, 0]

for i in range(5):
    valores[i] = float(input(f"Insira o valor {i+1}: "))


print("\nValores inseridos:")
for i in range(5):
    print(f"Valor {i+1}: {valores[i]}")


elemento_pesquisado = float(input("\nDigite o valor a ser pesquisado: "))

encontrado = False
for i in range(5):
    if valores[i] == elemento_pesquisado:
        print(f"O valor {elemento_pesquisado} foi encontrado na posição {i+1}.")
        encontrado = True
        break

if not encontrado:
    print(f"O valor {elemento_pesquisado} não foi encontrado no vetor.")
