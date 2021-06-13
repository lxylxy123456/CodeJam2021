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
from collections import Counter
# A = list(map(int, input().split()))

def min_abs(d, _):
	c = Counter(d)
	ans = 10**len(d) * 100
	for i0 in range(0, c[0] + 1, 2):
	 for i1 in range(0, c[1] + 1, 2):
	  for i2 in range(0, c[2] + 1, 2):
	   for i3 in range(0, c[3] + 1, 2):
	    for i4 in range(0, c[4] + 1, 2):
	     for i5 in range(0, c[5] + 1, 2):
	      for i6 in range(0, c[6] + 1, 2):
	       for i7 in range(0, c[7] + 1, 2):
	        for i8 in range(0, c[8] + 1, 2):
	         for i9 in range(0, c[9] + 1, 2):
	          i = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
	          if i0 and i0 == sum(i):
	           continue
	          dd = []
	          for j in range(10):
	           for _ in range(c[j] - i[j]):
	            dd.append(j)
	          if not dd:
	           return 0
	          can0 = sum(i)
	          sdd = sorted(set(dd))
	          if 0 in sdd and not can0:
	           sdd.remove(0)
	          for j, k in zip(sdd[:-1], sdd[1:]):
	           ddd = list(dd)
	           ddd.remove(j)
	           ddd.remove(k)
	           ans = min(ans, (k - j) * 10**(len(dd) // 2 - 1) - max_abs(ddd))
	          ans = min(ans, max_abs(dd))
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

