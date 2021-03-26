try:
	import sys
	stdin = sys.stdin
	stdin = open('mu.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

import functools

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

def funclog(func):
	def f(*args):
		ans = func(*args)
		print(*args, ans)
		return ans
	return f

@functools.lru_cache(1048576)
# @funclog
def solve_range(X, Y, nques, left, right):
	if nques <= 0:
		if left != right:
			if left == 'C':
				return X
			else:
				assert left == 'J'
				return Y
	if left == 'X':
		return min(
			solve_range(X, Y, nques - 1, 'C', right),
			solve_range(X, Y, nques - 1, 'J', right),
		)
	elif right == 'X':
		return min(
			solve_range(X, Y, nques - 1, left, 'C'),
			solve_range(X, Y, nques - 1, left, 'J'),
		)
	elif left != right:
		if left == 'C':
			return solve_range(X, Y, nques - 1, right, right) + X
		else:
			assert left == 'J'
			return solve_range(X, Y, nques - 1, right, right) + Y
	else:
		# C JCJC C
		# 1 -> 1, 2 -> 1, 3 -> 2, 4 -> 2
		max_change = (nques + 1) // 2
		if X + Y < 0:
			return max_change * (X + Y)
		else:
			return 0
		return 0

def solve_extra(X, Y, S):
	if len(S) == 1:
		return 0
	prev = 'X'
	prev_let_i = -1
	prev_let = 'X'
	ans = 0
	for index, i in enumerate(S):
		if i == 'C':
			if prev == 'J':
				ans += Y
			elif prev == '?':
				ans += solve_range(X, Y, index - prev_let_i - 1, prev_let, i)
		elif i == 'J':
			if prev == 'C':
				ans += X
			elif prev == '?':
				ans += solve_range(X, Y, index - prev_let_i - 1, prev_let, i)
		else:
			assert i == '?'
			if prev != '?':
				prev_let = prev
				prev_let_i = index - 1
		prev = i
	if prev == '?':
		ans += solve_range(X, Y, len(S) - prev_let_i - 1, prev_let, 'X')
	return ans

T = int(input())
for test in range(T):
	X, Y, S = input().split()
	X = int(X)
	Y = int(Y)
	if X > 0 and Y > 0:
		ans = solve_normal(X, Y, S)
		# assert ans == solve_extra(X, Y, S)
	else:
		ans = solve_extra(X, Y, S)

	print('Case #%d:' % (test + 1), ans)

