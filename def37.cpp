#include <iostream>
using namespace std;

// Analisando os dois números

void analise (int n1, int n2){

	if (n1 > n2){
		cout << n1 << " é o maior. " << endl;
	}else if (n2 > n1){
		cout << n2 << " é o maior. " << endl;
	}
	else{
		cout << "Os dois números são iguais." << endl;
	}

}

int	main()
{
	int n1, n2;

	cout << "#### Analizando dois números ####" << endl;
	cout << "Digite um número: ";
	cin >> n1;
	cout << "Digite outro número: ";
	cin >> n2;

	cout << "#### Números digitados ####" << endl;
	cout << "Primeiro: " << n1 << endl;
	cout << "Segundo: " << n2 << endl;

	analise(n1, n2);

	return 0;
}