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

# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def get_ranges(P, K):
	ranges = []	# [1]: whether on the end (1 or K)
	# P = [3, 4, 5, 8], K = 10
	# ranges = [(2, True), (0, False), (0, False), (2, False), (2, True)]
	ranges.append((P[0] - 1, True))
	for i, j in zip(P, P[1:]):
		ranges.append((j - i - 1, False))
	ranges.append((K - P[-1], True))
	return ranges

def get_len(rng, nchoice):
	if nchoice == 2 or rng[1]:
		return rng[0]
	else:
		# 1 2 3 4 5 6 7 8 9 a b
		# O M O					1	1
		# O M . O				2	1
		# O . M . O				3	1
		# O M x . O				3	2
		# O . M x . O			4	2
		# O M x . . O			4	2
		# O . x M x . O			5	3
		# O M x x . . O			5	3
		# O . x M x . . O		6	3
		# O M x x . . . O		6	3
		# O . . x M x . . O		7	3
		# O M x x x . . . O		7	4
		# O . . x M x x . . O	8	4
		# O M x x x . . . . O	8	4
		# O . . x x M x x . . O	9	5
		# O M x x x x . . . . O	9	5
		return (rng[0] + 1) // 2

# assert get_ranges([3, 4, 5, 8], 10) == [(2, True), (0, False), (0, False), (2, False), (2, True)]

T = int(input())
for test in range(T):
	N, K = list(map(int, input().split()))
	P = list(map(int, input().split()))
	ans = K, N, P
	p = sorted(set(P))
	ranges = get_ranges(p, K)
	ranges = list(filter(lambda x: x[0], ranges))
	best_len = 0
	# choose one
	for i in ranges:
		cur_len = get_len(i, 2)
		best_len = max(best_len, cur_len)
	# choose two
	a = []
	for i in ranges:
		a.append(get_len(i, 1))
	a.sort()
	best_len = max(best_len, sum(a[-2:]))
# 	print(ranges, best_len, a)
	ans = best_len / K
	print('Case #%d:' % (test + 1), ans)

# 25 min, AC AC (1 attempts total)

