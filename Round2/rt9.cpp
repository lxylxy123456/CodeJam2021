#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>

#include "FordFulkerson.hpp"

using namespace std;
using namespace algorithms;

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
		GraphAdjList<int> G(true);
		umap<Edge<int>, int, EdgeHash<int>> c;
		umap<Edge<int>, int, EdgeHash<int>> f;
		int G_count = 0, M_count = 0;
		int start = Vertex(-1, -1), end = Vertex(-1, -2);
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (A[i][j] == B[i][j])
					continue;
				int vij = Vertex(i, j);
				if (A[i][j] == 'G') {
					G_count += 1;
					G.add_edge(vij, end);
					c[Edge<int>{vij, end, true}] = BASE;
					continue;
				}
				M_count += 1;
				G.add_edge(start, vij);
				c[Edge<int>{start, vij, true}] = BASE;
				for (int k = 0; k < R; k++) {
					for (int l = 0; l < C; l++) {
						if (A[k][l] == B[k][l])
							continue;
						if (A[k][l] == A[i][j])
							continue;
						int dist = abs(k - i) + abs(l - j);
						int s = Vertex(i, j), t = Vertex(k, l);
						G.add_edge(s, t);
						std::cout << s << '|' << t << std::endl;
						c[Edge<int>{s, t, true}] = BASE - min(dist * S, 2 * F);
					}
				}
			}
		}
		FordFulkerson(G, c, start, end, f);
		int total_flow = 0;
		for (auto i = G.edges_from(start); !i.end(); i++) {
			total_flow += f[*i];
		}
		int ans = min(G_count, M_count) * BASE - total_flow + \
					abs(G_count - M_count) * F;
		if ("print graph") {
			auto f1 = [](size_t vv) {
				return false;
			};
			auto f2 = [c, f](Edge<int> e) mutable {
				std::cout << " [label=\"" << f[e] << "/" << c[e] << "\"";
				if (f[e])
					std::cout << " style=bold";
				std::cout << "]";
			};
			graphviz(G, f1, f2);
		}
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

