class GrupoPessoas:
    def __init__(self):
        self.numeroHomens = 0
        self.pessoasMaior18 = 0
        self.mulheresMenosDe20 = 0
        self.quantidadeTotal = 0

    def getQuantidadeTotal(self):
        return self.quantidadeTotal

    def setQuantidadeTotal(self, sex, id):
        
        if(sex == 'masculino'):
            self.setNumeroHomens()

        elif(sex == 'feminino' and id < 20):
            self.setMulheresMenoresDe20()

        if(id >= 18):
            self.setPessoasMaior18()

        self.quantidadeTotal += 1

    def getMulheresMenoresDe20(self):
        return self.mulheresMenosDe20

    def setMulheresMenoresDe20(self): 
            self.mulheresMenosDe20 += 1

    def getNumeroHomens(self):
        return self.numeroHomens

    def setNumeroHomens(self):
            self.numeroHomens += 1

    def getPessoasMaior18(self):
        return self.pessoasMaior18

    def setPessoasMaior18(self):
        self.pessoasMaior18 += 1

turma = GrupoPessoas()

def linha():
    print('=-'*30)

def titulo():
    linha()
    print('#### Analisando um grupo de pessoas ####')
    linha()

def main():
    opc = 'sim'
    c = 1
    while(opc == 'sim'):
        sexo = str(input(f'Qual é o sexo da {c}° pessoa, feminino ou masculino: ')).lower().strip()
        if(sexo != 'feminino' and sexo != 'masculino'):
            sexo = validacaoSexo(sexo)
        idade = int(input(f'Qual é a idade da {c}° pessoa: '))
        if(idade <= 0 or idade > 150):
            idade = validacaoIdade(idade)

        turma.setQuantidadeTotal(sexo, idade)
        c += 1
        opc = str(input('Deseja continuar [sim/não]: '))
        linha()

def validacaoSexo(s):
    while(s != 'feminino' and s != 'masculino'):
        s = str(input('Erro! Digite o sexo novamente: '))
    return s

def validacaoIdade(i):
    while(i <= 0 or i > 150):
        i = int(input('Erro! Digite a idade novamente: '))

    return i

def resultado():
    print(f'Número de homens: {turma.getNumeroHomens()}')
    print(f'Número de mulheres menores de 20 anos: {turma.getMulheresMenoresDe20()}')
    print(f'Número de pessoas maiores de 18 anos: {turma.getPessoasMaior18()}')
    linha()


titulo()
main()
resultado()