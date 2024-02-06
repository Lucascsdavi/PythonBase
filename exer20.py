"""LUCAS DAVI"""
total = 0
cont = 0
preco = float(input("Insira o preço do produto (insira valor negativo ou zero para encerrar): "))

while preco > 0:
    total += preco
    cont += 1
    preco = float(input("Insira o preço do próximo produto (insira valor negativo ou zero para encerrar): "))

print(f"\nTotal: R${total:.2f}")
print(f"Número de artigos: {cont}")

