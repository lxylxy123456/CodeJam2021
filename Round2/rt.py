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
	return sum(map(sum, D))

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
			if DD[i][j]:
				DD[i][j] = False
				yield tt(DD), F
				for r, c in neighbors(i, j, bidir=0):
					if DD[r][c]:
						DD[r][c] = False
						yield tt(DD), S
						DD[r][c] = True
				DD[i][j] = True

def path_search(T):
#	if score(T) == 0:
#		return 0
	fringe = []
	heapq.heappush(fringe, (0, T, ()))
	while True:
		dist, t, h = heapq.heappop(fringe)
		print(dist)
		for i in t:
			print(end='  ')
			for j in i: print(end='01'[j])
			print()
		if score(t) == 0:
			for t in h:
				for i in t:
					print(end='  ')
					for j in i: print(end='01'[j])
					print()
				print()
			return dist
		for n, c in next_states(t):
			heapq.heappush(fringe, (dist + c, n, (t, *h)))

T = int(input())
for test in range(T):
	R, C, F, S = list(map(int, input().split()))
	A = []
	for _ in range(R):
		A.append(list(input()))
	B = []
	for _ in range(R):
		B.append(list(input()))
	D = []
	for i, j in zip(A, B):
		D.append(list(map(lambda x, y: x != y, i, j)))
	ans = path_search(tt(D))
	print('Case #%d:' % (test + 1), ans)

