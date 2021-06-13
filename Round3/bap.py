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

import operator
# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def min_abs(d, can0=True):
	if len(d) == 0:
		return 0
	ddd = d
	if not can0:
		ddd = list(filter(bool, d))
	approx = min(map(operator.sub, ddd[1:], ddd[:-1]))
	e = len(d) // 2 - 1
	ans = 10**e * 100
	if approx == 0:
		for i in set(d[::2]).intersection(set(d[1::2])):
			if i == 0 and not can0:
				continue
			dd = list(d)
			dd.remove(i)
			dd.remove(i)
			ans = min(ans, min_abs(dd))
	sd = sorted(set(d))
	for i, j in zip(sd, sd[1:]):
		if i == 0 and not can0:
			continue
		if j - i == max(1, approx):
			dd = list(d)
			dd.remove(i)
			dd.remove(j)
			ans = min(ans, (j - i) * 10**e - max_abs(dd))
	# print('min', d, ans)
	return ans

def max_abs(d):
	if not d:
		return 0
	e = len(d) // 2 - 1
	ans = (d[-1] - d[0]) * 10**e + max_abs(d[1:-1])
	# print('max', d, ans)
	return ans

T = int(input())
for test in range(T):
	D = sorted(map(int, input()))
	if len(D) == 2:
		ans = abs(int(D[0]) - int(D[1]))
	else:
		d = list(D)
		while d[0] == 0:
			d.pop(0)
		e = len(D) // 2 - 1
		if len(D) % 2 == 0:
			# Must be same number of digits
			ans = min_abs(tuple(D), False)
			'''
			approx = min(map(operator.sub, d[1:], d[:1]))
			ans = 10**e * 100
			for i in range(10):
				if i not in D:
					continue
				d = list(D)
				d.remove(i)
				for j in range(i, 10):
					if j - i > approx:
						break
					if j not in d:
						continue
					dd = list(d)
					dd.remove(j)
					ans = min(ans, (j - i) * 10**e + min_abs(tuple(dd)))
			'''
		else:
			# Must choose smallest number on more-digit-integer
			# Must choose largest number on less-digit-integer
			# Digit difference must be 1
			sm = d[0]
			lg = d[-1]
			dd = list(D)
			dd.remove(sm)
			dd.remove(lg)
			sm2 = dd.pop(0)
			ans = (sm * 10 + sm2 - lg) * 10**e - max_abs(tuple(dd))

	print('Case #%d:' % (test + 1), ans)

