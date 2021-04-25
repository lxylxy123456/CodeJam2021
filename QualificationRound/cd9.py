try:
	import os, sys
	stdin = sys.stdin
	stdin = open('cd.txt')
	# stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

import math, operator, itertools
from collections import defaultdict

if not 'Check expectation':
	# L = 0100011
	# E[L[i] = 0 and L[j] = 1 | 0 <= i < j < NQ]
	NQ = 10
	nnpairs = defaultdict(list)
	n1 = [0] * NQ
	for i in itertools.product(range(2), repeat=NQ):
		npairs = 0
		for j in range(NQ):
			for k in range(0, j):
				if i[j] == 0 and i[k] == 1:
					npairs += 1
		nnpairs[i.count(1)].append(npairs)
	x = []
	y = []
	for k, v in sorted(nnpairs.items()):
		x.append(k)
		avg = sum(v) / len(v)
		y.append(avg)
		print(k, avg, sep='\t')
		# f(x) = a * x**2 + b * x + c
		# f(0) = 0 = c							c = 0
		# f(NQ) = 0 = a * NQ**2 + b * NQ		a * NQ + b = 0
		# f(1) = (NQ - 1) / 2 = a + b			a * (NQ - 1) = (1 - NQ) / 2
		# a = -1/2, b = NQ / 2
		assert avg == -1/2 * k**2 + NQ/2 * k
	if not 'plot':
		import matplotlib.pyplot as plt
		plt.plot(x, y)
		plt.show()
	exit()

T = int(input())
P = int(input())

def f(x):
	return 1 / (1 + math.e**(-x))

NP = 100
NQ = 10000

for test in range(T):
	result = []
	for i in range(NP):
		result.append(input())
		# result[-1] = result[-1][:NQ]
	diff2index = defaultdict(set)
	diff = []
	for index, i in enumerate(zip(*result)):
		diff2index[i.count('1')].add(index)
		diff.append(i.count('1'))
	npairs = []
	if not 'check':
		for i in range(NQ):
			assert i in diff2index[diff[i]]
	for i in result:
		np = 0
		easier_incorrect = i.count('0')
		for j in range(NP, -1, -1):
			n0 = 0
			n1 = 0
			for k in diff2index[j]:
				if i[k] == '0':
					n0 += 1
				else:
					n1 += 1
			easier_incorrect -= n0
			np += n1 * easier_incorrect
		k = i.count('0')
		npairs.append(np / (-1/2 * k**2 + NQ/2 * k + 1))
		if not 'check':
			np2 = 0
			print(np, end='\t', flush=True)
			for j in range(NQ):
				for k in range(NQ):
					if i[j] == '0' and i[k] == '1' and diff[j] < diff[k]:
						np2 += 1
			print(np2)
			assert np == np2
#	for i in sorted(enumerate(npairs, 1), key=lambda x: x[1]): print(i, sep='\t')
	m = min(enumerate(npairs, 1), key=lambda x: x[1])
	# print(m)
	ans = m[0]
	print('Case #%d:' % (test + 1), ans)

