def linha():
	print("=-"*40)

def titulo():
	linha()
	print("##### Calcule a taboada de qualquer número #####")
	linha()

def usuario():
	n = int(input("A taboada de qual valor você deseja calcular? "))
	linha()
	return n

def imprimeTaboada(valor):
	for i in range(11):
		print(f"{valor} x {i} = {valor*i}")


titulo()
imprimeTaboada(usuario())