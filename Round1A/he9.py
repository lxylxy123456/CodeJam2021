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

def solve2(N, Q, A, S):
	assert N == 2
	# p[q] = p(answer of question q is T)
	# pTT = p(answer is T | A[0] gives T and A[1] gives T)
	# pTF = p(answer is T | A[0] gives T and A[1] gives F)
	# pFT = p(answer is T | A[0] gives F and A[1] gives T) = 1 - pTF
	# pFF = p(answer is T | A[0] gives F and A[1] gives F) = 1 - pTT
	P = []		# p[q] = [0] + [1] * pTT + [2] * pTF
	for a0, a1 in zip(A[0], A[1]):
		if a0 == 'T':
			if a1 == 'T':	P.append((0, 1, 0))
			else:			P.append((0, 0, 1))
		else:
			if a1 == 'T':	P.append((1, 0, -1))
			else:			P.append((1, -1, 0))
	E0 = (0, 0, 0)
	E1 = (0, 0, 0)
	for a0, a1, p in zip(A[0], A[1], P):
		if a0 == 'T':
			p0 = p
		else:
			p0 = map(operator.sub, (1, 0, 0), p)
		E0 = tuple(map(operator.add, E0, p0))
		if a1 == 'T':
			p1 = p
		else:
			p1 = map(operator.sub, (1, 0, 0), p)
		E1 = tuple(map(operator.add, E1, p1))
	# display2d:false$
	# solve([S[0] = E0[0] + E0[1] * pTT + E0[2] * pTF,
	#		S[1] = E1[0] + E1[1] * pTT + E1[2] * pTF], [pTT, pTF]);
	nTT = ((-S[0]*E1[2])+E0[0]*E1[2]+(S[1]-E1[0])*E0[2])
	nTF = -(E0[1]*(S[1]-E1[0])-S[0]*E1[1]+E0[0]*E1[1])
	den = (E1[1]*E0[2]-E0[1]*E1[2])
	if den == 0:
		assert not nTT and not nTF
		pTT = Fraction(1, 2)
		pTF = Fraction(1, 2)
		if E0[2] == 0 and E1[2] == 0:
			if E0[1] != 0:
				pTT = Fraction(S[0] - E0[0], E0[1])
			elif E1[1] != 0:
				pTT = Fraction(S[1] - E1[0], E1[1])
		elif E0[1] == 0 and E1[1] == 0:
			if E0[2] != 0:
				pTF = Fraction(S[0] - E0[0], E0[2])
			elif E0[1] != 0:
				pTF = Fraction(S[1] - E1[0], E1[2])
		else:
			if E0[1] == 0:
				s, e = S[1], E1
			else:
				s, e = S[0], E0
			s -= e[0]
			if s * e[1] <= 0:
				pTT = Fraction(0, 1)
			elif abs(s) > abs(e[1]):
				pTT = Fraction(1, 1)
			else:
				pTT = Fraction(s, e[1])
			s -= e[1] * pTT
			if e[2] == 0:
				pTF = 0
				assert s == 0
			else:
				pTF = Fraction(s, e[2])
	else:
		pTT = Fraction(nTT, den)
		pTF = Fraction(nTF, den)
	assert 0 <= pTT and pTT <= 1
	assert 0 <= pTF and pTF <= 1
	ansl = ''
	ansr = Fraction(0)
	for i in P:
		p = i[0] + i[1] * pTT + i[2] * pTF
		if p > Fraction(1, 2):
			ansl += 'T'
			ansr += p
		else:
			ansl += 'F'
			ansr += 1 - p
	ansr = '%d/%d' % (ansr.numerator, ansr.denominator)
	return ansl, ansr	

def combination(N, M):
	assert N >= M
	return math.factorial(N) // (math.factorial(M) * math.factorial(N - M))

