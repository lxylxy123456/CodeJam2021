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
from collections import defaultdict
# A = list(map(int, input().split()))

T, N, B, P = list(map(int, input().split()))
for test in range(T):
	heights = [0] * N
	h2i = defaultdict(set)
	h2i[0] = set(range(20))
	def place(n):
		print(n + 1)
		h = heights[n]
		h2i[h].remove(n)
		h += 1
		heights[n] = h
		h2i[h].add(n)
	for i in range(N * B):
		D = int(input())
		if D >= 9 or (D >= 7 and i >= N * B * 0.8):
			place(next(iter(h2i[max(filter(lambda x: x != B, heights))])))
#		elif D <= 1 or (D <= 4 and i >= N * B * 0.8):
#			place(next(iter(h2i[min(filter(lambda x: x != B, heights))])))
		elif not h2i[B - 1] or (i <= N * B * 0.8 and len(h2i[B - 1]) < 2):
			place(next(iter(h2i[max(filter(lambda x: x < B - 1, heights))])))
		else:
			m = min(filter(lambda x: x != B, heights))
			a = next(iter(h2i[m]))
#			print(m, a, heights[a], heights, h2i, file=sys.stderr)
			place(a)
	assert heights == [B] * N
# 
#   1000000000000000

print('               860939810732536850', file=sys.stderr)
print('               937467793908762347', file=sys.stderr)
print(input(), file=sys.stderr)	# should be 1 on AC

# 47 min, AC WA (estimated based on local testing)

