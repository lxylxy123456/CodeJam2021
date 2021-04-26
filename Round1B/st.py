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
				v[-2] += v[-1]
				v[-3] += v[-1]
				v[-1] = 0
	for i in range(N + 1, 10000000000000000000000000000):
		if try_root(i):
			return i
	0/0

# def solve2()

T = int(input())
for test in range(T):
	N, A, B = list(map(int, input().split()))
	U = [0] + list(map(int, input().split()))
	if A == 1 and B == 2:
		ans = solve1(N, A, B, U)
	else:
		0/0
	if ans is None:
		ans = 'IMPOSSIBLE'
	print('Case #%d:' % (test + 1), ans)

# 63 min, AC RC

