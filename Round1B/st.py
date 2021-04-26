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

import math # sys
# sys.setrecursionlimit(100000000)
from collections import defaultdict
# A = list(map(int, input().split()))

def solve1_old(N, A, B, U):
	assert A == 1 and B == 2
	req = dict(enumerate(U))
	total_req = sum(U)
	while total_req > 1:
		# print(req)
		k = min(req)
		if req[k] == 0:
			del req[k]
			continue
		if req.get(k + 1, 0) > 0:
			req[k] -= 1
			if not req[k]: del req[k]
			req[k + 1] -= 1
			if not req[k + 1]: del req[k + 1]
			req[k + 2] = req.get(k + 2, 0) + 1
			total_req -= 1
		else:
			req[k] -= 1
			if not req[k]: del req[k]
			req[k + 1] = req.get(k + 1, 0) + 1
	while req[min(req)] == 0:
		del req[min(req)]
	return min(req)

def solve1_old2(N, A, B, U):
	# Incorrect. e.g. 1 1 2 2 3 3, gives 7, should be 6
	assert A == 1 and B == 2
	req = []
	for index, i in enumerate(U):
		for _ in range(i):
			req.append(index)
	while len(req) > 1:
		# print(req)
		k = min(req)
		if k + 1 in req:
			req.remove(k)
			req.remove(k + 1)
			req.append(k + 2)
		else:
			req.remove(k)
			req.append(k + 1)
	assert len(req) == 1
	return req[0]

def solve1(N, A, B, U):
	assert A == 1 and B == 2
	def try_root(r):
		u = U.copy()
		v = [0] * r + [1]
		while u:
			# print(u, v)
			while u and u[-1] == 0:
				u.pop()
			while v and v[-1] == 0:
				v.pop()
			if not u:
				return True
			if not v:
				return False
			if len(v) < len(u):
				return False
			elif len(v) == len(u):
				if v[-1] < u[-1]:
					return False
				v[-1] -= u[-1]
				u[-1] = 0
			else:	# len(v) > len(u)
				if len(v) >= 2:
					v[-2] += v[-1]
				if len(v) >= 3:
					v[-3] += v[-1]
				v[-1] = 0
	for i in range(N + 1, 10000000000000000000000000000):
		if try_root(i):
			return i

def solve2(N, A, B, U):
	rem = set()
	gcd = math.gcd(A, B)
	for index, i in enumerate(U):
		if i:
			rem.add(index % gcd)
	if len(rem) > 1:
		return None

	def try_root(r):
		u = U.copy()
		v = [0] * r + [1]
		while u:
			# print(u, v)
			while u and u[-1] == 0:
				u.pop()
			while v and v[-1] == 0:
				v.pop()
			if not u:
				return True
			if not v:
				return False
			if len(v) < len(u):
				return False
			elif len(v) == len(u):
				if v[-1] < u[-1]:
					return False
				v[-1] -= u[-1]
				u[-1] = 0
			else:	# len(v) > len(u)
				if len(v) >= A + 1:
					v[-1 - A] += v[-1]
				if len(v) >= B + 1:
					v[-1 - B] += v[-1]
				v[-1] = 0

	for i in range(N + gcd, 100000000000000000000000000000000, gcd):
		if try_root(i):
			return i
	0/0

# def solve2()

if not 'dp':
	while True:
		import random
		N = 3
		U = [random.randrange(3) for _ in range(N + 1)]
		U[0] = 0
		U[-1] += 1
		if sum(U) < 2:
			continue
		a = solve1(N, 1, 2, U)
		b = solve1_old2(N, 1, 2, U)
		if a != b:
			print(N)
			print(U)
			print(a, b)

T = int(input())
for test in range(T):
	N, A, B = list(map(int, input().split()))
	U = [0] + list(map(int, input().split()))
	if A == 1 and B == 2:
		ans = solve1(N, A, B, U)
	else:
		ans = solve2(N, A, B, U)
	if ans is None:
		ans = 'IMPOSSIBLE'
	print('Case #%d:' % (test + 1), ans)

# 63 min, AC RE (5 attempts total)
# 75 min, AC AC (6 attempts total)

