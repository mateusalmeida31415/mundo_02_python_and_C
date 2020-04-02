#include <iostream>
#include <iomanip>
using namespace std;

// valor de cada prestação

float prestacao(float vacal, int tp){
	return vacal/(tp*12); 
}

// mensalidade em relação ao salário

float relacao(float sal, float pr){
	return (pr*100)/sal;
}

int main()
{
	float vacal, sal, pr, rl;
	int tp;

	cout << "Entre com o valor da casa que será adiquirida pelo cliente: R$ ";
	cin >> vacal;
	cout << "Entre com o valor do salário do cliente: R$ ";
	cin >> sal;
	cout << "Em quantos anos o cliente pretente quitar sua divida: ";
	cin >> tp;

	//status do emprestimo

	pr = prestacao(vacal, tp);
	rl = relacao(sal, pr);

	//Exibe os resultados com notação de ponto e com duas casas decimais 

	cout << fixed << setprecision(2);

	//Status do emprestimo
	
	if (rl < 30.0)
	{
		cout << "Valor de cada prestação: R$ " << pr << "\n";
		cout << "O valor da prestação relativo ao salário: " << rl << "%\n";
		cout << "Emprestimo autorizado!\n";

	}else{
		cout << "Valor de cada prestação: R$" << pr << "\n";
		cout << "O valor da prestação relativo ao salário: " << rl << "% \n";
		cout << "Emprestimo negado!\n";
	}

	return 0;
}