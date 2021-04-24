try:
	import os, sys
	stdin = sys.stdin
	# stdin = open('s.txt')
	stdin = open(os.path.splitext(__file__)[0] + '.txt')
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

	tmp1 = 1
	tmp2 = 0
	while tmp1 <= total:
		tmp1 *= P[0]
		tmp2 += 1
	limit = tmp2 * P[-1]

	def factor(num):
		ans_sum = 0
		ans = [0] * M
		for index, i in enumerate(P):
			while num % i == 0:
				ans[index] += 1
				ans_sum += i
				num //= i
				if ans[index] > N[index]:
					return None, None
		if num != 1:
			return None, None
		return ans, ans_sum

	ans = 0
	for i in range(0, limit):
		num = total - i
		if num <= 0:
			break
		factor_list, factor_sum = factor(num)
		if factor_sum is not None and factor_sum == i:
			ans = num
			break
	print('Case #%d:' % (test + 1), ans)

