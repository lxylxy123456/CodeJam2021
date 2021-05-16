#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int Vertex(int a, int b) {
	return a * 100 + b;
}

const int BASE = 3000000;

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
		// e.g. 1
		// M G M G M G M G M G M G
		// G G-M G-M G-M G-M G-M M
		// G-M G-M G-M G-M G-M G-M
		// M G M G M G M G M G M G
		// e.g. 2
		// M G M G G G M M M M M G
		// M G M G G G M-M-M-M-M-G
		// M G M-G-G-G-G M M M M M
		// M-G-G G G G M M M M M M
		// G G M G G G M M M M M M
		int G_count = 0, M_count = 0;
		set<int> _S, _T;
		map<int, map<int, int>> c;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (A[i][j] == B[i][j])
					continue;
				if (A[i][j] == 'G') {
					G_count += 1;
					_T.insert(Vertex(i, j));
					continue;
				}
				_S.insert(Vertex(i, j));
				M_count += 1;
				for (int k = 0; k < R; k++) {
					for (int l = 0; l < C; l++) {
						if (A[k][l] == B[k][l])
							continue;
						if (A[k][l] == A[i][j])
							continue;
						int dist = abs(k - i) + abs(l - j);
						int s = Vertex(i, j), t = Vertex(k, l);
						// c[s][t] = BASE - min(dist * S, 2 * F);
						c[s][t] = min(dist * S, 2 * F);
					}
				}
			}
		}
		// https://en.wikipedia.org/wiki/Hungarian_algorithm
		map<int, int> y;
		set<pair<int, int>> oGy;
		for (auto i : _S)
			for (auto j : _T)
				oGy.insert({i, j});
		while (true) {
			// let R S ⊆ S and R T ⊆ T be the vertices not covered by M (so R S
			// consists of the vertices in S with no incoming edge and R T
			// consists of the vertices in T with no outgoing edge).
			set<int> RS(_S), RT(_T);
			for (auto e : oGy) {
				if (RS.find(e.second) != RS.end())
					RS.erase(e.second);
				if (RT.find(e.first) != RT.end())
					RT.erase(e.first);
			}
			// Let Z be the set of vertices reachable in G y from R S by a
			// directed path only following edges that are tight.
			set<int> Z;
			set<int> fringe(RS);
			map<int, set<int>> Gy;
			map<int, int> parent;
			for (auto e : oGy) {
				int cost;
				if (_S.find(e.first) != _S.end()) {
					cost = c[e.first][e.second];
				} else {
					cost = c[e.second][e.first];
				}
				if (y[e.first] + y[e.second] == cost)
					Gy[e.first].insert(e.second);
			}
			while (fringe.size()) {
				int i = *fringe.begin();
				fringe.erase(i);
				Z.insert(i);
				for (auto j : Gy[i])
					if (Z.find(j) == Z.end()) {
						fringe.insert(j);
						parent[j] = i;
					}
			}
			// If R T ∩ Z is nonempty, then reverse the orientation of a
			// directed path in G y from R S to R T. Thus the size of the
			// corresponding matching increases by 1.
			set<int> RTnZ;
			set_intersection(RT.begin(), RT.end(), Z.begin(), Z.end(),
								inserter(RTnZ, RTnZ.end()));
			if (RTnZ.size()) {
				int a = *RTnZ.begin();
				while (RS.find(a) == RS.end()) {
					int b = parent[a];
					assert(oGy.find({b, a}) != oGy.end());
					oGy.erase({b, a});
					oGy.insert({a, b});
					a = b;
				}
			} else {
				// If R T ∩ Z is empty, then let Δ := ...
				set<int> ZnS, T_Z, ZnT;
				set_intersection(Z.begin(), Z.end(), _S.begin(), _S.end(),
									inserter(ZnS, ZnS.end()));
				set_difference(_T.begin(), _T.end(), Z.begin(), Z.end(),
								inserter(T_Z, T_Z.end()));
				set_intersection(Z.begin(), Z.end(), _T.begin(), _T.end(),
									inserter(ZnT, ZnT.end()));
				int delta = BASE;
				for (int i : ZnS) {
					for (int j : T_Z) {
						delta = min(delta, c[i][j] - y[i] - y[j]);
					}
				}
				if (delta >= BASE) {
					break;
				}
				// Increase y by Δ on the vertices of Z ∩ S and decrease y by Δ
				// on the vertices of Z ∩ T.
				for (int i : ZnS) {
					y[i] += delta;
				}
				for (int j : ZnT) {
					y[j] -= delta;
				}
			}
		}
		int total_flow = 0;
		for (auto i : _S)
			for (auto j : _T)
				if (oGy.find({j, i}) != oGy.end()) {
					total_flow += c[i][j];
				}
		if (!"print graph") {
			std::cout << '\t';
			for (auto j : _T) {
				std::cout << j << '\t';
			}
			std::cout << '\n';
			for (auto i : _S) {
				std::cout << i << '\t';
				for (auto j : _T) {
					if (oGy.find({j, i}) != oGy.end()) {
						std::cout << "\033[31m";
					}
					std::cout << c[i][j] << '\t';
					std::cout << "\033[0m";
				}
				std::cout << '\n';
			}
			for (auto e : oGy) {
				std::cout << e.first << '\t' << e.second << std::endl;
			}
		}
		int ans = abs(G_count - M_count) * F + \
			total_flow;
			// min(G_count, M_count) * BASE - total_flow;
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

