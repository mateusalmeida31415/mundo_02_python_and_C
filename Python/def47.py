def titulo():
	print("=-"*40)
	print("###### Todos os números pares de 0 até 50 ######")
	print("=-"*40)

def calPares():
	for i in range(0, 51):
		if(i % 2 == 0):
			print(i)

titulo()
calPares()