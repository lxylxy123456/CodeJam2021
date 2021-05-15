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

import math, functools, sys
sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

MOD = 10**9 + 7

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

def sol1_old(N, V):
	# state: 0 is unused, 1 is visible, 2 is hidden
	# dp[state] = number of ways
	dp = [None] * 3**N
	def i2s(i):
		s = []
		for _ in range(N):
			s.append(i % 3)
			i //= 3
		return s
	def s2i(s):
		ans = 0
		for i in reversed(s):
			ans *= 3
			ans += i
		return ans
	def solve_dp(i, s):
		if dp[i] is not None:
			return dp[i]
		# assert(s2i(i2s(i)) == i)
		used = sum(map(bool, s))
		vis = sum(map(lambda x: x == 1, s))
		if used > 0 and V[used - 1] != vis:
			ans = 0
		elif used == N:
			ans = 1
		else:
			ans = 0
			for index, i in enumerate(s):
				if i:
					continue
				ss = s.copy()
				for j in range(index):
					if ss[j] == 1:
						ss[j] = 2
				ss[index] = 1
				ans += solve_dp(s2i(ss), ss)
			ans %= 10**9 + 7
			# print(i, s)
		dp[i] = ans
		return ans
	ans = solve_dp(0, i2s(0))
	return ans

def sol1(N, V):
	# state: 0 is unused, 1 is visible, 2 is hidden
	# dp[state] = number of ways
	@functools.lru_cache(3**(N + 1))
	def solve_dp(s):
		used = sum(map(bool, s))
		vis = sum(map(lambda x: x == 1, s))
		if used > 0 and V[used - 1] != vis:
			ans = 0
		elif used == N:
			ans = 1
		else:
			ans = 0
			ss = list(s)
			for index, i in enumerate(s):
				if i == 0:
					ss[index] = 1
					ans += solve_dp(tuple(ss))
					ss[index] = 0
				elif i == 1:
					ss[index] = 2
			ans %= 10**9 + 7
			# print(i, s)
		return ans
	ans = solve_dp((0,) * N)
	return ans
	# This function will TLE
	# If rewrite this function with C, no longer TLE

def fact(n, cache=[1, 1, 2, 6]):
	assert n < 10**5 + 10
	while len(cache) <= n:
		cache.append(cache[-1] * len(cache) % MOD)
	return cache[n]

def pow_mod(a, b):
	ans = 1
	while b:
		if b % 2 == 1:
			ans *= a
			ans %= MOD
		a **= 2
		a %= MOD
		b //= 2
	return ans

def inv_fact(n, cache=[]):
	assert n < 10**5 + 10
	while len(cache) <= n:
		cache.append(pow_mod(fact(len(cache)), MOD - 2))
	return cache[n]

# https://cp-algorithms.com/combinatorics/binomial-coefficients.html

def sol2(N, V):
	import itertools
	cur_visible = []	# [i] = the cooking order of i-th biggest visible
	constraints = set()
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
			constraints.add((lower_bound, index))
		if upper_bound is not None:
			constraints.add((index, upper_bound))
		if lower_bound is not None and upper_bound is not None:
			constraints.remove((lower_bound, upper_bound))
		# print(cur_visible)
	if 0:
		ans = 0
		for p in itertools.permutations(range(N)):
			good = True
			for i, j in constraints:
				good = good and p.index(i) < p.index(j)
			ans += int(good)
		return ans
	if 1:
		adj_list = []
		adj_list_rev = []
		for i in range(N):
			adj_list.append([])
			adj_list_rev.append([])
		for i, j in constraints:
			adj_list[i].append(j)
			adj_list_rev[j].append(i)
		assert max(map(len, adj_list)) <= 1
		s = [-1] * N
		f = [-1] * N
		if 0:
	#		count = 0
			def recu(i):
				assert s[i] == -1 and f[i] == -1
	#			nonlocal count
	#			count += 1
	#			assert count < N + 10
	#			if count % 100 == 0:
	#				print(count, N)
	#				if count == 20000:
	#					import pdb; pdb.set_trace()
				ss = 1
				k = []
				ff = 1
				for j in adj_list_rev[i]:
					recu(j)
					ss += s[j]
					ff *= f[j]
					ff %= MOD
					k.append(s[j])
				ff *= fact(sum(k))
				ff %= MOD
				for j in k:
					ff *= inv_fact(j)
					ff %= MOD
				s[i] = ss
				f[i] = ff
			root = None
			for i in range(N):
				if not adj_list[i]:
					assert root is None
					root = i
			assert root is not None
			recu(root)
			# print(adj_list)
			# print(f)
			# print(s)
			return f[root] % (10**9 + 7)
		elif 1:
			order = []
			def dfs(i):
				for j in adj_list_rev[i]:
					dfs(j)
				order.append(i)
			root = None
			for i in range(N):
				if not adj_list[i]:
					assert root is None
					root = i
			assert root is not None
			dfs(root)
			for i in order:
				ss = 1
				k = []
				ff = 1
				for j in adj_list_rev[i]:
					ss += s[j]
					ff *= f[j]
					ff %= MOD
					k.append(s[j])
				ff *= fact(sum(k))
				ff %= MOD
				for j in k:
					ff *= inv_fact(j)
					ff %= MOD
				s[i] = ss
				f[i] = ff
			return f[root] % (10**9 + 7)

T = int(input())
for test in range(T):
	N = int(input())
	V = list(map(int, input().split()))
	# ans = sol1(N, V)
	ans = sol2(N, V)
	print('Case #%d:' % (test + 1), ans)

# a b c d
# 1 2 2 1: b < a; a > c > b; d > b
# 1 1 2  : b > a; c < b

