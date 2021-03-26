try:
	import sys
	stdin = sys.stdin
	stdin = open('mu.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

import operator

def solve_normal(X, Y, S):
	prev = 'X'
	ans = 0
	for i in S:
		if i == 'C':
			if prev == 'J':
				ans += Y
			prev = i
		elif i == 'J':
			if prev == 'C':
				ans += X
			prev = i
	return ans

T = int(input())
for test in range(T):
	X, Y, S = input().split()
	X = int(X)
	Y = int(Y)
	ans = solve_normal(X, Y, S)

	print('Case #%d:' % (test + 1), ans)

