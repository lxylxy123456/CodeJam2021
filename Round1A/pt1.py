try:
	import os, sys
	stdin = sys.stdin
	stdin = open('pt.txt')
	# stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

import itertools

T = int(input())
for test in range(T):
	M = int(input())
	P = []
	N = []
	for i in range(M):
		p, n = map(int, input().split())
		P.append(p)
		N.append(n)
	total = 0
	for p, n in zip(P, N):
		total += p * n
	ans = 0
	for choices in itertools.product(*map(lambda x: range(x + 1), N)):
		prod = 1
		sum_ = total
		for i, j in zip(P, choices):
			prod *= i**j
			sum_ -= i * j
		if sum_ == prod:
			ans = max(sum_, ans)
	print('Case #%d:' % (test + 1), ans)

