"""LUCAS DAVI"""
num = 0

while num >=1 or num < 8 :
    num = int(input("Digite um número (1 a 7): "))
    if 1 <= num <= 7:
        if num == 1:
            print("Domingo")
        elif num == 2:
            print("Segunda-feira")
        elif num == 3:
            print("Terça-feira")
        elif num == 4:
            print("Quarta-feira")
        elif num == 5:
            print("Quinta-feira")
        elif num == 6:
            print("Sexta-feira")
        elif num == 7:
            print("Sábado")
    else:
        print("Número fora do intervalo. Tente novamente.")
