
#imprime linha para separar os texto
def linha():

	print("=-"*20)

#Calcula a idade de um atleta
def idade(an,niv ):

	if(niv == "sim"):
		return (2020 - an)
	else:
		return (2020 - an - 1)

#Retorna a categoria do atleta
def categoria(id):

	print(f"Sua idade: {id}")

	if(id <= 9):
		print(f"Categoria: Mirin.")
	elif(id > 9 and id <= 14):
		print(f"Categoria: Infantil.")
	elif(id > 14 and id <= 19):
		print(f"Categoria: Júnior.")
	elif(id > 19 and id <= 20):
		print(f"Categoria: Sênior.")
	else:
		print(f"Categoria: Máster.")


linha()
print("#### Categoria dos Atletas ####")
linha()

#Pergunta o usuário o ano em que ele nasceu
ano = int(input("Ano em que o atleta nasceu: "))
#Pergunta o usuário se ele já fez aniversário
niver = str(input("Esse atleta já fez aniversário: ")).lower()

categoria(idade(ano, niver))


