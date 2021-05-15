#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

using INT = long long int;

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

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N;
		std::cin >> N;
		int V[N];
		for (int i = 0; i < N; i++)
			cin >> V[i];
		INT ans = sol1(N, V);
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

