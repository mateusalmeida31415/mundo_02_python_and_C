from random import randint
from time import sleep

class Jogo():
    def __init__(self):
        self.vitorias = 0
        self.partidas = 0
        self.derrota = 0
    
    def getVitorias(self):
        return self.vitorias
    
    def setVitorias(self):
        self.vitorias += 1

    def getPartidas(self):
        return self.partidas

    def setPartidas(self):
        self.partidas += 1

    def getDerrota(self):
        return self.derrota

    def setDerrota(self):
        self.derrota += 1


parImpar = Jogo()

def linha():
    print('=-'*30)

def titulo():
    linha()
    print('#### Vamos jogar par ou impar? ####')
    print('#### Pensei em número, agora você tem que adivinhar se ele é par ou impar! ####')
    print('#### Se você errar o jogo termina, caso contrario continua até você errar. ####')
    print('#### Descubra o seu recorde!! ####')
    linha()

def main():

    while(parImpar.getDerrota() != 1):
        opc = str(input('Escolha uma opção, par ou impar: ')).lower().strip()
        if(opc != 'impar' and opc != 'par'):
            opc = validacao(opc)

        n = randint(0, 10)
        print('Processando...')
        sleep(1)
        print(f'Número escolhido pelo computador: {n}')
        linha()
        sleep(1)
        if(opc == 'par' and n % 2 == 0):
            parImpar.setVitorias()
        elif(opc == 'impar' and n % 2 != 0):
            parImpar.setVitorias()
        else:
            parImpar.setDerrota()

        parImpar.setPartidas()

def resultado():
    linha()
    print(f'Número de partidas: {parImpar.getPartidas()}')
    print(f'Número de vitórias: {parImpar.getVitorias()}')
    linha()

def validacao(op):
    linha()
    while(op != 'impar' and op != 'par'):
        op = str(input('Erro! Escolha par ou impar: '))

    linha()
    return op


titulo()
main()
resultado()


    
