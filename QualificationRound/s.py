try:
	import sys
	stdin = sys.stdin
	stdin = open('c.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

print(input())

