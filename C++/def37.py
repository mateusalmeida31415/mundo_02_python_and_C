print("### Analizando dois números ###")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))



print("#### Números Digitados ####")
print(f"Primeiro: {n1}")
print(f"Segundo: {n2}")

#Analizando os dois números

if n1 > n2:
	print(f"O número maior é: {n1}")
elif n2 > n1:
	print(f"O número maior é {n2}")
else:
	print("O dois números são iguais.")


