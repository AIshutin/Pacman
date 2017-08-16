#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <array>
#include <random>
#include <set>
#include <queue>

using namespace std;

int length, width, MinDistPlayers, n, c, a, sorry;
char packman, wall, apple, cherry, food;
ofstream saves;
vector< vector <string> > mods;
vector<vector<int > > map1;
queue <array<int, 2> > queque;
map<array<int, 2>, int> dist;
vector<string> GameField2;
vector< vector<string> > antimods;
vector< vector< string> > symm;
vector<array<int, 2> > players;
int APPLE;
int PACKMAN;

vector<string> make_symm(vector<string> arr) { // Funcion to make gamefield symmetrical
	int n = arr.size();
	int m = arr[0].size();
	vector<string> brr;
	brr.resize(n);
	for (int i = 0; i < n; i++) {
		brr[i].resize(m);
		for (int j = 0; j < m; j++)
			brr[i][j] = arr[i][m - j - 1];
	}
	return brr;
}

void CalcDist(array<int, 2> start) { //Function for calculating distance from one point to all. Bfs
	dist.clear();
	dist[start] = 0;
	while (queque.size() != 0) queque.pop();
	queque.push(start);
	array<int, 2> var;
	var[0] = -1;
	var[1] = 1;
	int i = 0;
	while (queque.size() > 0) {
		for (int i1 = 0; i1 < 2; i1++) {
			for (int j1 = 0; j1 < 2; j1++) {
				int i2 = queque.front()[0];
				int j2 = queque.front()[1];
				if (j1 % 2 == 0) i2 += var[i1];
				else j2 += var[i1];
				array<int, 2> curr;
				curr[0] = i2;
				curr[1] = j2;
				if (i2 < length && i2 >= 0 && j2 < width && j2 >= 0 && GameField2[i2][j2] != wall && dist.find(curr) == dist.end()) {
					dist[queque.front()];
					dist[curr] = dist[queque.front()] + 1;
					queque.push(curr);
				}
			}
		}
		queque.pop();
		i++;
	}
}

bool IsConnected() { //Checking if is possible to move from any point to any
	int n = 0;
	int i1 = -1;
	int j1 = -1;
	for (int i = 0; i < length; i++) {
		for (int j = 0; j < width; j++) {
			if (GameField2[i][j] != wall) {
				i1 = i;
				j1 = j;
				n += 1;
			}
		}
	}
	array<int, 2> z;
	z[0] = i1;
	z[1] = j1;
	CalcDist(z);
	if (dist.size() != n) return false;
	return true;
}

void GenField() { //Function that generates gamefields
	for (int i = 0; i < map1.size(); i++) {
		for (int j = 0; j < (map1[i].size() / 2); j++) {
			int q = rand() % mods.size();
			map1[i][j] = q;
			map1[i][map1[0].size() - j - 1] = -q - 1;
		}
		if (map1[0].size() % 2) {
			map1[i][map1[0].size() / 2] = rand() % symm.size();
		}
	}
}

bool PlaceApples(int a, char apple, int deep) { // Fuction that places apples
	if (deep >= APPLE) return false;
	int cnt = 0;
	vector<array<int, 2> > apples;
	while (cnt != a) {
		int x = rand() % width;
		int y = rand() % length;
		if (GameField2[y][x] == food) {
			GameField2[y][x] = apple;
			array<int, 2> curr;
			curr[0] = y;
			curr[1] = x;
			apples.push_back(curr);
			cnt += 1;
		}
		else continue;
	}
	//Check if it`s fair
	bool log = false;
	int last = -1;
	for (int i = 0; i < n; i++) {
		CalcDist(players[i]);
		int summ = 0;
		for (int j = 0; j < a; j++) {
			array<int, 2> curr;
			curr[0] = apples[j][0];
			curr[1] = apples[j][1];
			summ += dist[curr];
		}
		if (last == -1) last = summ;
		if (last != summ) {
			for (int i = 0; i < GameField2.size(); i++)
				for (int j = 0; j < GameField2[i].size(); j++)
					if (GameField2[i][j] == apple) GameField2[i][j] = food;
			return PlaceApples(a, apple, deep + 1);
		}
	}
	return true;
}

