T, N, Q = map(int, input().split())
q = Q // T

def query(x, y, z):
	print(x, y, z)
	return int(input())

for test in range(T):
	a = query(1, 2, 3)
	x = [1, 2, 3]
	x.remove(a)
	small, large = x
	ans = [small, a, large]
	for i in range(4, N + 1):
		min_possible = 0
		max_possible = len(ans)
		while min_possible != max_possible:
			assert min_possible < max_possible
			if len(range(min_possible, max_possible)) == 1:
				if min_possible:
					min_possible -= 1
				else:
					max_possible += 1
			if len(range(min_possible, max_possible)) == 2:
				qry0 = min_possible
				qry1 = max_possible - 1
			else:
				sep = len(range(min_possible, max_possible)) // 3
				assert sep
				qry0 = min_possible + sep
				qry1 = min_possible + sep * 2
			b = query(i, ans[qry0], ans[qry1])
			if b == i:
				min_possible = qry0 + 1
				max_possible = qry1
			elif b == ans[qry0]:
				max_possible = qry0
			else:
				assert b == ans[qry1]
				min_possible = qry1 + 1
		ans.insert(min_possible, i)

	print(' '.join(map(str, ans)))
	if int(input()) != 1:
		break

