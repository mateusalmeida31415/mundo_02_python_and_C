maiorPeso = menorPeso = 0

def linha():

	print("=-"*40)

def titulo():

	print("#### Analise pesos de pessoas de um grupo ####")

def obtemValores():

	global maiorPeso, menorPeso

	for i in range(0, 5):
		peso = float(input(f"Digite o valor do peso da {i + 1}° pessoa: "))
		linha()
		if(i == 0):
			maiorPeso = peso
			menorPeso = peso

		analisePeso(peso)	

def analisePeso(peso):

	global maiorPeso, menorPeso

	if(peso >= maiorPeso):
		maiorPeso = peso
	if(peso < menorPeso):
		menorPeso = peso

def resultado():

	print(f"Pessoa com maior peso do conjunto: {maiorPeso}")
	print(f"Pessoa com menor peso do conjunto: {menorPeso}")
	linha()


titulo()
obtemValores()
resultado()