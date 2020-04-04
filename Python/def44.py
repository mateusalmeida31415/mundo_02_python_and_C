#Cria linhas entre os conteudos
def linha():
	print("=-"*20)

def titulo():

	linha()
	print("#### Cálculo do desconto ####")
	linha()

def menu():

	print("Escolha uma forma de pagamento:")
	print("[1] À vista  no cartão: 5% de desconto;")
	print("[2] 2x no cartão: preço normal;")
	print("[3] 3x ou mais no cartão: 20% de juros;")
	print("[4] À vista/dinheiro: 10% de desconto.")

def verificaOpcao(opc):

	while(opc <= 0 or opc > 4):
		opc = int(input("Erro! Digite umas das opções acima: "))

	return opc

def calculoPreco(op, pr):

	if(op == 1):
		return pr*0.95
	elif (op == 2):
		return pr;
	elif (op == 3):
		return pr*1.2
	else: 
		return pr*0.9
 
def resultadoFinal(total):

	print(f"O total que irá pagar é: R$ {total:.2f}")

def main():

	titulo()
	menu()
	linha()
	opcao = int(input(">> "))
	linha()
	opcao = verificaOpcao(opcao)	
	preco = float(input("Preço do produto: R$ "))
	linha()
	resultadoFinal(calculoPreco(opcao, preco))


main()

