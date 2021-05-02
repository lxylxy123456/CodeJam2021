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

def construct_roar(n, Y):
	ans = str(n)
	while int(ans) <= Y or ans == str(n):
		n += 1
		ans += str(n)
	# assert is_roar(ans)
	return int(ans)

def get_roar(Y):
	y = str(Y)
	# print(y)
	candid = []
	candid.append(construct_roar(int('1'), Y))
	candid.append(construct_roar(int('9'), Y))
	for i in range(1, len(y)):
		candid.append(construct_roar(int('9' * (i + 1)), Y))
		candid.append(construct_roar(int('1' + '0' * i), Y))
		for j in range(20):
			candid.append(construct_roar(int(y[:i]) + j, Y))
	return min(candid)
	# 99 -> 123
	# 999 -> 1011
	# 9999 -> 12345
	# 99999 -> 100101

	# 56789
	# 678910
	# 78910
	# 9899100
	# 99100
	

def is_roar(Y):
	for i in range(1, len(Y)):
		n = int(Y[:i])
		yy = Y[i:]
		count = 1
		while yy:
			n += 1
			if yy.startswith(str(n)):
				yy = yy[len(str(n)):]
				count += 1
			else:
				break
		else:
			if count >= 2:
				return True

def get_roar_slow(Y):
	Z = Y + 1
	while True:
		if is_roar(str(Z)):
			return Z
		Z += 1

if not 'dp':
	import random
	# for i in range(10000, 100000):
	while True:
		# i = random.randint(1, 100)
		i = random.randint(10000, 100000)
		# 59022	91011	78910
		# i = 59022
		# i = 9699999
		print(i, end='\t')
		a = get_roar(i)
		b = get_roar_slow(i)
		print(a, b, sep='\t')
		assert a == b
	print('pass')

T = int(input())
for test in range(T):
	Y = int(input())
	ans = get_roar(Y)
	if not 'dp':
		print(get_roar_slow(Y))
	print('Case #%d:' % (test + 1), ans)

# 35 min, AC AC (2 attempts total)