bool GenField2(int deep) { //Function that places object on gamefield
	if (deep >= PACKMAN) return false;
	int cnt = 0;
	//Place Packmen
	players.clear();
	while (cnt != n) {
		int x = rand() % width;
		int y = rand() % length;
		if (GameField2[y][x] == food) {
			GameField2[y][x] = packman;
			array<int, 2> z;
			z[0] = y;
			z[1] = x;
			players.push_back(z);
			cnt += 1;
		}
		else continue;
	}
	//Check if you have done this fair]
	int last = -1;
	bool log = true;
	for (int i = 0; i < n; i++) {
		CalcDist(players[i]);
		int summ = 0;
		for (int j = 0; j < n; j++) {
			if (dist.find(players[j]) == dist.end() || (dist[players[j]] != 0 && dist[players[j]] < MinDistPlayers)) {
				log = false;
				break;
			}
			summ += dist[players[j]];
		}
		if (!log) break;
		if (last == -1) last = summ;
		if (last != summ) log = false;
	}
	//if not -> try again
	if (!log) {
		for (int i = 0; i < GameField2.size(); i++)
			for (int j = 0; j < GameField2[i].size(); j++)
				if (GameField2[i][j] == packman) GameField2[i][j] = food;
		return GenField2(deep + 1);
	}
	//else place apples/cherry
	//apples
	if (!PlaceApples(a, apple, deep)) return false;
	if (!PlaceApples(c, cherry, deep)) return false;
	return true;
}

//working with user;
/**
void write13(ofstream file, vector<string> GameField) { //Function that writes gamefield to file
	for (int i = 0; i < width + 2; i++) file << wall;
	file << endl;
	for (int i = 0; i < length; i++) {
		file << wall;
		for (int j = 0; j < width; j++) file << GameField[i][j];
		file << wall << endl;
	}
	for (int i = 0; i < width + 2; i++) file << wall;
	file << endl << endl;
}**/

set<string> positive;

void unarchive() { //Fuction that makes from list of modules normal gamefield
	GameField2.clear();
	GameField2.resize(length);
	for (int i = 0; i < length; i++) GameField2[i].resize(width);
	for (int i = 0; i < map1.size(); i++)
		for (int j = 0; j < map1[i].size(); j++) {
			if (j * 2 + 1 == map1[i].size()) {
				for (int i1 = i * 3; i1 < i * 3 + 3; i1++)
					for (int j1 = j * 3; j1 < j * 3 + 3; j1++) {
						//cout << "Bug1 " << i << " " << j << " " << i1 << " " << j1 << " " << endl;
						map1[i][j];
						//cout << "@" << endl;
						symm[map1[i][j]];
						//cout << "#" << symm.size() << " " << map1[i][j] << endl;
						symm[map1[i][j]][i1 - i * 3];
						//cout << "%" ;
						//cout << symm[map1[i][j]][i1 - i * 3].size() << endl;
						symm[map1[i][j]][i1 - i * 3][j1 - j * 3];
						//cout << "^" << endl;
						GameField2[i1][j1] = symm[map1[i][j]][i1 - i * 3][j1 - j * 3];
					}
			}
			else if (map1[i][j] >= 0) {
				for (int i1 = i * 3; i1 < i * 3 + 3; i1++)
					for (int j1 = j * 3; j1 < j * 3 + 3; j1++) {
						//cout << "Bug2" << endl;
						GameField2[i1][j1] = mods[map1[i][j]][i1 - i * 3][j1 - j * 3];
					}
			}
			else {
				map1[i][j]++;
				map1[i][j] *= -1;
				for (int i1 = i * 3; i1 < i * 3 + 3; i1++)
					for (int j1 = j * 3; j1 < j * 3 + 3; j1++) {
						//cout << "Bug3" << endl;
						GameField2[i1][j1] = antimods[map1[i][j]][i1 - i * 3][j1 - j * 3];
					}
			}
		}
}

