def linha():
    print('=-'*30)

def titulo():
    linha()
    print('#### Digite 999 para sair. ####')
    linha()

def user():

    n1 = c = soma = 0
    while(n1 != 999):
        n1 = int(input(f'Digite o {c + 1}° número: '))
        if(n1 != 999):
            c += 1
            soma += n1
    
    resultado(soma, c)

def resultado(s, cont):
    linha()
    print(f'Quantidade de números digitados é: {cont}')
    print(f'Soma de todos os números é: {s}')
    linha()

titulo()
user()
