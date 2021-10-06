/*
 * author:	anky
 * date:	12th April, 2021.
 * desc:	First easy script to anaylyse using radare2 in CSC 442
 * 		Reverse Engineering lecture.
 */

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string attempt;	// declare string to store attempt
    for (;;)		// infinite loop
    {
	cout << "Enter the password:\t";
	cin >> attempt;
	if (attempt.compare("0&v10u$") == 0)	// compare attempt with password
	{
	    cout << endl << "SUCCESS" << endl;
	    break;	// break out if you got the password right.
	}
	else
	    cout << endl << "FAILURE" << endl;
    }
    return 0;
}
