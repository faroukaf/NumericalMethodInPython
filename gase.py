m = int(input("number of varabiles: "))
equiation = []

def mysum(li, eq, i):
	out = eq[i][m]
	temp = []
	j = 0
	while j < i:
		temp.append(j)
		out -= (eq[i][j] * li [j])
		j += 1
	j += 1
	while j < m:
		temp.append(j)
		out -= (eq[i][j] * li [j])
		j += 1	
	return out / eq[i][i]

# get equation
i = 0 
while i < m:
 	eq = []
 	j = 0
 	while j < m:
 		eq.append(int(input("a{}{}: ".format(i+1, j+1))))
 		j += 1
 	eq.append(int(input("b{}: ".format(i+1))))
 	equiation.append(eq)
 	i += 1

print(len(equiation), "\n", equiation)

varabiles = [0 for i in range(m)]
n = 0
while 1:
	i = 0
	print(n, ":", varabiles)
	c = varabiles[0]
	while i < m:
		varabiles[i] = mysum(varabiles, equiation, i)
		i += 1
	temp = varabiles[0] - c
	check = temp * (-1) ** int(temp < 0)
	if check < 10 ** -4:
		print(n + 1, ":", varabiles)
		break
	n += 1


