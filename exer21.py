"""LUCAS DAVI"""
total = 0
cont = 0
preco = float(input("Insira o preço do produto (insira valor negativo ou zero para encerrar): "))

while preco > 0:
    total += preco
    cont += 1
    preco = float(input("Insira o preço do próximo produto (insira valor negativo ou zero para encerrar): "))

pag = float(input("Introduza o valor de pagamento: "))
print(f"\nTotal: R${total:.2f} e seu troco é de {pag-total}R$")
print(f"Número de artigos: {cont}")