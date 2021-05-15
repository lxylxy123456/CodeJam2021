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

import functools
# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def factor(N):
	ans = []
	while N % 2 == 0:
		ans.append(2)
		N //= 2
	i = 3
	while N > i:
		while N % i == 0:
			ans.append(i)
			N //= i
		i += 2
	ans.append(N)
	return ans

@functools.lru_cache(100000)
def sol1(N, minimum=3):
	f = factor(N)
	ans = 0
	for i in range(1 << len(f)):
		a = 1
		b = 1
		for jndex, j in enumerate(f):
			if i & (1 << jndex):
				a *= j
			else:
				b *= j
		if a < minimum:
			continue
		if b == 1:
			ans = max(ans, 1)
			continue
		ans = max(ans, 1 + sol1(b - 1, 2))
	# print(' ' * level, N, minimum, ans)
	return ans

# 24 6 3
# 22 11
# 8 2 1

T = int(input())
for test in range(T):
	N = int(input())
	ans = sol1(N)
	print('Case #%d:' % (test + 1), ans)

