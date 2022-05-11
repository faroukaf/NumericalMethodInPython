m = int(input("number of varabiles: "))
equiation = []

def mysum(li, le, eq, i):
	out = eq[i][m]
	j = 0
	while j < i:
		out -= (eq[i][j] * le[j])
		j += 1
	j += 1
	while j < m:
		out -= (eq[i][j] * li[j])
		j += 1
	return out / eq[i][i]

# get equation
i = 0 
while i < m:
 	eq = []
 	j = 0
 	while j < m:
 		eq.append(int(input("a{}{}".format(i+1, j+1))))
 		j += 1
 	eq.append(int(input("b{}".format(i+1))))
 	equiation.append(eq)
 	i += 1

print(len(equiation), "\n", equiation)

varabiles = [[0 for i in range(m)], [0 for i in range(m)]]
our = 0
n = 0

while 1:
	other = (our + 1) % 2
	print(n, ":", varabiles[our])
	c = varabiles[our][0]
	i = 0
	while i < m:
		varabiles[other][i] = mysum(varabiles[our], varabiles[other], equiation, i)
		i += 1
	temp = varabiles[other][0] - c
	check = temp * (-1) ** int(temp < 0)
	if check < 10 ** -4:
		print(n + 1, ":", varabiles[other])
		break
	our = other
	n += 1



