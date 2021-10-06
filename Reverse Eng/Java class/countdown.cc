//#define WINDOWS

#include <iostream>
#ifndef WINDOWS
	#include <unistd.h>
#else
	#include <windows.h>
#endif
using namespace std;

string obfuscate(string password)
{
	for (int i=0; i<password.length()/2; i++)
	{
		char t = password[i];
		password[i] = password[password.length() - i - 1];
		password[password.length() - i - 1] = t;
	}

	return password;
}

int main()
{
	int cycle = 2000000;

	cout << "COUNTDOWN: ";
	while (cycle > 0)
	{
		cout << cycle << "," << flush;
#ifndef WINDOWS
		usleep(1000 * 1000);
#else
		Sleep(1000);
#endif
		cycle--;
	}
	cout << "0\n";
	// c1c1c55407e1b2695e6cf49710b18774
	cout << "The password is " << obfuscate("47781b01794fc6e5962b1e70455c1c1c") << endl;
}
