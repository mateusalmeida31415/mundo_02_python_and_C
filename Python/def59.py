def linha():
    print("=-"*30)

def titulo():
    linha()
    print('#### Realize um das operações ####')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    linha()

def userOpcao():
    opc = int(input('>> '))
    opc = validaOpcao(opc)
    acao(opc)

def userValue():
    linha()
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    linha()

    return n1, n2

def validaOpcao(opc):
    while(opc <= 0 or opc > 5):
        opc = int(input('Erro! Digite novamente: '))

    return opc    

def acao(op):
    if(op == 1):
        soma()
    elif(op == 2):
        multiplicao()
    elif(op == 3):
        maior()
    elif(op == 4):
        titulo()
        userOpcao()
    elif(op == 5):
        sair()

def soma():
    n1, n2 = userValue()
    print(f'A soma entre {n1} e {n2} é: {n1+n2}')
    linha()

def multiplicao():
    n1, n2 = userValue()
    print(f'A multiplicação entre {n1} e {n2} é: {n1*n2}.')
    linha()

def maior():
    n1, n2 = userValue()
    if(n1 > n2):
        print(f'{n1} é maior que {n2}.')
        linha()
    else:
        print(f'{n2} é maior que {n1}.')
        linha()

def sair():
    linha()
    print('Volte sempre!')
    linha()


titulo()
userOpcao()
