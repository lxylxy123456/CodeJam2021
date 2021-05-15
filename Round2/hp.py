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

import math
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
	if 1:
		ans = 0
		for p in itertools.permutations(range(N)):
			good = True
			for i, j in constraints:
				good = good and p.index(i) < p.index(j)
			ans += int(good)
		return ans
	if 1:
		for i in range(N):
			constraints.append((N, i))
			constraints.append((i, N + 1))
		N += 2
		adj_list = []
		adj_list_rev = []
		for i in range(N):
			adj_list.append([])
			adj_list_rev.append([])
		for i, j in constraints:
			adj_list[i].append(j)
			adj_list_rev[j].append(i)
		print(adj_list)
		print(adj_list_rev)
		color = [0] * N
		order = []
		def dfs(s):
			if color[s] != 0:
				return
			color[s] = 1
			for t in adj_list[s]:
				dfs(t)
			order.append(s)
		dfs(N - 2)
		print(order)
		ancestor = [None] * N
		ancestor[N - 1] = set()
		for i in reversed(order):
			ancestor[i] = set()
			for j in adj_list_rev[i]:
				ancestor[i].update(ancestor[j])
				ancestor[i].add(j)
		perm = [None] * N
		perm[N - 1] = 0
		for i in reversed(order):
			perm = 1
			for j in adj_list_rev[i]:
				perm = math.factorial(perm + l) // \
						(math.factorial(l) * math.factorial(perm))
		print(ancestor)
	print(constraints)

T = int(input())
for test in range(T):
	N = int(input())
	V = list(map(int, input().split()))
	ans = sol(N, V)
	print('Case #%d:' % (test + 1), ans)

# a b c d
# 1 2 2 1: b < a; a > c > b; d > b
# 1 1 2  : b > a; c < b