int main() {
	//getting conditions of game field
	ifstream settings("settings.txt");
	ifstream modules("data.gm");
	//ifstream pos("positive.txt");
	string pm, wl, ap, ch, fd, saves;
	settings >> length >> width >> MinDistPlayers >> n >> c >> a >> pm >> wl >> ap >> ch >> fd >> saves;
	packman = pm[0];
	wall = wl[0];
	apple = ap[0];
	cherry = ch[0];
	food = fd[0];
	settings.close();

	int numb;
	modules >> numb;
	//Downloading modules
	for (int i = 0; i < numb; i++) {
		string line1, line2, line3;
		modules >> line1 >> line2 >> line3;
		vector <string> curr;
		curr.push_back(line1);
		curr.push_back(line2);
		curr.push_back(line3);
		for (int q = 0; q < 3; q++)
			for (int j = 0; j < curr[q].size(); j++) {
				if (curr[q][j] == '.') curr[q][j] = food;
				if (curr[q][j] == '0') curr[q][j] = wall;
			}
		mods.push_back(curr);
		vector<string> z = make_symm(curr);
		antimods.push_back(z);
		bool log = true;
		for (int i = 0; i < curr.size(); i++)
			for (int j = 0; j < curr[i].size(); j++)
				if (curr[i][j] != z[i][j]) log = false;
		if (log) symm.push_back(z);
	}
	modules.close();
	/**set<string> positive;
	int num;
	pos >> num;
	for (int i = 0; i < num; i++) {
		string z;
		pos >> z;
		positive.insert(z);
	}
	pos.close();**/
	ofstream fout(saves);
	map1.resize(length / 3);
	//Magic. If you don`t afraid headache change cosntant and observe what will happend. You`ll be amazed.
	if (length == 15 && width == 15) {
		APPLE = 300;
		PACKMAN = 200;
	}
	else if (length == 21 && width == 21) {
		APPLE = 300;
		PACKMAN = 200;
	}
	else if ((length == 21 && width == 24) || (length == 24 && width == 21)) {
		APPLE = 700;
		PACKMAN = 500;
	}
	else if ((length == 27 && width >= 24) || (length >= 24 && width == 27)) {
		APPLE = 1000;
		PACKMAN = 1000;
	}
	else {
		APPLE = 400;
		PACKMAN = 300;
	}

	for (int i = 0; i < map1.size(); i++)
		map1[i].resize(width / 3, -1);
	while (true) {
		GenField();
		unarchive();
		if (IsConnected()) {
			if (!GenField2(0)) continue;
			for (int i = 0; i < width + 2; i++) cout << wall;
			cout << endl;
			for (int i = 0; i < length; i++){
			cout << wall;
			for (int j = 0; j < width; j++) cout << GameField2[i][j];
			cout << wall << endl;
			}
			for (int i = 0; i < width + 2; i++) cout << wall;
			cout << endl << endl;
			/**string answer;
			cout << "Save it? ";
			cin >> answer;**/
			if (true) { /// positive.find(answer) != positive.end()
				for (int i = 0; i < width + 2; i++) fout << wall;
				fout << endl;
				for (int i = 0; i < length; i++) {
					fout << wall;
					for (int j = 0; j < width; j++) fout << GameField2[i][j];
					fout << wall << endl;
				}
				for (int i = 0; i < width + 2; i++) fout << wall;
				fout << endl << endl;
			}
			/**cout << "Continue work? ";
			cin >> answer;**/

			if (true) break; /// positive.find(answer) == positive.end()
							 ///cout << endl;
		}
	}
	fout.close();
	//cout << "Saves will stored in " << saves << "." << endl;
	return 0;
}
