try:
	import os, sys
	stdin = sys.stdin
	# stdin = open('s.txt')
	stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


T = int(input())
for test in range(T):

	print('Case #%d:' % (test + 1), ans)

