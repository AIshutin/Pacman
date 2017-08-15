#include <iostream>
#include <time.h>
#include <vector>

using namespace std;

vector<int> v;

int main() {
	clock_t t = clock();
	for (int i = 0; i < 1000000; i++) {
		v.push_back(i);
	}
	cout << clock() - t << endl;
	return 0;
}