from time import sleep

def titulo():
	print("=-"*20)
	print("##### Contagem regressiva #####")
	print("=-"*20)


titulo()

for i in range(10, -1, -1):
	print(f"{i}! ")
	sleep(1)

print("BOOM!")