class ConjutoNumeros:

    def __init__(self):
        self.soma = 0
        self.quantidade = 0
        self.numeros = []

    def construtora(self):
        self.set_quantidade()
        self.set_soma()

    def get_soma(self):
        return self.soma

    def set_soma(self):
        self.soma = sum(self.numeros)

    def get_quantidade(self):
        return self.quantidade
    
    def set_quantidade(self):
        self.quantidade = len(self.numeros)

    def get_numeros(self):
        return self.numeros

    def set_numeros(self, num):
        self.numeros.append(num)


n = ConjutoNumeros()

def linha():
    print('=-'*25)

def titulo():
    linha()
    print('#### Analisando números ####')
    linha()

def aviso():
    linha()
    print('#### Digite 999 para terminar ####')
    linha()


titulo()
aviso()

num = 0 
cont = 1

while(num != 999):
    num = int(input(f'Digite o {cont}° número: '))
    cont += 1
    if(num != 999):
        n.set_numeros(num)

n.construtora()
    
linha()
print(f'Quantidades de números digitados: {n.get_quantidade()}')
print(f'soma de todos os números digitados: {n.get_soma()}')
linha()