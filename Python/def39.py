print("#### Qual  a sua situação militar ? ####")
ano = int(input("Digite o ano que você nasceu: "))
niver = str(input("Você já fez aniversário? ")).lower()

# Analise da idade do usuário 

def idade():
	if (niver == 'nao') or (niver == 'não'):
		return (2020 - ano - 1)
	else:
		return (2020 - ano)

# Situação militar

if idade() < 18:
	print(f"Sua idade: {idade()}")
	print("Você ainda não pode se alistar.")
elif idade() == 18:
	print(f"Sua idade: {idade()}")
	print("Você já pode se alistar.")
else:
	print(f"Sua idade: {idade()}")
	print("Você já deveria ter se alistado.")

