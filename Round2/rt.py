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

import heapq
# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def tt(D):
	return tuple(map(tuple, D))

def ll(T):
	return list(map(list, T))

def score(D):
	return sum(map(lambda d, b: sum(map(lambda i, j: i != j, d, b)), D, B))

def neighbors(r, c, bidir=2):
	if r > 0:
		yield r - 1, c
	if c > 0:
		yield r, c - 1
	if bidir:
		if r < R - 1:
			yield r + 1, c
		if bidir > 1:
			if c < C - 1:
				yield r, c + 1

def next_states(D):
	DD = ll(D)
	for i in range(R):
		for j in range(C):
			if D[i][j] != B[i][j]:
				DD[i][j] = B[i][j]
				yield tt(DD), F
				for r, c in neighbors(i, j, bidir=0):
					if D[r][c] != B[r][c] and B[r][c] == D[i][j]:
						DD[r][c] = B[r][c]
						yield tt(DD), S
						DD[r][c] = D[r][c]
				DD[i][j] = D[i][j]

def path_search(T):
#	if score(T) == 0:
#		return 0
	searched = set()
	fringe = []
	heapq.heappush(fringe, (0, T))
	while True:
		dist, t = heapq.heappop(fringe)
		#print(dist)
		#for i in t:
		#	print(end='  ');
		#	for j in i: print(end=j);
		#	print()
		if score(t) == 0:
		#	for t in h:
		#		for i in t:
		#			print(end='  ')
		#			for j in i: print(end=j)
		#			print()
		#		print()
			return dist
		if t in searched:
			continue
		searched.add(t)
		for n, c in next_states(t):
			heapq.heappush(fringe, (dist + c, n))

T = int(input())
for test in range(T):
	R, C, F, S = list(map(int, input().split()))
	A = []
	for _ in range(R):
		A.append(list(input()))
	B = []
	for _ in range(R):
		B.append(list(input()))
	ans = path_search(tt(A))
	print('Case #%d:' % (test + 1), ans)

