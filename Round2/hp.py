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

def sol(N, V):
	import itertools
	cur_visible = []	# [i] = the cooking order of i-th biggest visible
	constraints = []
	for index, i in enumerate(V):
		#j = V[index + 1]
		#if j - i > 1:
		#	ans = 0
		if i > len(cur_visible) + 1:
			return 0
		lower_bound = None
		upper_bound = None
		while len(cur_visible) > i - 1:
			lower_bound = cur_visible.pop()
		if cur_visible:
			upper_bound = cur_visible[-1]
		cur_visible.append(index)
		if lower_bound is not None:
			constraints.append((lower_bound, index))
		if upper_bound is not None:
			constraints.append((index, upper_bound))
		# print(cur_visible)
	# print(constraints)
	ans = 0
	for p in itertools.permutations(range(N)):
		good = True
		for i, j in constraints:
			good = good and p.index(i) < p.index(j)
		ans += int(good)
	return ans

T = int(input())
for test in range(T):
	N = int(input())
	V = list(map(int, input().split()))
	ans = sol(N, V)
	print('Case #%d:' % (test + 1), ans)

# a b c d
# 1 2 2 1: b < a; a > c > b; d > b
# 1 1 2  : b > a; c < b

