"""LUCAS DAVI"""
max1 = 0
max2 = 0
max3 = 0
cont = 0
numero = 1

while numero > 0:

    numero = float(input("Insira um número positivo (insira o numero 0 para encerrar): "))
    if numero == 0:
        break

    cont += 1

    if numero > max1:
        max3 = max2
        max2 = max1
        max1 = numero
    elif numero > max2:
        max3 = max2
        max2 = numero
    elif numero > max3:
        max3 = numero

# Exibe o resultado
print(f"\nOs três maiores valores são: {max1}, {max2}, {max3}")
print(f"Número de valores lidos: {cont}")

