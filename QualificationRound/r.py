try:
	import sys
	stdin = sys.stdin
	stdin = open('r.txt')
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
	N = int(input())
	L = list(map(int, input().split()))

	ans = 0
	for i in range(N - 1):
		j = min(enumerate(L[i:], i), key=operator.itemgetter(1))[0]
		ans += len(L[i: j + 1])
		L[i: j + 1] = reversed(L[i: j + 1])
	print('Case #%d:' % (test + 1), ans)

