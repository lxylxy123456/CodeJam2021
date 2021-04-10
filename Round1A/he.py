try:
	import os, sys
	stdin = sys.stdin
	# stdin = open('s.txt')
	stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


import operator
REV = {'T': 'F', 'F': 'T'}

T = int(input())
for test in range(T):
	N, Q = map(int, input().split())
	A = []
	S = []
	for i in range(N):
		a, s = input().split()
		A.append(a)
		S.append(int(s))
	while N >= 2 and A[0] == A[1]:
		N = 1
		assert S[0] == S[1]
		S.pop()
		A.pop()
	if N == 1:
		if S[0] <= Q // 2:
			ansl = ''.join(map(REV.__getitem__, A[0]))
			ansr = '%d/1' % (Q - S[0])
		else:
			ansl = A[0]
			ansr = '%d/1' % S[0]
		# FFF 1
	elif N == 2:
		nsame = sum(map(operator.eq, A[0], A[1]))
		ndiff = Q - nsame
		schange = S[0] - S[1]
		# x: correct @ 0 -> incorrect @ 1
		# y: incorrect @ 0 -> correct @ 1
		# schange = x - y
		# ndiff = x + y
		# x = (schange + ndiff) // 2
		# y = (ndiff - schange) // 2
		# score on nsame = S[0] - x = S[0] - (schange + ndiff) // 2
		# score on ndiff = x (for 0) or y (for 1)
		x = (schange + ndiff) // 2
		y = (ndiff - schange) // 2
		ssame = S[0] - x
		if ssame <= nsame // 2:
			rev = True
			esame = nsame - ssame
		else:
			rev = False
			esame = ssame
		ansl = ''
		for i, j in zip(A[0], A[1]):
			if i != j:
				if x > y:
					ansl += i
				else:
					ansl += j
			else:
				if rev:
					ansl += REV[i]
				else:
					ansl += i
		ansr = '%d/1' % (esame + max(x, y))
	ans = repr((N, Q, A, S))
	print('Case #%d:' % (test + 1), ansl, ansr)

