try:
	import os, sys
	stdin = sys.stdin
	if len(sys.argv) > 1:
		stdin = open(sys.argv[1])
	else:
		# stdin = open('s.txt')
		stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

# python3 ../interactive_runner.py python3 local_testing_tool.py 0 -- python3 db9.py

import random
from fractions import Fraction
# import math, sys
# sys.setrecursionlimit(100000000)
from collections import defaultdict
# A = list(map(int, input().split()))

T, N, B, P = list(map(int, input().split()))

dp = []	# dp[a][b][c][d]  = expected score of having a blocks placed, where
		# there are b towers of height B - 2, c towers of height B - 1, d ... B
		# a in range(N * B + 1, (b, c, d) in range(N + 1))

if 'calculate_dp':
	for i in range(N * B + 1):
		dp.append([])
		for j in range(N + 1):
			dp[-1].append([])
			for k in range(N + 1):
				dp[-1][-1].append([])
				for l in range(N + 1):
					dp[-1][-1][-1].append(None)

	dp[N * B][0][0][N] = Fraction(0)

	def valid_dp(a, b, c, d):
		if a not in range(N * B + 1):
			return False
		bcd = b + c + d
		if bcd > N:
			return False
		single = a - (b * (B - 2) + c * (B - 1) + d * B)
		if single not in range(B - 2):
			return False
		if bcd == N and single:
			return False
		return True

	def next_state(a, b, c, d):
		# returns new_a, new_b, new_c, new_d, pow10
		assert valid_dp(a, b, c, d)
		if b:
			yield a + 1, b - 1, c + 1, d, B - 2
		if c:
			yield a + 1, b, c - 1, d + 1, B - 1
		if b + c + d < N:
			pow10 = a - (b * (B - 2) + c * (B - 1) + d * B)
			assert pow10 >= 0
			if pow10 < B - 3:
				yield a + 1, b, c, d, pow10
			else:
				yield a + 1, b + 1, c, d, pow10

	for a in reversed(range(N * B)):
		for b in range(N + 1):
			if b * (B - 2) > a:
				continue
			for c in range(N + 1):
				if b + c > N or b * (B - 2) + c * (B - 1) > a:
					continue
				for d in range(N + 1):
					# print(a, b, c, d, valid_dp(a, b, c, d))
					if not valid_dp(a, b, c, d):
						continue
					next_states = []
					for i, j, k, l, m in next_state(a, b, c, d):
						if dp[i][j][k][l] is None:
							print(a, b, c, d, 'e1')
							print(i, j, k, l, 'e2')
							print(list(next_state(a, b, c, d)))
							0/0
						next_states.append((dp[i][j][k][l], m))
					best_total = 0
					for i in range(10):
						best = 0
						for j, k in next_states:
							best = min(best, j - i * 10**k)
						best_total += best
					dp[a][b][c][d] = best_total / 10
					# print(a, b, c, d, dp[a][b][c][d])

	if not 'write dp':
		import pickle
		pickle.dump(dp, open('/tmp/a.pickle', 'wb'))
	
# print(dp, file=sys.stderr)
# 0/0

for test in range(T):
	heights = [0] * N
	h2i = defaultdict(set)
	h2i[0] = set(range(20))
	def place(n):
		print(n + 1)
		h = heights[n]
		h2i[h].remove(n)
		h += 1
		heights[n] = h
		h2i[h].add(n)
	a, b, c, d = 0, 0, 0, 0
	for i in range(N * B):
		D = int(input())
		assert D != -1
		next_states = []
		for i, j, k, l, m in next_state(a, b, c, d):
			if dp[i][j][k][l] is None:
				0/0
			next_states.append((dp[i][j][k][l], m, (i, j, k, l)))
		best = 1
		best_m = None
		best_ijkl = None
		for j, k, l in next_states:
			ji10k = j - D * 10**k
			if ji10k < best:
				best = ji10k
				best_m = k
				best_ijkl = l
		# print(a, b, c, d, heights, best_m, file=sys.stderr, end='\t', flush=1)
		place(next(filter(lambda x: x[1] == best_m, enumerate(heights)))[0])
		a, b, c, d = best_ijkl
	assert heights == [B] * N
# 
#   1000000000000000

print('               860939810732536850', file=sys.stderr)
print('               937467793908762347', file=sys.stderr)
print(input(), file=sys.stderr)	# should be 1 on AC

# 47 min, AC WA (estimated based on local testing)
# 60 min, AC WA

