#include <iostream>
using namespace std;

int idade(string niver, int ano){
	if ((niver == "nao") or (niver == "não")){
		return (2020 - 1996 - 1);
	}else{
		return (2020 - 1996);
	}

}

void input(int idade){

	cout << "Sua idade: " << idade << endl;
	if (idade < 18){
		cout << "Você ainda não pode se alistar." << endl;
	}else if (idade == 18){
		cout << "Você já pode se alistar." << endl;
	}else{
		cout << "Você deve se alistar." << endl;
	}
}

int main()
{
	int ano;
	string niver;

	cout << "#### Você sabe a sua situação militar? ####" << endl;
	cout << "Digite o ano em que você nasceu: ";
	cin >> ano;
	cout << "Você já fez aniversário? ";
	cin >> niver;

	input(idade(niver, ano));

	return 0;
}