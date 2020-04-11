def linha():
    print("=-"*30)

def titulo():
    linha()
    print('#### Calculando o fatorial de um número ####')
    linha()

def user():
    n = int(input('Escolha um número: '))
    linha()
    fatorial(n)

def fatorial(n):
    fat = 1
    if(n == 0):
        print(f'O fatorial de {n} é 1.')
        linha()
    else: 
        for i in range(1,n + 1):
            fat *= i
        print(f'O fatorial de {n} é {fat}.')
        linha()

titulo()
user()
