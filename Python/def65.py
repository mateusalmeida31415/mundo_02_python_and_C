class ConjutoNumeros:

    def __init__(self, quantidade, maior, menor, numeros, media):
        self.maior = menor
        self.menor = menor
        self.numeros = []
        self.quantidade = 0
        self.media = 0

    def resultado(self):
        self.set_maior()
        self.set_menor()
        self.set_quantidade()
        self.set_media()
        print(f'Maior número do conjunto: {self.get_maior()}')
        print(f'Menor número do conjunto: {self.get_menor()}')
        print(f'Quantidade de números digitados {self.get_quantidade()}')
        print(f'Média dos números: {self.get_media()}')

    def get_maior(self):
        return self.maior

    def set_maior(self):
        self.maior = max(self.numeros)

    def get_menor(self):
        return self.menor
    
    def set_menor(self):
        self.menor = min(self.numeros)

    def get_numeros(self):
        return self.numeros
    
    def set_numeros(self, n):
        self.numeros.append(n)

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self):
        self.quantidade = len(self.numeros)
    
    def get_media(self):
        return self.media
    
    def set_media(self):
        self.media = sum(self.numeros)/self.quantidade


def linha():
    print('=-'*30)

def titulo():
    linha()
    print('#### Analisando um conjunto de números ####')
    linha()

n = ConjutoNumeros(0, 0, 0, 0, 0)
opc = 'sim'
cont = 1

titulo()

while(opc == 'sim'):
    
    num = int(input(f'Digite o {cont}° número: '))
    n.set_numeros(num)
    cont += 1
    opc = str(input('Deseja continuar (sim ou não): ')).lower()

n.resultado()


