def linha():

	print("=-"*40)

def titulo():

	linha()
	print("##### Verificação de números primos #####")
	linha()

def obtenha():

	num = int(input("Digite um número: "))
	print(f"{num} ", end="")

	return num

def verificaPrimo(num):

	primo = True

	for i in range(1, num + 1):
		if(num % i == 0 and i != 1 and i != num):
			primo = False
			break

	return primo

def resultado(statusNum):

	if(statusNum == True):
		print("é um número primo.")
	else:
		print("não é um número primo.")



titulo()
resultado(verificaPrimo(obtenha()))
