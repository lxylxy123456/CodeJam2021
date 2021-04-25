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

T = int(input())
for test in range(T):
	A, B, C = list(map(int, input().split()))
	# speed of hour hand: 1 tick / ns
	# speed of min hand: 12 tick / ns
	# speed of sec hand: 720 tick / ns
	# 1 deg = 12 * 10**10 ticks
	# 360 deg = 12 * 360 * 10**10 ticks
	# 12 hrs = 12 * 3600 * 10**9 ns
	# input: A, B, C
	# hands: H, M, S
	# nticks
	# output: h, m, s, n
	round_ticks = 432 * 10**11
	# H = nticks
	# M = (nticks * 12) % round_ticks
	# S = (nticks * 720) % round_ticks
	# nticks in [0, round_ticks)
	# Test case 1
	nticks = None
	for H, MS in [(A, {B, C}), (B, {A, C}), (C, {A, B})]:
		M = (H * 12) % round_ticks
		S = (H * 720) % round_ticks
		if {M, S} == MS:
			nticks = H
			break

	# Test case 2 / 3
	if nticks is None:
		# M - H = (nticks * 11) % round_ticks
		# S - M = (nticks * 708) % round_ticks
		# nticks * 11 in [0, round_ticks * 11)
		for H, M, S in [(A, B, C), (A, C, B), (B, A, C), (B, C, A), (C, A, B),
						(C, B, A)]:
			MH_rem = (M - H) % round_ticks
			SM_rem = (S - M) % round_ticks
			for MH_quo in range(11):
				MH = MH_quo * round_ticks + MH_rem
				if MH % 11 == 0:
					nticks_guess = MH // 11
					SM = nticks_guess * 708
					if SM % 708 == 0:
						# check
						HH = nticks_guess
						MM = (nticks_guess * 12) % round_ticks
						SS = (nticks_guess * 720) % round_ticks
						HHH = (H - HH) % round_ticks
						MMM = (M - MM) % round_ticks
						SSS = (S - SS) % round_ticks
#						print(*map(lambda x: x / round_ticks,
#									(HH - H, MM - M, SS - S)))
						if len({HHH, MMM, SSS}) == 1:
							nticks = nticks_guess

	ans_n = nticks % 1000000000
	ans_s = (nticks // 1000000000) % 60
	ans_m = (nticks // (60 * 1000000000)) % 60
	ans_h = (nticks // (60 * 60 * 1000000000))
	ans = map(str, (ans_h, ans_m, ans_s, ans_n))
	print('Case #%d:' % (test + 1), ' '.join(ans))

# 37 min, AC AC AC

