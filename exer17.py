"""LUCAS DAVI"""
num = 0
while num >=1 or num < 8 :
    num = int(input("Digite um número (1 a 7, ou 0 para sair): "))

    if num == 0:
        print("Programa encerrado.")
        break

    if 1 <= num <= 7:
        if num == 1:
            print("Domingo")
            print("Cinema")
        elif num == 2:
            print("Segunda-feira")
            print("música")
        elif num == 3:
            print("Terça-feira")
            print("passear")
        elif num == 4:
            print("Quarta-feira")
            print("corrida")
        elif num == 5:
            print("Quinta-feira")
            print("video games")
        elif num == 6:
            print("Sexta-feira")
            print("sushi")
        elif num == 7:
            print("Sábado")
            print("descanso")
    else:
        print("Opção inválida. Tente novamente.")
