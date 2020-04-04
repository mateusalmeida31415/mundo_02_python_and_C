
#calcula a média da notas
def media():
	return (n1 + n2)/2

#Cria uma linha para separar o conteúdo
def linha():
	print("+-"*20)

#Retorna a situação do aluno
def situacao(m):
	if(m < 5):
		print("O aluno foi reprovado.")
	elif(m >= 5 and m <= 6.9):
		print("O Aluno terá que fazer uma prova final.")
	else:
		print("Aluno reprovado.")

linha()
print("#### Calcule a nota de um aluno ####")
linha()
n1 = float(input("Entre com a primeira nota do aluno: "))
linha()
n2 = float(input("Entre com a outra nota do aluno: "))
linha()

print(f"A média do alunos foi: {media():.2f}")

situacao(media())