def solve3(N, Q, A, S):
	assert N == 3
	c = Counter(zip(*A))
	q1 = c['T', 'T', 'T'] + c['F', 'F', 'F']
	q2 = c['T', 'T', 'F'] + c['F', 'F', 'T']
	q3 = c['T', 'F', 'T'] + c['F', 'T', 'F']
	q4 = c['T', 'F', 'F'] + c['F', 'T', 'T']
	total_count = 0
	# si0: score in type i questions where 0 are the same answer as A[0]
	# siq: score in type i questions where q1 are the same answer as A[0]
	s10, s1q = 0, 0
	s20, s2q = 0, 0
	s30, s3q = 0, 0
	s40, s4q = 0, 0
	for t1 in range(q1 + 1):	# number of q1 questions that A[0] is correct
		# display2d:false$
		# solve([S[0] = t1 + t2 + t3 + t4, 
		#		S[1] = t1 + t2 + q3 - t3 + q4 - t4,
		#		S[2] = t1 + q2 - t2 + t3 + q4 - t4], [t2, t3, t4]);
		t2 = -(2*t1+q4+q3-S[1]-S[0])
		assert t2 % 2 == 0
		t2 //= 2
		t3 = -(2*t1+q4+q2-S[2]-S[0])
		assert t3 % 2 == 0
		t3 //= 2
		t4 = (2*t1+2*q4+q3+q2-S[2]-S[1])
		assert t4 % 2 == 0
		t4 //= 2
		if not t2 in range(q2 + 1): continue
		if not t3 in range(q3 + 1): continue
		if not t4 in range(q4 + 1): continue
		count = (combination(q1, t1) * combination(q2, t2) *
			combination(q3, t3) * combination(q4, t4))
		total_count += count
		s1q += t1 * count
		s10 += (q1 - t1) * count
		s2q += t2 * count
		s20 += (q2 - t2) * count
		s3q += t3 * count
		s30 += (q3 - t3) * count
		s4q += t4 * count
		s40 += (q4 - t4) * count
	# si0: score in type i questions where 0 are the same answer as A[0]
	# siq: score in type i questions where q1 are the same answer as A[0]
	ansl = ''
	for a0, a1, a2 in zip(*A):
		if (a0, a1, a2) in (('T', 'T', 'T'), ('F', 'F', 'F')):
			if s1q > s10:	ansl += a0
			else:			ansl += REV[a0]
		elif (a0, a1, a2) in (('T', 'T', 'F'), ('F', 'F', 'T')):
			if s2q > s20:	ansl += a0
			else:			ansl += REV[a0]
		elif (a0, a1, a2) in (('T', 'F', 'T'), ('F', 'T', 'F')):
			if s3q > s30:	ansl += a0
			else:			ansl += REV[a0]
		elif (a0, a1, a2) in (('T', 'F', 'F'), ('F', 'T', 'T')):
			if s4q > s40:	ansl += a0
			else:			ansl += REV[a0]
		else:
			raise ValueError
	num = max(s10, s1q) + max(s20, s2q) + max(s30, s3q) + max(s40, s4q)
	ansr = Fraction(num, total_count)
	ansr = '%d/%d' % (ansr.numerator, ansr.denominator)
	return ansl, ansr

import operator, math
from collections import Counter
from fractions import Fraction
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
#	while N >= 2 and A[0] == A[1]:
#		N = 1
#		assert S[0] == S[1]
#		S.pop()
#		A.pop()
	if N == 1:
		S.append(S[-1])
		A.append(A[-1])
		N += 1

	if N == 2:
		S.append(S[-1])
		A.append(A[-1])
		N += 1
	if N == 3:

