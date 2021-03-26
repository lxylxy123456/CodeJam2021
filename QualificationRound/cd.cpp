#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

#define FLOAT float
#define EXP expf

FLOAT f(FLOAT x) {
	return 1 / (1 + EXP(-x));
}

FLOAT GUESS[] = {-2.75, -2.25, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25,
					1.75, 2.25, 2.75};
constexpr int LEN_GUESS = sizeof(GUESS) / sizeof(GUESS[0]);

template <typename T>
T square(T x) {
	return x * x;
}

int main() {
	int T, P;
	cin >> T >> P;
	for (int test = 0; test < T; test++) {
		char result[100][10000];
		for (int i = 0; i < 100; i++)
			cin >> result[i];
		
//		for (int i = 0; i < 100; i++)
//			for (int j = 0; j < 10000; j++)
//				assert (result[i][j] == '1' || result[i][j] == '0');
		FLOAT skill[100];
		for (int i = 0; i < 100; i++) {
			int correct_count = 0;
			for (int j = 0; j < 10000; j++)
				correct_count += result[i][j] == '1' ? 1 : 0;
			FLOAT correct_rate = ((FLOAT) correct_count) / 10000;
			skill[i] = (correct_rate - 0.5) * 7.5;
		}
		FLOAT diff[10000];
		for (int i = 0; i < 10000; i++) {
			FLOAT prob[LEN_GUESS];
			for (int j = 0; j < LEN_GUESS; j++)
				prob[j] = 0;
			for (int j = 0; j < 100; j++)
				for (int k = 0; k < LEN_GUESS; k++) {
					if (result[j][i] == '1')
						prob[k] += f(skill[j] - GUESS[k]);
					else
						prob[k] += 1 - f(skill[j] - GUESS[k]);
				}
			int correct_guess = 0;
			for (int j = 0; j < LEN_GUESS; j++)
				if (prob[correct_guess] < prob[j])
					correct_guess = j;
			diff[i] = GUESS[correct_guess];
		}
		FLOAT fukashigis[100];
		for (int i = 0; i < 100; i++) {
			FLOAT fukashigi = 0;
			if (0) {
				for (int j = 0; j < 10000; j++) {
					if (result[i][j] == '1')
						fukashigi -= 1 - f(skill[i] - diff[j]);
					else
						fukashigi -= f(skill[i] - diff[j]);
				}
			} else if (0) {
				for (int j = 0; j < 10000; j++) {
					fukashigi += result[i][j] - '0';
					fukashigi -= f(skill[i] - diff[j]);
				}
			} else {
				for (int j = 0; j < 10000; j++) {
					if (result[i][j] == '1')
						fukashigi -= square(1 - f(skill[i] - diff[j]));
					else
						fukashigi -= square(f(skill[i] - diff[j]));
				}
			}
			fukashigis[i] = fukashigi;
		}
		int ans = 0;
		for (int i = 0; i < 100; i++) {
			if (fukashigis[ans] < fukashigis[i])
				ans = i;
		}
		cout << "Case #" << (test + 1) << ": " << (ans + 1) << endl;
	}
}

