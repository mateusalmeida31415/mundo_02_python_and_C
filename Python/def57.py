def linha():

    print("=-"*40)

def titulo():

    linha()
    print("#### Obtendo o sexo ####")
    linha()

def obtenha():

    sexo = str(input("Digite o seu sexo, [F] para feminino ou [M] para masculino: ")).lower()
    linha()
    if(sexo != 'f' and sexo != 'm'):
        sexo = validacao(sexo)

    return sexo

def validacao(sexo):
    
    while(sexo != 'f' and sexo != 'm'):
        sexo = str(input("Erro! Digite novamente(F ou M): "))
        linha()
    
    return sexo    

def resultadoFinal(s):

    if(s == 'f'):
        print("Seu sexo é Feminino.")
    else:
        print("Seu sexo é masculino.")

titulo()
resultadoFinal(obtenha())