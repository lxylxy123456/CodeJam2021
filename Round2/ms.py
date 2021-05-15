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
# from collections import defaultdict
# A = list(map(int, input().split()))

T, N = list(map(int, input().split()))
for test in range(T):
	for i in range(1, N):
		print('M', i, N)
		index = int(input())
		if index != i:
			print('S', i, index)
			assert int(input()) == 1
	print('D')
	assert int(input()) == 1
	# print('Case #%d:' % (test + 1), ans)

