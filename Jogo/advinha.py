import random
print("Jogo de Adivinhação")
print("Tente adivinhar o número que estou pensando de 1 a 100")
print ("Você tem 7 tentativas para acertar o número secreto")
numero_secreto = random.randint(1,100)
contador = 7
acertou = False
while contador > 0:
    tentativa = int(input("Digite seu palpite "))
    contador -= 1
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True
        break
    elif tentativa < numero_secreto:
        print("O número secreto é maior que o seu palpite.")
    else:
        print("O número secreto é menor que o seu palpite.")

if not acertou:
    print("Que pena! Você errou. O número secreto era: ", numero_secreto)
else:
    print ("Você acertou em ", 7 - contador,"tentativas!")