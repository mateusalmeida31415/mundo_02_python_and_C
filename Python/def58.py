from random import randint
from time import sleep

def linha():
    print("=-"*40)

def titulo():
    linha()
    print("#### Jogo de adivinhação ####")
    linha()

def maquinaEscolha():

    numeroGerado = randint(1, 10)
    return numeroGerado

def usuario():

    print("Pensei em um número entre 1 e 10, agora você deve adivinhar.")
    linha()
    minhaEscolha = int(input("Sua vez: "))
    sleep(1)
    linha()
    return minhaEscolha

def tentativas(minhaEscolha, numeroGerado):

    minhasTentativas = 1
    while(numeroGerado != minhaEscolha):
        minhaEscolha = int(input("Você errou! Tente outro número: "))
        sleep(1)
        linha()
        minhasTentativas += 1

    resultadoFinal(minhasTentativas, numeroGerado)

def resultadoFinal(minhasTentativas, numeroGerado):
    
    print("Parabéns, você acertou!")
    print(f"Número escolhido pela máquina: {numeroGerado}")
    print(f"Número de tentativas: {minhasTentativas}")
    linha()

titulo()
tentativas(usuario(), maquinaEscolha())