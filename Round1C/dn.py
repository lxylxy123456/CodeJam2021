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

NOT = {'0': '1', '1': '0'}.__getitem__

def op_double(x):
	if x == '0':
		return x
	return x + '0'

def op_not(x):
	if x == '0':
		return '1'
	ans = ''.join(map(NOT, x)).lstrip('0')
	if not ans:
		ans = '0'
	return ans

def search(S, E):
	searched = set()
	fringe = {S}
	ans = 0
	# while True:
	mSE2 = max(len(S), len(E)) * 2 + 2
	f = lambda x: len(x) < mSE2
	while fringe:
		if E in fringe:
			return ans
		new_fringe = set()
		for i in fringe:
			new_fringe.add(op_not(i))
			new_fringe.add(op_double(i))
		searched.update(fringe)
		fringe = set(filter(f, new_fringe)).difference(searched)
		ans += 1
	return 'IMPOSSIBLE'

T = int(input())
for test in range(T):
	S, E = input().split()
	ans = search(S, E)
	print('Case #%d:' % (test + 1), ans)

# 18 min, AC MLE (1 attempt total)

