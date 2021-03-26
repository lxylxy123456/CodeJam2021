try:
	import os, sys
	stdin = sys.stdin
	# stdin = open('s.txt')
	stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


import math, operator
T = int(input())
P = int(input())

def f(x):
	return 1 / (1 + math.e**(-x))

for test in range(T):
	result = []
	for i in range(100):
		result.append(input())
	skill = []
	for i in result:
		correct_rate = i.count('1') / 10000
		# f(x) := 1 / (1 + %e**(-x));
		# plot2d(integrate(f(s - q), q, -3, 3) / 6, [s, -3, 3]);
		# plot2d(((integrate(f(s - q), q, -3, 3) / 6) - 0.5) * 7.5, [s, -3, 3]);
		skill.append((correct_rate - 0.5) * 7.5)
	diff = []
	for i in range(10000):
		guess = [-2.75, -2.25, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25,
					1.75, 2.25, 2.75]
		prob = [0] * len(guess)
		for r, s in zip(result, skill):
			correct = r[i] == '1'
			for index, q in enumerate(guess):
				if correct:
					prob[index] += f(s - q)
				else:
					prob[index] += 1 - f(s - q)
		diff.append(guess[max(enumerate(prob), key=operator.itemgetter(1))[0]])
	fukashigis = []
	for i in range(100):
		fukashigi = 0
		for j in range(10000):
			if result[i][j] == '1':
				fukashigi += 1 - f(skill[i] - diff[j])
			else:
				fukashigi += f(skill[i] - diff[j])
		fukashigis.append(fukashigi)
	print(skill)
	print(diff)
	print(fukashigis)
	ans = min(enumerate(fukashigis), key=operator.itemgetter(1))[0] + 1
	print('Case #%d:' % (test + 1), ans)

