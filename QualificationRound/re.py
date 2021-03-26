try:
	import sys
	stdin = sys.stdin
	stdin = open('re.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

import operator

#Reversort(L):
#  for i := 1 to length(L) - 1
#    j := position with the minimum value in L between i and length(L), inclusive
#    Reverse(L[i..j])

T = int(input())
for test in range(T):
	N, C = map(int, input().split())

	min_cost = N - 1
	max_cost = (2 + N) * (N - 1) // 2	# 2 + 3 + ... + N
	if C not in range(min_cost, max_cost + 1):
		ans = 'IMPOSSIBLE'
	else:
		redundant_cost = C - min_cost
		cost_budget = []
		for i in range(N - 1):
			cur_cost = max(0, min(N - i - 1, redundant_cost))
			redundant_cost -= cur_cost
			cost_budget.append(cur_cost)
		L = list(range(1, N + 1))
		for i in reversed(range(N - 1)):
			# L[i: j + 1]
			j = i + cost_budget[i]
			L[i: j + 1] = reversed(L[i: j + 1])
		ans = ' '.join(map(str, L))
	print('Case #%d:' % (test + 1), ans)