#	if N == 2:
#		ansl, ansr = solve2(N, Q, A, S)
#	elif N == 3:

		ansl, ansr = solve3(N, Q, A, S)
	else:
		# p[q] = p(answer of question q is T)
		# pTTT = p(answer is T | A[0..2] gives TTT)
		# pTTF
		# pTFT
		# pTFF
		# pFTT = 1 - pTFF
		# pFTF = 1 - pTFT
		# pFFT = 1 - pTTF
		# pFFF = 1 - pTTT
		P = []	# p[q] = [0] + [1] * pTTT + [2] * pTTF + [3] * pTFT + [4] * pTFF
		for a012 in zip(A[0], A[1], A[2]):
			P.append({
				('T', 'T', 'T'): (0, 1, 0, 0, 0),
				('T', 'T', 'F'): (0, 0, 1, 0, 0),
				('T', 'F', 'T'): (0, 0, 0, 1, 0),
				('T', 'F', 'F'): (0, 0, 0, 0, 1),
				('F', 'T', 'T'): (1, 0, 0, 0, -1),
				('F', 'T', 'F'): (1, 0, 0, -1, 0),
				('F', 'F', 'T'): (1, 0, -1, 0, 0),
				('F', 'F', 'F'): (1, -1, 0, 0, 0),
			}[a012])
		E0 = (0, 0, 0, 0, 0)
		E1 = (0, 0, 0, 0, 0)
		E2 = (0, 0, 0, 0, 0)
		for a0, a1, a2, p in zip(A[0], A[1], A[2], P):
			p0 = p if A[0] == 'T' else map(operator.sub, (1, 0, 0, 0, 0), p)
			E0 = tuple(map(operator.add, E0, p0))
			p1 = p if A[0] == 'T' else map(operator.sub, (1, 0, 0, 0, 0), p)
			E1 = tuple(map(operator.add, E1, p1))
			p2 = p if A[0] == 'T' else map(operator.sub, (1, 0, 0, 0, 0), p)
			E2 = tuple(map(operator.add, E2, p2))
		# display2d:false$
		# solve([
		#	S[0] = E0[0] + E0[1]*pTTT + E0[2]*pTTF + E0[3]*pTFT + E0[4]*pTFF,
		#	S[1] = E1[0] + E1[1]*pTTT + E1[2]*pTTF + E1[3]*pTFT + E1[4]*pTFF,
		#	S[2] = E2[0] + E2[1]*pTTT + E2[2]*pTTF + E2[3]*pTFT + E2[4]*pTFF],
		#	[pTTT, pTTF, pTFT]);
		
		nsame, n2, n0, n1 = 0, 0, 0, 0
		Amaj = []
		Adif = []
		for i, j, k in zip(*A):
			if i == j:
				if j == k:
					nsame += 1
					Adif.append(-1)
				else:
					n2 += 1
					Adif.append(2)
				Amaj.append(i)
			else:
				if j == k:
					n0 += 1
					Adif.append(0)
				else:
					n1 += 1
					Adif.append(1)
				Amaj.append(k)
		assert nsame == Adif.count(-1)
		assert n0 == Adif.count(0)
		assert n1 == Adif.count(1)
		assert n2 == Adif.count(2)
		# x0 = number of correct in n0
		# x1 = number of correct in n1
		# x2 = number of correct in n2
		# xs = number of all correct
		# S0 = xs + x0 + n1 - x1 + n2 - x2
		# S1 = xs + x1 + n0 - x0 + n2 - x2
		# S2 = xs + x2 + n1 - x1 + n0 - x0
		# solve([S0 = xs + x0 + n1 - x1 + n2 - x2, S1 = xs + x1 + n0 - x0 + n2 - x2, S2 = xs + x2 + n1 - x1 + n0 - x0], [x1, x2, x0, xs]);
		for xs in range(Q + 1):
			x0 = (n2+n1+2*n0-S[2]-S[1]+2*xs)//2
			x1 = (n2+2*n1+n0-S[2]-S[0]+2*xs)//2
			x2 = (2*n2+n1+n0-S[1]-S[0]+2*xs)//2
			print(xs, x0, x1, x2)

		print(nsame, n0, n1, n2, S)
		0/0
	print('Case #%d:' % (test + 1), ansl, ansr)

