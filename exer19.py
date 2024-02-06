"""LUCAS DAVI"""
num = 0
while num >=1 or num <=1 :
    num = int(input("Digite um valor para saber se é negativo ou positivo: "))
    if num >= 0:
        print(f"O numero {num} é positivo\n")
    else:
        print(f"O numero {num} é negativo\n")
    if num == 0:
        print("Programa encerrado.")
        break

