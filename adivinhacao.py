print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

chute = int(chute)

print("Você digitou", chute)

if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim de jogo")