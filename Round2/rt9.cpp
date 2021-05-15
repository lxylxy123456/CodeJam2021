#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int R, C, F, S;
		cin >> R >> C >> F >> S;
		vector<vector<char>> A, B;
		for (int i = 0; i < R; i++) {
			A.push_back({});
			for (int j = 0; j < C; j++) {
				char c;
				cin >> c;
				A[i].push_back(c);
			}
		}
		for (int i = 0; i < R; i++) {
			B.push_back({});
			for (int j = 0; j < C; j++) {
				char c;
				cin >> c;
				B[i].push_back(c);
			}
		}
		int ans = 0;
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

