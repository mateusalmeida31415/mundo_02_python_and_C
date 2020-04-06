def titulo():
	print("=-"*40)
	print("### Soma de todos os números impares multuplos de três entre 0 e 500")
	print("=-"*40)

def calcula():
	for i in range(1, 501):
		if(i % 2 != 0 and i % 3 == 0):
			print(i)

titulo()
calcula()