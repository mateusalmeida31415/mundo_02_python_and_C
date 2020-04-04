
#Adicionar linhas para separar o conteudo
def linha():
	print("=-"*20)

#Calcula o índice de massa corporea
def imc(p, alt):
	return p/(alt**2)

#Retorna a categoria dos dados do usuário de acordo com imc
def status(imc):
	if(imc <= 18.5):
		print("Abaixo do peso.")
	elif(imc > 18.5 and imc <= 25.0):
		print("Peso ideal.")
	elif(imc > 25.0 and imc <= 30.0):
		print("Sobre peso.")
	elif(imc > 30.0 and imc <= 40.0):
		print("Obesidade.")
	else:
		print("Obesidade mórbida.")


linha()
print("#### Calcule o seu IMC ####")
linha()

#Obetem do usuário o valor do seu peso e a sua altura
peso = float(input("Qual é o seu peso: "))
linha()
altura = float(input("Qual é a sua altura: "))
linha()

status(imc(peso, altura))
linha()



