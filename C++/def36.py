caval = float(input("Entre com o valor da casa que será adiquirida pelo cliente: R$ "))
sal = float(input("Entre com o valor do sálario do cliente: R$ "))
tp = int(input("Em quantos anos o cliente pretente quitar sua divida: "))

#valor de cada parcela

def parcela():
	return caval/(tp*12)

#porcentagem do salário

def relativo():
	return parcela()*100/sal

#status do meprestimo


if(parcela() < sal*0.3):
	print(f"Valor de cada prestação: R$ {parcela():.2f}")
	print(f"O valor da prestação representa {relativo():.2f}% do sálario do cliente.")
	print("Emprestimo autorizado!")
else:
	print(f"Valor de cada prestação: R$ {parcela():.2f}")
	print(f"O valor da prestação representa {relativo():.2f}% do sálario do cliente.")
	print("O Emprestimo não pode ser autorizado!")
	
#fim

