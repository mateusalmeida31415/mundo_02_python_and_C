#include <iostream>
using namespace std;

// valor de cada prestação

float prestacao(float vacal, int tp){
	return vacal/(tp*12); 
}

// mensalidade em relação ao salário

float relacao(float sal, float pr){
	return (pr(*100)/sal;
}

int main()
{
	float vacal, sal, pr, rl;
	int tp;

	cout << "Entre com o valor da casa que será adiquirida pelo cliente: R$ ";
	cin >> vc;
	cout << "Entre com o valor do salário do cliente: R$ ";
	cin >> sal;
	cout << "Em quantos anos o cliente pretente quitar sua divida: ";
	cin >> tp;

	//status do emprestimo

	pr = prestacao(vacal, tp);
	rl = relacao(sal, pr);

	if (rl < 30.0)
	{
		cout << "Valor de cada prestação: R$" << pr;
		cout << "O valor da prestação relativo ao salário: " << rl << "%";
		cout << "Emprestimo autorizado!";

	}else{
		cout << "Valor de cada prestação: R$" << pr;
		cout << "O valor da prestação relativo ao salário: " << rl << "%";
		cout << "Emprestimo negado!";
	}

	return 0;
}