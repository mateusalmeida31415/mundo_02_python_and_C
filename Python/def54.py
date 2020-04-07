idmaior = idmenor = 0


def linha():

	print("=-"*40)

def titulo():

	linha()
	print("#### Analise de maioridade ####")
	linha()

def cadastro():

	for i in range(7):
		ano = int(input(f"Ano em que o {i+1}° cliente nasceu: "))
		niver = str(input("Ele já fez aniversario? ")).lower()
		status(ano, niver)

def status(ano, niver):

	global idmaior, idmenor

	if((2020 - ano) >= 18 and niver == "sim"):
		idmaior += 1
	elif((2020 - ano ) > 18 and niver != "sim"):
		idmaior += 1
	else: 
		idmenor += 1

def final():
	print(f"Quantidade de pessoas maiores de idade é: {idmaior}")
	print(f"Quantidade de pessoas menores de idade é: {idmenor}")
	

titulo()
cadastro()
final()

