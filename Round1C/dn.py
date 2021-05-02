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

REV = {'1': '0', '0': '1'}

def to_lst(N):
	if N == 0:
		return []
	count = 0
	cur = '1'
	ans = []
	for i in N:
		if i == cur:
			count += 1
		else:
			ans.append(count)
			cur = REV[cur]
			count = 1
	ans.append(count)
#	if cur == '1':
#		ans.append(0)
#	assert len(ans) % 2 == 0
	return ans

def solve(S, E):
	# Convert the string to (number of left-most 1s, number of 0s after that,
	# number of 1s after than, ...), treat 0 as a special case
	# Then double means:
	#  if len(lst) % 2 == 0: lst[-1] += 1
	#  else: lst.append(1)
	#  number of consecutive 1's will stay
	# And not means:
	#  lst.pop(0)
	#  number of consecutive 1's will stay or decrease
	# Treat 0 as empty list
	#  double([]) = []
	#  not([]) = [1]
	## Suppose we never need to convert 0 to 1, and allow lst[-1] to be 0
	## so that len(lst) % 2 == 0. Then
	##  double means lst[-1] += 1
	##  not means lst.pop(0); lst.append(0) if lst[-1] != 0 else lst.pop()
	if S == '0':
		if E == '0':
			return 0
		ans = solve('1', E)
		if ans == 'IMPOSSIBLE':
			return ans
		return ans + 1
	s = to_lst(S)
	e = to_lst(E)
	if E == '0':
		# 11 -> 0					1
		# 1100 -> 11 -> 0			2
		# 110011 -> 1100 -> 11 -> 0	3
		return len(s)
	if (len(s) + 1)//2 < (len(e) + 1)//2:
		return 'IMPOSSIBLE'
	# print(S, s); print(E, e)
	ans = 3**3**3
	for i in range(len(e) + 1):
		if not (i == 0 or s[-i:-1] == e[:i-1] and s[-1] <= e[i-1] and (
			s[-1] == e[i-1] or len(s) % 2 == 0 or
			(len(s)+1)//2 > (len(e)+1)//2)):
			continue
		cur = 0
		T = S
		t = s.copy()
		if i == 0:
			if len(t) % 2 == 0:
				# not
				t.pop(0); cur += 1; T = op_not(T)
			for jndex, j in enumerate(e):
				# double * j
				t.append(j); cur += j; T += '0' * j
				if jndex != len(e) - 1:
					# not
					t.pop(0); cur += 1; T = op_not(T)
			for _ in range(len(t) - len(e)):
				# not
				t.pop(0); cur += 1; T = op_not(T)
			assert T == E
		else:
			j = e[i-1] - s[-1]
			if j:
				if len(t) % 2 == 1:
					# not
					t.pop(0); cur += 1; T = op_not(T)
				# double * j
				t[-1] += j; cur += j; T += '0' * j
			for jndex, j in enumerate(e[i:]):
				if len(t) % 2 == 0:
					# not
					t.pop(0); cur += 1; T = op_not(T)
				# double * j
				t.append(j); cur += j; T += '0' * j
			for _ in range(len(t) - len(e)):
				# not
				t.pop(0); cur += 1; T = op_not(T)
			assert T == E
#			print(s[-i:-1] , e[:i-1] , s[-1] , e[i-1], i)
		if cur < ans:
			ans = cur
	return ans

if not 'afl':
	import random
	while True:
		S = bin(random.randrange(100))[2:]
		E = bin(random.randrange(100))[2:]
		# 100110 1001100
		print(S, E)
		solve(S, E)

T = int(input())
for test in range(T):
	S, E = input().split()
	# ans = search(S, E)
	ans = solve(S, E)
	print('Case #%d:' % (test + 1), ans)

# 18 min, AC MLE (1 attempt total)
# 88 min, AC AC (3 attempt total)

