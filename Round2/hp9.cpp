#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>

using namespace std;

using INT = long long int;

#define MOD 1000000007

INT solve_dp(int N, int *V, int *state, INT *dp) {
	int key = 0;
	for (int i = 0; i < N; i++)
		key = key * 3 + state[i];
	if (dp[key] != -1)
		return dp[key];
	INT ans = 0;
	int used = 0, vis = 0;
	for (int i = 0; i < N; i++) {
		if (state[i]) {
			used += 1;
			if (state[i] == 1)
				vis += 1;
		}
	}
	if (used > 0 && V[used - 1] != vis)
		ans = 0;
	else if (used == N)
		ans = 1;
	else {
		int ss[N];
		for (int i = 0; i < N; i++)
			ss[i] = state[i];
		for (int i = 0; i < N; i++) {
			if (state[i] == 0) {
				ss[i] = 1;
				ans += solve_dp(N, V, ss, dp);
				ans %= 1000000007;
				ss[i] = 0;
			} else if (state[i] == 1) {
				ss[i] = 2;
			}
		}
	}
	dp[key] = ans;
	return ans;
}

INT sol1(int N, int *V) {
	int ndp = pow(3, N);
	INT *dp = (INT*) malloc(ndp * sizeof(INT));
	for (int i = 0; i < ndp; i++)
		dp[i] = -1;
	int state[N];
	for (int i = 0; i < N; i++)
		state[i] = 0;
	INT ans = solve_dp(N, V, state, dp);
	free(dp);
	return ans;
}

INT pow_mod(INT a, int b) {
	INT ans = 1;
	while (b) {
		if (b % 2)
			ans = (ans * a) % MOD;
		a = a * a % MOD;
		b /= 2;
	}
	return ans;
}

void recu(int i, std::vector<int> &s, std::vector<INT> &f,
			std::vector<std::vector<int>> &adj_list_rev, INT *fact,
			INT *inv_fact) {
	assert(s[i] == -1 && f[i] == -1);
	int ss = 1;
	INT ff = 1;
	int k = 0;
	for (int j = 0; j < adj_list_rev[i].size(); j++) {
		recu(adj_list_rev[i][j], s, f, adj_list_rev, fact, inv_fact);
		ss += s[adj_list_rev[i][j]];
		ff = ff * f[adj_list_rev[i][j]] % MOD;
		k += s[adj_list_rev[i][j]];
		ff = ff * inv_fact[s[adj_list_rev[i][j]]] % MOD;
	}
	ff = ff * fact[k] % MOD;
	s[i] = ss;
	f[i] = ff;
}

int initialized = false;
std::vector<INT> fact = {1}, inv_fact = {1};

int sol2(int N, int *V) {
	if (!initialized) {
		for (int i = 1; i < 100010; i++) {
			fact.push_back(fact[i - 1] * i % MOD);
			inv_fact.push_back(pow_mod(fact[i], MOD - 2));
		}
	}
	std::vector<int> cur_visible;
	std::vector<std::vector<int>> constraints(N);
	for (int i = 0; i < N; i++) {
		if (V[i] > cur_visible.size() + 1)
			return 0;
		int lower_bound = -1, upper_bound = -1;
		while (cur_visible.size() > V[i] - 1) {
			lower_bound = cur_visible.back();
			cur_visible.pop_back();
		}
		if (cur_visible.size())
			upper_bound = cur_visible.back();
		cur_visible.push_back(i);
		if (lower_bound != -1) {
			if (upper_bound != -1)
				for (int j = 0; j < constraints[lower_bound].size(); j++) {
					if (constraints[lower_bound][j] == upper_bound) {
						constraints[lower_bound][j] = i;
						break;
					}
				}
			else
				constraints[lower_bound].push_back(i);
		}
		if (upper_bound != -1)
			constraints[i].push_back(upper_bound);
	}
	std::vector<std::vector<int>> adj_list = constraints;
	std::vector<std::vector<int>> adj_list_rev(N);
	int root = -1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < adj_list[i].size(); j++)
			adj_list_rev[adj_list[i][j]].push_back(i);
		if (!adj_list[i].size()) {
			assert(root == -1);
			root = i;
		}
	}
	assert(root != -1);
	std::vector<int> s(N, -1);
	std::vector<INT> f(N, -1);
	// recu(root, s, f, adj_list_rev, fact, inv_fact);
	std::vector<int> order;
	std::vector<int> fringe = {root};
	while (fringe.size()) {
		int i = fringe.back();
		fringe.pop_back();
		order.push_back(i);
		for (int j = 0; j < adj_list_rev[i].size(); j++) {
			fringe.push_back(adj_list_rev[i][j]);
		}
	}
	for (auto ii = order.rbegin(); ii != order.rend(); ii++) {
		int &i = *ii;
		assert(s[i] == -1 && f[i] == -1);
		int ss = 1;
		INT ff = 1;
		int k = 0;
		for (int j = 0; j < adj_list_rev[i].size(); j++) {
			ss += s[adj_list_rev[i][j]];
			ff = ff * f[adj_list_rev[i][j]] % MOD;
			k += s[adj_list_rev[i][j]];
			ff = ff * inv_fact[s[adj_list_rev[i][j]]] % MOD;
		}
		ff = ff * fact[k] % MOD;
		s[i] = ss;
		f[i] = ff;
	}
	return f[root];
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N;
		std::cin >> N;
		int V[N];
		for (int i = 0; i < N; i++)
			cin >> V[i];
		// INT ans = sol1(N, V);
		INT ans = sol2(N, V);
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

