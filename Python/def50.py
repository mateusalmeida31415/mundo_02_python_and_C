soma = 0

def linha():
	print("=-"*40)

def titulo():
	linha()
	print("#### Soma dos números pares ####")
	linha()

def usuario():
	for i in range(6):
		linha()
		n = int(input(f"Digite {i + 1}° número: "))
		linha()
		analise(n)

def analise(nums):
	global soma      # Esse é um ponto muito importante 
	if nums % 2 == 0:
		 soma += nums

def resultadoFinal():
	print(f"A Soma de todos os números pares: {soma}")


titulo()
usuario()
resultadoFinal()