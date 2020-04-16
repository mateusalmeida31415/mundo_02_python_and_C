def linha():
    print('=-'*40)

def titulo():
    linha()
    print('#### Analise númerica ####')
    linha()

def user():
    opc = 'sim'
    n = []
    c = 1
    somaTotal = 0
    while(opc == 'sim'):
        n = int(input('Digite um número: '))
        opc = str(input('Deseja digitar outro número? [sim] ou [não]')).lower()
        somaTotal += n
        if(opc == 'sim'):
            c += 1

        print(f'Soma total: {somaTotal}')
        print(f'Maior número: {max(n)}')
        print(f'Menor número: {min(n)}')
        print(f'Média: {(somaTotal/c):.2f}')
        print(f'Total de números: {c}')

titulo()
user()
            
    
