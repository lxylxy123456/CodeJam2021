import random, sys
T = 100
print(T)
for t in range(T):
	dat = (
		random.randint(1, 100),
		random.randint(1, 100),
		''.join(random.choices('CJ?', k=random.randint(1, 10))),
	)
	print(*dat)

