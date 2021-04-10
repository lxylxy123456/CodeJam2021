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
	N = int(input())
	X = input().split()
	assert len(X) == N
	ans = 0
	x0 = X[0]
	for x1 in X[1:]:
		if len(x1) >= len(x0):
			if int(x1) <= int(x0):
				ans += 1
				x1 += '0'
			else:
				pass
		else:
			# x1 = 1
			# x0 = 234
			if x1 + '0' * (len(x0) - len(x1)) > x0:
				ans += len(x0) - len(x1)
				x1 += '0' * (len(x0) - len(x1))
			elif x1 + '9' * (len(x0) - len(x1)) <= x0:
				ans += len(x0) - len(x1) + 1
				x1 += '0' * (len(x0) - len(x1) + 1)
			else:
				new_x1 = str(int(x0) + 1)
				assert new_x1.startswith(x1)
				ans += len(new_x1) - len(x1)
				x1 = new_x1
		assert int(x0) < int(x1)
		x0 = x1
	print('Case #%d:' % (test + 1), ans)

