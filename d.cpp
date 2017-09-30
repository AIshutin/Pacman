#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int main() {
	vector<int> a;
	int n;
	cin >> n;
	a.resize(n);
	for (int i = 0; i < n; i++) cin >> a[i];
	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int c, a1, b;
		cin >> c >> a1 >> b;
		if (c == 0) {
			int mn = 1e9 + 100;
			int mn_i = -1;
			for (int j = a1 - 1; j < b; j++) {
				if (a[j] < mn) {
					mn = a[j];
					mn_i = j;
				}
			}
			cout << mn << " " << mn_i + 1 << endl; 
		} else {
			a[a1 - 1] = b;
		}
	}
	return 0;	
}