# Fiz certo, só conferir no github
import random
tentativas = 0
numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)
for c in range(3):
    chances = int(input('Informe um número entre 1 e 10: '))
    if numero_aleatorio != chances:
        print("Você errou, tente mais uma vez")
        tentativas += 1
        if tentativas >= 0:
            print('você gastou {} chances, de 3'.format(tentativas))
            if tentativas >= 3:    
                print('Você perdeu :(')
    else: 
        numero_aleatorio == chances
        print('Você adivinhou o número aleatório! ')